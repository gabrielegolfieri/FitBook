import plotly.graph_objects as go

tempi = ["0", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24"]
frequenza = [70, 75, 76, 77, 75, 110, 113, 75, 77, 114, 115, 77, 77]

fig = go.Figure()

fig.add_trace(go.Scatter(x=tempi, y=frequenza, mode='lines+markers', name="Frequenza", 
                         yaxis='y1', line=dict(color='crimson')))

fig.update_layout(
    title="Frequenza Cardiaca",
    xaxis_title="Ora",
    yaxis_title="Frequenza Cardiaca (bpm)",
    template="plotly_white"
)

fig.write_html("docs/grafico_interattivo_cuore.html")