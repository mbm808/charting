import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

raw = pd.read_csv('C:\\Users\\mbmil\\Desktop\\KS oil.csv')
raw = raw[raw["Status"] == "Producing"]
usa = gpd.read_file("C:\\Users\\mbmil\\Desktop\\usa.zip")
ks = usa[usa["STUSPS"] == "KS"]
ks.plot(edgecolor='black', facecolor='none').set_axis_off()
plt.scatter(raw["Longitude (NAD27)"], raw["Latitude (NAD27)"], s=0.25, c=raw["Total Depth"], cmap="rainbow")
plt.colorbar(label="Well Depth (ft)")
plt.show()


# plt.hist(raw["Total Depth"], bins=100)
# plt.show()
