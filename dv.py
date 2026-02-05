import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

import cba
import avg
import spatial
import con
import graph
import rank
import histo


# ---------------- Sidebar ---------------- #
def side_bar_homepage():
    st.sidebar.title("Team Members")
    st.sidebar.info("Kishan kumar sharma (19BCE2569)")
    st.sidebar.info("Aditya Narayan (19BCE2172)")


# ---------------- Homepage ---------------- #
def homepage():
    st.markdown(
        "<h1 style='text-align: center;'>WORLD HAPPINESS REPORT</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<span style='background-color:#121922'>",
        unsafe_allow_html=True
    )

    st.write(
        "We are going to visualise what are the factors and which countries "
        "have the most happy population."
    )

    st.write(
        "The World Happiness Report is a publication of the Sustainable "
        "Development Solutions Network, powered by data from the Gallup World Poll."
    )

    st.markdown(
        "**Data source:** [Kaggle](https://www.kaggle.com/unsdsn/world-happiness)"
    )

    st.markdown(
        "We have visualized the dataset using different factors which influence happiness score."
    )

    criteria_list = [
        'Economy (GDP per Capita)',
        'Family',
        'Health (Life Expectancy)',
        'Freedom',
        'Trust (Government Corruption)',
        'Generosity'
    ]

    for i in criteria_list:
        st.markdown(f"**{i}**")

    st.write("We have used these visualization tools:")
    st.image("Image/tool.png", use_column_width=True)


# ---------------- Layout / Navigation ---------------- #
def createlayout():

    # Safe query params handling
    query_params = dict(st.query_params)

    st.sidebar.title("Menu")

    page_list = [
        "Homepage",
        "Country based analysis",
        "Average based analysis",
        "Spatial based analysis",
        "Heatmap of Continents",
        "Scatter plots",
        "Rank based Analysis",
        "Histogram of Scores Distribution"
    ]

    # Default page index
    default_selectbox = int(query_params.get("selectbox", 0))

    # Sidebar selector
    app_mode = st.sidebar.selectbox(
        "Please select a page",
        page_list,
        index=default_selectbox
    )

    # Update query params
    query_params["selectbox"] = page_list.index(app_mode)
    st.query_params.clear()
    st.query_params.update(query_params)

    # Page routing
    if app_mode == "Homepage":
        homepage()

    elif app_mode == "Country based analysis":
        cba.load_page()

    elif app_mode == "Average based analysis":
        avg.load_page()

    elif app_mode == "Spatial based analysis":
        spatial.viz_page()

    elif app_mode == "Heatmap of Continents":
        con.load_page()

    elif app_mode == "Scatter plots":
        graph.load_page()

    elif app_mode == "Rank based Analysis":
        rank.load_page()

    elif app_mode == "Histogram of Scores Distribution":
        histo.load_page()


# ---------------- Main ---------------- #
def main():
    side_bar_homepage()
    createlayout()


if __name__ == "__main__":
    main()
