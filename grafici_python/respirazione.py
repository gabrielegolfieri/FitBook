import plotly.graph_objects as go

tempi = ["0:00", "2:00", "4:00", "6:00", "8:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00", "24:00"]
frequenza = [14, 16, 15, 13, 17, 30, 32, 18, 14, 35, 40, 16, 15]

fig = go.Figure()

fig.add_trace(go.Scatter(x=tempi, y=frequenza, mode='lines+markers', name="Frequenza", line=dict(color='skyblue')))

fig.update_layout(
    title="Frequenza Respiratoria",
    xaxis_title="Ora della giornata",
    yaxis_title="Atti respiratori al minuto",
    template="plotly_white"
)

fig.write_html("../docs/grafico_interattivo_respirazione.html")