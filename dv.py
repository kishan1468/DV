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


# ---------------- Compatibility patch ---------------- #
# New Streamlit versions require a figure in st.pyplot(); old calls had none.
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
