# conda install -c conda-forge geopandas
import geopandas
import matplotlib.pyplot as plt

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
print(world.head())

world.plot()
plt.show()

print(world.geometry.name)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world['centroid_column'] = world.centroid
world = world.set_geometry('centroid_column')
world.plot()
plt.show()
print('#',50*"-")
# -----------------------
import fiona
help(fiona.open)
url = "http://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"
df = geopandas.read_file(url)
print(df.head())
print('#',50*"-")
# -----------------------
world = world[(world.pop_est>0) & (world.name!="Antarctica")]
world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
world.plot(column='gdp_per_cap')
plt.show()