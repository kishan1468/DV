def createlayout():

    # Get query params safely
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

    # Default index handling
    default_selectbox = int(query_params.get("selectbox", 0))

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
