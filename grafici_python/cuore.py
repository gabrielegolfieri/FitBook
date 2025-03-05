import plotly.graph_objects as go

tempi = ["0:00", "2:00", "4:00", "6:00", "8:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00", "24:00"]

frequenza = [70, 75, 76, 77, 75, 110, 113, 75, 77, 114, 115, 77, 77]

fig = go.Figure()

fig.add_trace(go.Scatter(x=tempi, y=frequenza, mode='lines+markers', name="Frequenza", line=dict(color='crimson')))

fig.update_layout(
    title="Frequenza Cardiaca",
    xaxis_title="Ora della giornata",
    yaxis_title="Frequenza Cardiaca (bpm)"
)

fig.write_html("../docs/grafico_interattivo_cuore.html")