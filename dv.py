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


# ---------------- Page Configuration ---------------- #
st.set_page_config(
    page_title="World Happiness Report",
    page_icon="🌍",
    layout="wide"
)


# ---------------- Compatibility Patch ---------------- #
# Support older calls to st.pyplot() that do not pass a figure.
if not getattr(st.pyplot, "_patched", False):
    _original_pyplot = st.pyplot

    def _pyplot_compat(fig=None, **kwargs):
        if fig is None:
            fig = plt.gcf()
            kwargs.setdefault("clear_figure", True)
        return _original_pyplot(fig, **kwargs)

    _pyplot_compat._patched = True
    st.pyplot = _pyplot_compat


# ---------------- Sidebar ---------------- #
def side_bar_homepage():
    st.sidebar.title("Author")
    st.sidebar.info("Kishan Kumar Sharma (19BCE2569)")


# ---------------- Homepage ---------------- #
def homepage():
    st.markdown(
        "<h1 style='text-align: center;'>WORLD HAPPINESS REPORT</h1>",
        unsafe_allow_html=True
    )

    st.write(
        "We are going to visualise the factors associated with "
        "happiness and identify countries with the highest happiness scores."
    )

    st.write(
        "The World Happiness Report is a publication of the Sustainable "
        "Development Solutions Network, using data from the Gallup World Poll."
    )

    st.markdown(
        "**Data source:** "
        "[World Happiness dataset on Kaggle]"
        "(https://www.kaggle.com/unsdsn/world-happiness)"
    )

    st.markdown(
        "We have visualized the dataset using different factors "
        "that may influence happiness scores."
    )

    criteria_list = [
        "Economy (GDP per Capita)",
        "Family",
        "Health (Life Expectancy)",
        "Freedom",
        "Trust (Government Corruption)",
        "Generosity",
    ]

    for criterion in criteria_list:
        st.markdown(f"**{criterion}**")

    st.write("Visualization tools used in this project:")

    # Show the image only if the file exists.
    import os

    if os.path.exists("Image/tool.png"):
        st.image("Image/tool.png", use_container_width=True)
    else:
        st.info(
            "Add Image/tool.png to the repository to display "
            "the visualization-tools image."
        )


# ---------------- Layout / Navigation ---------------- #
def createlayout():
    page_list = [
        "Homepage",
        "Country based analysis",
        "Average based analysis",
        "Spatial based analysis",
        "Heatmap of Continents",
        "Scatter plots",
        "Rank based Analysis",
        "Histogram of Scores Distribution",
    ]

    # Read and validate the saved page index.
    query_params = st.query_params
    try:
        default_selectbox = int(query_params.get("selectbox", 0))
    except (ValueError, TypeError):
        default_selectbox = 0

    default_selectbox = max(
        0, min(default_selectbox, len(page_list) - 1)
    )

    st.sidebar.title("Menu")

    app_mode = st.sidebar.selectbox(
        "Please select a page",
        page_list,
        index=default_selectbox,
    )

    # Preserve the selected page in the URL.
    selected_index = page_list.index(app_mode)
    if query_params.get("selectbox") != str(selected_index):
        st.query_params["selectbox"] = str(selected_index)

    # Route to the existing project modules.
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
