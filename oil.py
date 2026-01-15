import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from scipy.signal import find_peaks

raw = pd.read_csv('C:\\Users\\mbmil\\Desktop\\KS oil.csv')
# add "OIL-P&A", "O&G-P&A" to include plugged and abandoned wells
raw = raw[(raw["Status"] == "Producing") & (raw["Total Depth"].notna()) & (raw["Well Type"].isin(["OIL", "O&G"])) &
          (raw["Completion Date Sort"].notna())]
print(raw.columns)
raw["yr"] = raw["Completion Date Sort"].str.rsplit('/', n=1).str[1].str[:4]
raw["year"] = raw["yr"].astype(int)


def mapit(counties=True):
    if counties:
        counties = gpd.read_file("C:\\Users\\mbmil\\Desktop\\counties.zip")
        kscounties = counties[counties["STATEFP"] == "20"]
        kscounties.plot(edgecolor="black", facecolor="none").set_axis_off()
        print(kscounties.crs)
    else:
        usa = gpd.read_file("C:\\Users\\mbmil\\Desktop\\usa.zip")
        ks = usa[usa["STUSPS"] == "KS"]
        ks.plot(edgecolor='black', facecolor='none').set_axis_off()
    plt.scatter(raw["Longitude (NAD27)"], raw["Latitude (NAD27)"], s=0.25, c=raw["Total Depth"], cmap="rainbow")
    # plt.scatter(raw["Longitude (NAD27)"], raw["Latitude (NAD27)"], s=2, c=raw["year"], cmap="rainbow")
    cbar = plt.colorbar(shrink=0.75)
    cbar.set_label("Total Depth (feet)", size=18)
    plt.tight_layout()
    plt.show()

def distribution():
    y=raw["Total Depth"]
    kde = gaussian_kde(y)
    x = np.linspace(y.min(), y.max(), 100)
    density = kde(x)
    peaks, _ = find_peaks(density, prominence=0.00001)
    true_peaks = x[peaks]
    plt.hist(y, bins=100)
    for peak in true_peaks:
        plt.axvline(peak, color='r')
    plt.show()

mapit()
# distribution()