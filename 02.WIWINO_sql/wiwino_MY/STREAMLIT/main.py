import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


questions = [
    "Highlight 10 wines to boost sales.",
    "Prioritize a country for marketing.",
    "Select 3 top wineries for awards.",
    "Find wines with _coffee_, _toast_, _green apple_, _cream_, _citrus_ keywords. Confirm with 10 users.",
    "Top 3 global grapes and their 5 best-rated wines.",
    "Create a leaderboard for average wine ratings by country and vintage.",
    "Top 5 _Cabernet Sauvignon_ recommendations for a VIP client."
]


if 'selected_question' not in st.session_state:
    st.session_state.selected_question = None

if not st.session_state.selected_question:
    st.title("Welcome to VinoMetrics!")
    st.subheader("Unlocking the Financial Potential of Wine Data")
    st.markdown("""
    ### About VinoMetrics
    At **VinoMetrics**, we specialize in transforming wine data into actionable insights that drive business growth. Our interactive platform offers a comprehensive analysis of wine sales, trends, and key performance indicators to help you make informed decisions.

    Whether you're looking to understand market trends, optimize your product portfolio, or enhance your financial performance, VinoMetrics provides the tools you need to succeed in the competitive world of wine.
    """)

    st.sidebar.title("Question")
    selected_question = st.sidebar.radio("Select a question", questions)    

    st.session_state.selected_question = selected_question
else:
    st.title("Wine Insights")
    st.subheader(f"Selected Question: {st.session_state.selected_question}")
    if st.session_state.selected_question == questions[0]:
        st.write("Showing chart for highlighting top 10 wines")














# if "show_message" not in st.session_state:
#     st.session_state.show_message = False

# def show_message():
#     st.session_state.show_message = True


# if not st.session_state.show_message:


#     st.markdown("""
#     ### About VinoMetrics
#     At **VinoMetrics**, we specialize in transforming wine data into actionable insights that drive business growth. Our interactive platform offers a comprehensive analysis of wine sales, trends, and key performance indicators to help you make informed decisions.

#     Whether you're looking to understand market trends, optimize your product portfolio, or enhance your financial performance, VinoMetrics provides the tools you need to succeed in the competitive world of wine.
#     """)


#     if st.button("Get started"):
#         show_message()

# if st.session_state.show_message:
#     st.markdown("""
# ### We want to highlight 10 wines to increase our sales. Which ones should we choose and why?
# """)





















    
