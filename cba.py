import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = 'data/happiness_combined_year copy 2.csv'

df = pd.read_csv(DATA_PATH)
df = df.drop(columns=['Unnamed: 0'])

FACTORS = [
    ('Economy (GDP per Capita)', 'red'),
    ('Family', 'blue'),
    ('Health (Life Expectancy)', 'green'),
    ('Freedom', 'yellow'),
    ('Trust (Government Corruption)', 'orange'),
    ('Generosity', 'magenta'),
]


def plot_fac(data):
    """Six small charts (one per happiness factor) for one country."""
    fig, axes = plt.subplots(3, 2, figsize=(16, 8))
    for ax, (column, color) in zip(axes.flat, FACTORS):
        sns.pointplot(x="Year", y=column, data=data, color=color, ax=ax)
    fig.tight_layout()
    return fig


def plot(lst, data=df):
    for country in lst:
        d = data[data['Country'] == country]

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.pointplot(x="Year", y="Happiness Rank", data=d, ax=ax)
        ax.set_title(country)
        st.pyplot(fig)
        plt.close(fig)

        fig = plot_fac(d)
        st.pyplot(fig)
        plt.close(fig)


def info():
    countries = df['Country'].unique()
    countries_selected = st.multiselect('Select countries', countries)

    if not countries_selected:
        st.info('Select at least one country to see its charts.')
        return

    plot(countries_selected)


def load_page():
    st.markdown("<h1 style='text-align: center;'>Country based analysis</h1>",
                unsafe_allow_html=True)
    info()


if __name__ == "__main__":
    load_page()
