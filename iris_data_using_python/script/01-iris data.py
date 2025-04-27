import pandas as pd

# Load the data
df = pd.read_csv(r'D:/my projects/iris_data_using_python/iris.csv')

# Clean column names (strip spaces and fix casing)
df.columns = df.columns.str.strip()

# Optional: Convert all column names to lowercase
df.columns = df.columns.str.lower()

# Now you can use lowercase safely
print(df.columns)  # Confirm names
print(df['species'].value_counts())  # Show how many of each species






# # import pandas as pd
# # import plotly.express as px

# # # Step 1: Load and clean data
# # df = pd.read_csv(r'D:/my projects/iris_data_using_python/iris.csv')
# # df.columns = df.columns.str.strip().str.lower()

# # # Step 2: Create interactive scatter plot
# # fig = px.scatter(
# #     df,
# #     x='sepal.length',
# #     y='sepal.width',
# #     color='species',
# #     size='petal.length',
# #     hover_data=['petal.width'],
# #     title='🌸 Iris Dataset: Sepal Size by Species',
# #     labels={
# #         'sepal.length': 'Sepal Length (cm)',
# #         'sepal.width': 'Sepal Width (cm)',
# #         'species': 'Species'
# #     },
# #     template='plotly_white'  # You can try 'plotly_dark', 'ggplot2', 'seaborn'
# # )

# # # Step 3: Save to HTML
# # fig.write_html("D:/my projects/iris_data_using_python/iris_plot.html")

# # # Optional: Show directly (for Visual Studio interactive window)
# # fig.show()



# print(df.columns)



# import plotly.express as px

# fig = px.scatter(
#     df,
#     x="sepal.length",
#     y="sepal.width",
#     color="species",
#     title="Sepal Length vs Sepal Width",
#     labels={"sepal.length": "Sepal Length", "sepal.width": "Sepal Width"}
# )
# fig.show()



# import plotly.express as px

# fig = px.scatter(
#     df,
#     x="petal.length",
#     y="petal.width",
#     color="species",
#     title="Petal Length vs Petal Width",
#     labels={"petal.length": "Petal Length", "petal.width": "Petal Width"}
# )
# fig.show()




# import plotly.express as px
# fig = px.scatter(
#     df,
#     x="sepal.length",
#     y="petal.length",
#     color="species",
#     title="Sepal Length vs Petal Length",
#     labels={"sepal.length": "Sepal Length", "petal.length": "Petal Length"}
# )
# fig.show()



# import plotly.express as px

# fig_3d = px.scatter_3d(
#     df,
#     x='sepal.length',
#     y='sepal.width',
#     z='petal.length',
#     color='species',
#     size='petal.width',
#     title='Iris Dataset in 3D',
#     template='plotly_dark'
# )

# fig_3d.write_html("D:/my projects/iris_data_using_python/iris_3d.html")





from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig_dash = make_subplots(rows=1, cols=2, subplot_titles=("Sepal Comparison", "Petal Comparison"))

# Sepal scatter
for species in df['species'].unique():
    filtered = df[df['species'] == species]
    fig_dash.add_trace(
        go.Scatter(
            x=filtered['sepal.length'],
            y=filtered['sepal.width'],
            mode='markers',
            name=f'Sepal - {species}',
            marker=dict(size=8),
        ),
        row=1, col=1
    )

# Petal scatter
for species in df['species'].unique():
    filtered = df[df['species'] == species]
    fig_dash.add_trace(
        go.Scatter(
            x=filtered['petal.length'],
            y=filtered['petal.width'],
            mode='markers',
            name=f'Petal - {species}',
            marker=dict(size=8),
        ),
        row=1, col=2
    )

fig_dash.update_layout(
    title_text="📊 Iris Dashboard: Sepal & Petal Analysis",
    showlegend=True,
    template="plotly_white",
    height=500
)

fig_dash.write_html("D:/my projects/iris_data_using_python/iris_dashboard.html")
