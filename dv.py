# ---------------- Sidebar ---------------- #
def side_bar_homepage():
    st.sidebar.title("🌍 World Happiness Dashboard")
    st.sidebar.markdown(
        "Explore happiness indicators across countries."
    )

    st.sidebar.divider()

    st.sidebar.subheader("Navigation")

    page = st.sidebar.radio(
        "Choose a section:",
        [
            "Home",
            "Correlation Analysis",
            "Average Happiness",
            "Spatial Analysis",
            "Country Comparison",
            "Graphs",
            "Country Rankings",
            "Distribution Analysis",
        ],
    )

    return page


# ---------------- Main Application ---------------- #
def main():
    st.set_page_config(
        page_title="World Happiness Dashboard",
        page_icon="🌍",
        layout="wide",
    )

    st.title("🌍 World Happiness Report")
    st.markdown(
        "Explore global happiness scores and their relationship "
        "with economic and social indicators."
    )

    page = side_bar_homepage()

    if page == "Home":
        st.subheader("Welcome")
        st.write(
            "Use the sidebar to explore happiness data, compare "
            "countries, and analyze factors associated with happiness."
        )

    elif page == "Correlation Analysis":
        st.subheader("Correlation Analysis")
        st.info("Connect your correlation-analysis module here.")

    elif page == "Average Happiness":
        st.subheader("Average Happiness")
        st.info("Connect your average-happiness module here.")

    elif page == "Spatial Analysis":
        st.subheader("Spatial Analysis")
        st.info("Connect your spatial-analysis module here.")

    elif page == "Country Comparison":
        st.subheader("Country Comparison")
        st.info("Connect your country-comparison module here.")

    elif page == "Graphs":
        st.subheader("Graphs")
        st.info("Connect your graph module here.")

    elif page == "Country Rankings":
        st.subheader("Country Rankings")
        st.info("Connect your ranking module here.")

    elif page == "Distribution Analysis":
        st.subheader("Distribution Analysis")
        st.info("Connect your distribution-analysis module here.")


if __name__ == "__main__":
    main()
