import streamlit as st

from Proj3_repo.App.search import recommend


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Travel Explorer",
    page_icon="🌍",
    layout="wide"
)


# -------------------------------
# Custom CSS
# -------------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #f8fafc;
    }


    .hero {

        background: linear-gradient(
            135deg,
            #0ea5e9,
            #2563eb
        );

        padding: 40px;

        border-radius: 20px;

        color:white;

        text-align:center;

        margin-bottom:30px;

    }


    .hero h1 {

        font-size:48px;

    }


    .hero p {

        font-size:20px;

    }



    .card {

        background:white;

        padding:25px;

        border-radius:20px;

        box-shadow:
        0px 5px 20px rgba(0,0,0,0.08);

        margin-bottom:25px;

    }



    .country {

        color:#64748b;

        font-size:18px;

    }



    </style>

    """,

    unsafe_allow_html=True
)



# -------------------------------
# Header
# -------------------------------


st.markdown(
    """
    <div class="hero">

    <h1>
    🌍 AI Travel Explorer
    </h1>

    <p>
    Discover destinations using artificial intelligence
    </p>

    </div>

    """,

    unsafe_allow_html=True
)



# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:


    st.title(
        "⚙️ Settings"
    )


    st.write(
        "Customize your experience"
    )


    show_score = st.checkbox(
        "Show AI similarity score",
        True
    )


    st.info(
        """
        AI understands meaning,
        not only keywords.
        
        Example:
        "quiet romantic escape"
        can match Santorini.
        """
    )



# -------------------------------
# Search
# -------------------------------


st.subheader(
    "Where would you like to go?"
)



query = st.text_input(

    "",

    placeholder=
    "Example: relaxing beach vacation"

)



search = st.button(
    "✨ Explore Destinations"
)



# -------------------------------
# Results
# -------------------------------


if search:


    if not query:


        st.warning(
            "Please enter a travel preference."
        )


    else:


        results = recommend(
            query
        )


        st.success(
            f"Found {len(results)} recommendations"
        )



        for destination, score in results:



            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )



            st.subheader(
                f"📍 {destination.name}"
            )


            st.markdown(

                f"""
                <div class="country">
                🌎 {destination.country}
                </div>
                """,

                unsafe_allow_html=True
            )


            col1, col2 = st.columns(2)



            with col1:

                st.write(
                    "🏷 Category:",
                    destination.category
                )


            with col2:


                if show_score and score > 0:


                    percentage = int(
                        score * 100
                    )


                    st.write(
                        "🤖 AI Match"
                    )


                    st.progress(
                        min(
                            percentage,
                            100
                        )
                    )


                    st.write(
                        f"{percentage}%"
                    )



                else:


                    st.info(
                        "⭐ Popular destination"
                    )



            st.write(
                destination.description
            )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )