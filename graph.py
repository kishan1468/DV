import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def info():

    # Load data
    df = pd.read_csv('data/avg.csv')

    # Sidebar selectors
    x = st.sidebar.selectbox(
        "X axis",
        tuple(df.columns.to_list()),
        index=0
    )

    y = st.sidebar.selectbox(
        "Y axis",
        tuple(df.columns.to_list()),
        index=1 if len(df.columns) > 1 else 0
    )

    # Create figure (Modern Streamlit Safe)
    fig, ax = plt.subplots(figsize=(8, 5))

    # Safe scatter plot
    sns.scatterplot(
        x=x,
        y=y,
        data=df,
        hue="Country" if "Country" in df.columns else None,
        ax=ax
    )

    # Legend outside plot
    if "Country" in df.columns:
        ax.legend(bbox_to_anchor=(1.01, 1.05), borderaxespad=0)

    ax.set_title(f"{y} vs {x}")

    # Streamlit render
    st.pyplot(fig)


def load_page():
    info()


if __name__ == "__main__":
    load_page()
