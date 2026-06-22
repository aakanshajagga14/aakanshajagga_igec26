from pathlib import Path
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

base = Path(__file__).resolve().parents[1]
data_dir = base / "data"
fig_dir = base / "figures"
fig_dir.mkdir(parents=True, exist_ok=True)

def save_meta(name, caption, description):
    with open(fig_dir / f"{name}.png.meta.json", "w") as f:
        json.dump({"caption": caption, "description": description}, f, indent=2)

df1 = pd.read_csv(data_dir / "fig1_data.csv")
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df1["Location"], y=df1["Actual Solar Potential (kWh/m²/day)"],
    name="Actual Solar Potential", marker_color="#8ecae6"
))
fig.add_trace(go.Bar(
    x=df1["Location"], y=df1["AI Recommendation Score"],
    name="AI Recommendation Score", marker_color="#ffb703"
))
fig.update_layout(
    barmode="group",
    title="Solar Potential vs AI Recommendation Score (simulated)",
)
fig.update_xaxes(title_text="Location")
fig.update_yaxes(title_text="Value")
fig.write_image(fig_dir / "figure01.png")
save_meta("figure01", "Figure 01: Solar potential vs AI recommendation score", "Grouped bar chart comparing actual solar potential and AI recommendation score across urban and rural locations.")

df2 = pd.read_csv(data_dir / "fig2_data.csv")
fig = px.box(df2, x="Site Type", y="Predicted ROI ($/kWh)", color="Site Type")
fig.update_layout(title="Predicted ROI by Site Type (simulated)")
fig.update_xaxes(title_text="Site Type")
fig.update_yaxes(title_text="Predicted ROI")
fig.write_image(fig_dir / "figure02.png")
save_meta("figure02", "Figure 02: Predicted ROI by location type", "Boxplot showing higher predicted ROI for urban than rural sites.")

df3 = pd.read_csv(data_dir / "fig3_data.csv")
fig = px.box(df3, x="Site Type", y="Model Score", color="Site Type")
fig.update_layout(title="Final AI Model Score by Site Type (simulated)")
fig.update_xaxes(title_text="Site Type")
fig.update_yaxes(title_text="Model Score")
fig.write_image(fig_dir / "figure03.png")
save_meta("figure03", "Figure 03: Final AI model score by location type", "Boxplot showing lower model scores for rural deployment sites.")

df4 = pd.read_csv(data_dir / "fig4_data.csv", header=None)
fig = px.imshow(
    df4,
    color_continuous_scale="YlGnBu",
    aspect="auto",
    origin="upper"
)
fig.update_layout(title="AI Model Confidence Across Simulated Region")
fig.update_xaxes(title_text="Longitude")
fig.update_yaxes(title_text="Latitude")
fig.write_image(fig_dir / "figure04.png")
save_meta("figure04", "Figure 04: AI model confidence heatmap", "Heatmap showing higher confidence in the northern urban half and lower confidence in the southern rural half.")
