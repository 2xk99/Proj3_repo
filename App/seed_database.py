import numpy as np

from sentence_transformers import SentenceTransformer

from destinations import destinations

from Proj3_repo.App.database import engine

from Proj3_repo.App.models import destinations_table



model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)



with engine.begin() as connection:


    for item in destinations:


        # Check duplicate

        query = destinations_table.select().where(

            destinations_table.c.name == item["name"]

        )


        existing = connection.execute(
            query
        ).first()



        if existing:

            continue



        text = (

            item["name"]

            + " "

            + item["description"]

        )


        embedding = model.encode(
            text
        )


        embedding_bytes = (

            np.array(
                embedding,
                dtype=np.float32
            )

            .tobytes()

        )



        insert_query = destinations_table.insert().values(

            name=item["name"],

            country=item["country"],

            description=item["description"],

            category=item["category"],

            embedding=embedding_bytes

        )


        connection.execute(
            insert_query
        )



print(
    "Destinations inserted successfully!"
)