import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    all_eq_data =csv.reader(f)
    header = next(all_eq_data)

    bright, lons, lats, acq_date = [], [], [], []
    for eq_dict in all_eq_data:
        bright.append(eq_dict[2])
        lons.append(eq_dict[1])
        lats.append(eq_dict[0])
        acq_date.append(eq_dict[5])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': acq_date,
    'marker': {
        'size': [int(br[:3])//30 for br in bright],
        'color': [float(br) for br in bright],
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'fire hazard class'},
    },
}]

my_layout = Layout(title="world fires")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')