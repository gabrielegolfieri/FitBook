import plotly.graph_objects as go

tempi = ["0", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24"]
frequenza = [14, 16, 15, 13, 17, 30, 32, 18, 14, 35, 40, 16, 15]

fig = go.Figure()

fig.add_trace(go.Scatter(x=tempi, y=frequenza, mode='lines+markers', name="Frequenza", 
                         yaxis='y1', line=dict(color='skyblue')))

fig.update_layout(
    title="Frequenza Respiratoria",
    xaxis_title="Ora",
    yaxis_title="Atti respiratori al minuto",
    template="plotly_white"
)

fig.write_html("docs/grafico_interattivo_respirazione.html")