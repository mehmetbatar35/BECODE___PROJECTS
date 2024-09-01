# VinoMetrics

<p align="center">
  <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="Streamlit Logo" width="150"/>
  <img src="https://www.sqlite.org/images/sqlite370_banner.gif" alt="SQLite Logo" width="150"/>
</p>

## Overview

**VinoMetrics** is an interactive Streamlit app designed to provide insights into wine trends and performance. The app features various data visualizations and analyses to help users make informed decisions regarding wine sales, marketing, and more.

## Features

- **Database Overview**: Displays information about the Wiwino database.
- **Top Wines**: Highlights the top 10 wines to boost sales.
- **Marketing Prioritization**: Helps prioritize countries for marketing efforts.
- **Top Wineries**: Identifies the top 3 wineries for awards.
- **Wine Characteristics**: Finds wines with specific characteristics such as coffee, toast, green apple, cream, and citrus.
- **Global Grapes**: Showcases the top 3 global grape varieties and their best-rated wines.
- **Leaderboard**: Creates a leaderboard for average wine ratings by country and vintage.
- **User Demographics**: Analyzes wine popularity among different user demographics.
- **Value for Money**: Identifies wines that offer the best value considering their ratings and prices.

## Installation

To run this Streamlit app locally, follow these steps:

1. ## Clone the Repository

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. ## Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. ## Install Dependencies 

Ensure you have pip installed, then run:

```bash
pip install streamlit matplotlib pandas numpy
```
4. ## Run the Streamlit App
```bash
streamlit run app.py
```

## Usage

### Navigate to the App

Open your web browser and go to [**Vinometrics**](http://mainpy-ftbfy4zmtcvfkaycbjruu4.streamlit.app) to view the app.

### Select a Question

Use the sidebar to select a question or topic of interest. The app will display relevant insights and visualizations based on your selection.

### View Insights

The main area of the app will update to show visualizations and information related to the selected question.


## Contributing

If you would like to contribute to the development of VinoMetrics, please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and passes all tests.

## Contact

For any questions or feedback, please contact [batar.mehmet@outlook.com].
