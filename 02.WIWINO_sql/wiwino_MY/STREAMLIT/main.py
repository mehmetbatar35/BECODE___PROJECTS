import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import base64
import os


def encode_image(image_file_path):
    with open(image_file_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
        return encoded_image

image_path = os.path.join('png', 'background.jpg')
encoded_image = encode_image(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/jpeg;base64,{encoded_image});
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center center;
        min-height: 100vh;
        background-color: rgba(0, 0, 0, 0.3); /* Adjust transparency */
    }}
    .stTitle {{
        color: white;
        font-weight: bold;
        font-size: 24px;
    }}
    .stSubheader {{
        color: #FFD700; /* Example color */
        font-weight: bold;
        font-size: 18px;
    }}
    .stMarkdown {{
        background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
        padding: 10px;
        border-radius: 5px;
        color: #F0F0F0; /* Light text color */
        text-shadow: 1px 1px 2px black; /* Text shadow */
    }}
    [data-testid="stSidebar"] {{
        background-color: rgba(0, 0, 0, 0.8); /* Dark sidebar background */
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


questions = [
    "Which database did I work with?",
    "Highlight 10 wines to boost sales.",
    "Prioritize a country for marketing.",
    "3 top wineries for awards.",
    "Find wines with _coffee_, _toast_, _green apple_, _cream_, _citrus_ keywords. Confirm with 10 users.",
    "Top 3 global grapes and their 5 best-rated wines.",
    "Create a leaderboard for average wine ratings by country and vintage.",
    "Which wines are most popular among different user demographics (e.g., by country or region of the users)?",
    "Which wines offer the best value for money, considering their ratings and prices?"
]
selected_question = st.sidebar.radio("VinoMetrics", options = [""] + questions)  




if selected_question:
    st.title("Wine Insights")
    if selected_question == questions[0]:
        st.write("Wiwino Database")
        image_path_00 = './png/database.png'
        st.image(image_path_00, caption = "Wiwino", use_column_width = True)
    elif selected_question == questions[1]:
        st.write("10 wines to boost sale")
        image_path_01 = './png/01.png'
        st.image(image_path_01, caption="Top 10 Wines", use_column_width= True)
    elif selected_question == questions[2]:
        st.write("Prioritize a country for marketing")
        image_path_02 = './png/02.png'
        st.image(image_path_02, caption="Country Marketing Priority", use_column_width= True)
    elif selected_question == questions[3]:
        st.write("3 top wineries for awards")
        image_path_03 = './png/3.png'
        st.image(image_path_03, caption="Top 3 Wineries", use_column_width= True)
    elif selected_question == questions[4]:
        st.write("Find Wines with Coffee, Toast, Green Apple, Cream, Citrus; Confirm with 10 Users.")
        image_path_04 = './png/4.png'
        st.image(image_path_04, caption="Find Wines: Coffee, Toast, Apple, Cream, Citrus; Confirm with 10 Users.", use_column_width= True)
    elif selected_question == questions[5]:
        st.write("Top 3 global grapes and their 5 best-rated wines.")
        image_path_05_0 = './png/5.0.png'
        st.image(image_path_05_0, caption="Top 3 global grapes", use_column_width= True)
        image_path_05_1 = './png/5.Cabernet Sauvignon.png'
        st.image(image_path_05_1, caption="5 best-rated wines of Cabernet Sauvignon", use_column_width= True)
        image_path_05_2 = './png/5.Merlot.png'
        st.image(image_path_05_2, caption="5 best-rated wines of Merlot", use_column_width= True)
        image_path_05_3 = './png/5.Chardonnay.png'
        st.image(image_path_05_3, caption="5 best-rated wines of Chardonnay", use_column_width= True)
    elif selected_question == questions[6]:
        st.write("Leaderboard: Avg. Wine Ratings by Country & Vintage")
        image_path_06_1 = './png/6.1.png'
        st.image(image_path_06_1, caption="Leaderboard: Avg. Wine Ratings by Country", use_column_width= True)
        image_path_06_2 = './png/6.2.png'
        st.image(image_path_06_2, caption="Leaderboard: Avg. Wine Ratings by Vintage", use_column_width= True)
    elif selected_question == questions[7]:
        st.write("Which Wines Are Most Popular by User Demographics (e.g., Country/Region)?")
        image_path_07_1 = './png/7.1.png'
        st.image(image_path_07_1, caption="By Region", use_column_width= True)
        image_path_07_2 = './png/7.2.png'
        st.image(image_path_07_2, caption="By Country", use_column_width= True)
    elif selected_question == questions[8]:
        st.write("Which Wines Offer the Best Value by Rating and Price?")
        image_path_08 = './png/8.png'
        st.image(image_path_08, caption="Best Value Wines by Rating and Price", use_column_width= True)

else:
    st.title("Welcome to VinoMetrics!")
    st.subheader("Unlocking the Financial Potential of Wine Data")
    st.markdown("""
    ### About VinoMetrics
    At **VinoMetrics**, we specialize in transforming wine data into actionable insights that drive business growth. Our interactive platform offers a comprehensive analysis of wine sales, trends, and key performance indicators to help you make informed decisions.

    Whether you're looking to understand market trends, optimize your product portfolio, or enhance your financial performance, VinoMetrics provides the tools you need to succeed in the competitive world of wine.
    """)















