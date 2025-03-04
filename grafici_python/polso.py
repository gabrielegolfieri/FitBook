import plotly.graph_objects as go

tempi = ["0:00", "2:00", "4:00", "6:00", "8:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00", "24:00"]
temperatura = [32.1, 31.8, 32.5, 33.0, 32.7, 34.9, 34.3, 33.1, 32.6, 32.0, 34.7, 34.1, 32.5, 32.4]


fig = go.Figure()
fig.add_trace(go.Bar(x=tempi, y=temperatura, name="Temperatura del polso", marker=dict(color='magenta')))

fig.update_layout(
    title="Temperatura del polso",
    xaxis_title="Ora della giornata",
    yaxis_title="Temperatura del polso (°C)"
)

fig.write_html("../docs/grafico_interattivo_polso.html")