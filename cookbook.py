import streamlit as st
import numpy as np
import pandas as pd

cookbook = st.sidebar.radio(
    "Cookbook",
    [
        "Description",
        "Dataframe formatting",
        "Side-by-side charts",
        "Select rows",
        "Range slider",
        "Advanced selectbox",
        "Seaborn",
        "Wordcloud",
        "Emojis",
    ],
)

if cookbook == "Description":
    """
    ## Streamlit Cookbook
    Here are a few code snippets and examples of common functionality people like to add to their Streamlit apps. :balloon:

    - To see the full functionality of Streamlit, check out our [user documentation](https://docs.streamlit.io/en/latest/). 
    - Need help with Streamlit? Stop by the [Streamlit community forum](https://discuss.streamlit.io/) and say hello!
    - Have an example you'd like to share? [Submit a pull request on GitHub](https://github.com/kellyamanda/cookbook)!
    """

if cookbook == "Dataframe formatting":
    """
    ## Formatting Dataframes
    Use a [Pandas styler object](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html) to change the style of a rendered dataframe.
    """

    with st.echo():
        df = pd.DataFrame(
            np.random.randn(3, 5), columns=("col %d" % i for i in range(5))
        )

        def color_value(val):
            return "background-color: {}".format("red") if val < 0 else "black"

        df_color = df.style.applymap(color_value)
        df_color

if cookbook == "Side-by-side charts":

    """
    ## Side-by-side charts
    Streamlit will support horizontal layout by late 2020. In the meantime, you can use [Altair](https://altair-viz.github.io/) and [Plotly](https://plotly.com/python/) for side-by-sidebar
    layout of charts.

    ### Altair example
    """
    with st.echo():
        import altair as alt

        # Data
        df = pd.DataFrame(
            {
                "year": ["2010", "2011", "2010", "2011"],
                "animal": ["antelope", "antelope", "velociraptor", "velociraptor"],
                "count": [8, 6, 2, 4],
            }
        )

        # Altair chart with facet
        side_by_side_chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(x="animal", y="count",)
            .properties(width=200, height=200)
            .facet("year")
        )

        side_by_side_chart

    "### Plotly example"
    with st.echo():
        import plotly.graph_objs as go

        # Simple scatter plot
        scatter = go.Line(x=[5, 20, 35], y=[30, 20, 10])

        # Simple bar chart
        bar = go.Bar(
            x=[
                "velociraptor_2010",
                "velociraptor_2011",
                "velociraptor_2012",
                "velociraptor_2013",
            ],
            y=[5, 8, 11, 14],
            xaxis="x2",
            yaxis="y2",
        )

        # Data component
        data = [scatter, bar]

        # Layout component
        layout = go.Layout(
            xaxis=dict(domain=[0.0, 0.45]),
            xaxis2=dict(domain=[0.55, 1.0]),
            yaxis2=dict(overlaying="y", anchor="free", position=0.55),
        )

        # Figure component
        fig = go.Figure(data=data, layout=layout)

        st.plotly_chart(fig)

if cookbook == "Select rows":
    """
    ## Select rows in a dataframe
    We are working on adding functionality so you can directly interact with and edit charts and dataframes.
    In the meantime, you can use `st.multiselect` to select specific rows from a dataframe.
    """

    df = pd.DataFrame(
        {
            "date": ["2019-08-01", "2019-08-01", "2019-08-02", "2019-08-02"],
            "users": ["Sara", "James", "Sara", "James"],
            "events": ["3", "2", "5", "1"],
        }
    )

    # Select some rows using st.multiselect. This will break down when you have >1000 rows.
    st.write("### Full Dataset", df)
    selected_indices = st.multiselect("Select rows:", df.index)
    selected_rows = df.loc[selected_indices]
    st.write("### Selected Rows", selected_rows)

if cookbook == "Range slider":
    """
    ## Range slider
    Create a range slider by passing a two-element tuple or list as the value
    """
    with st.echo():
        values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

        st.write("Selected values:", values)

if cookbook == "Advanced selectbox":
    """
    ## Advanced st.selectbox functionality
    Use the `format_func` parameter to pass complex objects to `st.selectbox` (or `st.radio`) and choose what shows in the UI.

    ### Example 1
    """
    with st.echo():
        display = ("male", "female")

        options = list(range(len(display)))

        value = st.selectbox("gender", options, format_func=lambda x: display[x])

        st.write(value)

    "### Example 2"
    with st.echo():
        from vega_datasets import data

        @st.cache
        def load_data():
            return data.birdstrikes()

        cols = {
            "Airport__Name": "Airport Name",
            "Aircraft__Make_Model": "Aircraft Make & Model",
            "Effect__Amount_of_damage": "Effect: Amount of Damage",
            "Flight_Date": "Flight Date",
            "Aircraft__Airline_Operator": "Airline Operator",
            "Origin_State": "Origin State",
            "When__Phase_of_flight": "When (Phase of Flight)",
            "Wildlife__Size": "Wildlife Size",
            "Wildlife__Species": "Wildlife Species",
            "When__Time_of_day": "When (Time of Day)",
            "Cost__Other": "Cost (Other)",
            "Cost__Repair": "Cost (Repair)",
            "Cost__Total_$": "Cost (Total) ($)",
            "Speed_IAS_in_knots": "Speed (in Knots)",
        }

        dataset = load_data()

        column = st.selectbox(
            "Describe Column", list(dataset.columns), format_func=cols.get
        )

        st.write(dataset[column].describe())


if cookbook == "Seaborn":
    """
    ## Seaborn in Streamlit
    Seaborn builds on top of a Matplotlib figure so you can display the charts in the same way:
    """

    with st.echo():
        import seaborn as sns

        df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 30, 70]})
        sns.lineplot(x="x", y="y", data=df)
        st.pyplot()


if cookbook == "Wordcloud":
    """
    ## Create a Wordcloud
    Use Matplotlib and Wordcloud to create a simple wordcloud chart.
    """
    with st.echo():
        from wordcloud import WordCloud
        import matplotlib.pyplot as plt

        text = "Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing"

        # Create and generate a word cloud image:
        wordcloud = WordCloud().generate(text)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        st.pyplot()

if cookbook == "Emojis":
    """
    ## Emojis in Streamlit
    Use markdown formatting! Streamlit supports most standard emojis. [See full list here](https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json).
    """

    with st.echo():
        st.write("Showing :heart: for Streamlit :raised_hands:")
