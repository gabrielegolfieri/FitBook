import plotly.graph_objects as go

tempi = ["0", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24"]
temperatura = [32.1, 31.8, 32.5, 33.0, 32.7, 31.9, 32.3, 33.1, 32.6, 32.0, 31.7, 32.1, 32.5, 32.4]


fig = go.Figure()
fig.add_trace(go.Bar(x=tempi, y=temperatura, name="Temperatura del polso", marker=dict(color='magenta')))

fig.update_layout(
    title="Temperatura del polso",
    xaxis_title="Ora",
    yaxis_title="Temperatura del polso (°C)"
)

fig.write_html("docs/grafico_interattivo_polso.html")