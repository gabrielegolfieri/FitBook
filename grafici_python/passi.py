import plotly.graph_objects as go

giorni = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]

passi = [5000, 4500, 8000, 10000, 5500, 9500, 7000]

fig = go.Figure()

fig.add_trace(go.Bar(x=giorni, y=passi, name="Passi Giornalieri", marker=dict(color='orange')))

fig.update_layout(
    title="Numero di Passi Giornalieri",
    xaxis_title="Giorni",
    yaxis_title="Numero di Passi"
)

fig.write_html("../docs/grafico_interattivo_passi.html")
