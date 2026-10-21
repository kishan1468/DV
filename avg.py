import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = 'data/happiness_combined_year copy 2.csv'

CHARTS = [
    ('Generosity', 'Average Generosity Country-wise'),
    ('Trust (Government Corruption)', 'Average Government Corruption Country-wise'),
    ('Freedom', 'Average Freedom Country-wise'),
    ('Economy (GDP per Capita)', 'Average GDP Country-wise'),
    ('Health (Life Expectancy)', 'Average Life Expectancy Country-wise'),
    ('Family', 'Average Social Support Country-wise'),
]


def info():
    df = pd.read_csv(DATA_PATH)
    df = df.drop(columns=['Unnamed: 0'])
    avg = (df.groupby('Country')
             .mean(numeric_only=True)
             .sort_values(by='Happiness Score', ascending=False)
             .reset_index())

    for column, title in CHARTS:
        ax = avg.plot('Country', column)
        ax.set_title(title)
        fig = ax.get_figure()
        st.pyplot(fig)
        plt.close(fig)


def load_page():
    st.markdown("<h1 style='text-align: center;'>Average Based Analysis</h1>",
                unsafe_allow_html=True)
    info()


if __name__ == "__main__":
    load_page()
