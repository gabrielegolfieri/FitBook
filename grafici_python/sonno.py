import plotly.graph_objects as go

categorie = ["Veglia", "Sonno leggero", "Sonno profondo", "REM"]

valori = [0.4, 4, 2, 1.6]

fig = go.Figure(data=[go.Pie(labels=categorie, values=valori)])

fig.update_layout(
    title="Distribuzione del sonno"
)

fig.write_html("../docs/grafico_interattivo_sonno.html")
