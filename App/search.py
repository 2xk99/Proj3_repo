import numpy as np

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity

from sqlalchemy import select

from Proj3_repo.App.database import engine

from Proj3_repo.App.models import destinations_table



model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)



def get_embedding(text):

    return model.encode(
        text
    ).reshape(1,-1)



def find_similar(user_input):


    input_embedding = get_embedding(
        user_input
    )


    results = []



    with engine.connect() as connection:


        query = select(
            destinations_table
        )


        rows = connection.execute(
            query
        )



        for row in rows:


            stored_embedding = np.frombuffer(

                row.embedding,

                dtype=np.float32

            ).reshape(1,-1)



            score = cosine_similarity(

                input_embedding,

                stored_embedding

            )[0][0]



            results.append(

                (
                    row,
                    score
                )

            )



    if not results:

        return []



    results.sort(

        key=lambda x:x[1],

        reverse=True

    )



    if results[0][1] < 0.30:

        return []



    return results[:3]



def fallback():


    with engine.connect() as connection:


        query = (

            select(destinations_table)

            .limit(3)

        )


        rows = connection.execute(
            query
        ).fetchall()



    return [

        (
            row,
            0
        )

        for row in rows

    ]



def recommend(user_input):


    results = find_similar(
        user_input
    )


    if not results:

        return fallback()


    return results