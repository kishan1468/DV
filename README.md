# World Happiness Report — Data Visualization

An interactive data visualization project exploring global happiness scores and the socioeconomic factors associated with them using Python and Streamlit.

## Live Demo

**[Explore the Interactive Dashboard](https://worldhappinessreportdv.streamlit.app/?selectbox=0)**

## Project Overview

The World Happiness Report is a publication associated with the Sustainable Development Solutions Network. This project explores country-level happiness scores and examines how different economic, social, and health-related indicators vary across countries.

Using exploratory data analysis and interactive visualizations, the application helps users compare countries, investigate indicator relationships, and explore patterns in happiness scores.

## Key Indicators

The project explores the following factors:

- **Economy (GDP per Capita):** Economic conditions and their association with happiness scores.
- **Family:** Social support and family-related indicators.
- **Health (Life Expectancy):** The relationship between life expectancy and reported happiness.
- **Freedom:** The association between perceived freedom and happiness.
- **Trust (Government Corruption):** The relationship between perceptions of corruption and happiness.
- **Generosity:** The association between generosity and happiness.

## Features

- Interactive country-level analysis
- Comparison of happiness indicators
- Regional correlation heatmaps
- Scatter plots for exploring relationships between variables
- Country rankings and score distributions
- Historical comparisons across available years
- Interactive dashboard built with Streamlit

## Technology Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Application:** Streamlit
- **Dataset:** World Happiness data

## Dataset

The project uses the World Happiness dataset available on Kaggle.

**[View the dataset on Kaggle](https://www.kaggle.com/unsdsn/world-happiness)**

Please refer to the original dataset documentation for details about data collection, definitions, and attribution.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/kishan1468/World-Happiness-Report-Data-Vizualisation.git
cd World-Happiness-Report-Data-Vizualisation
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run dv.py
```

## Project Objective

The objective is to use exploratory data analysis and interactive visualization to understand how happiness scores differ across countries and how these differences relate to economic, social, and health-related indicators.

**Note:** Observed relationships indicate associations, not necessarily causal effects.

## Author

**Kishan Kumar Sharma**

[GitHub Profile](https://github.com/kishan1468)
