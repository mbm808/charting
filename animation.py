import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf

def stocks(st="2020-01-01", en = "2020-12-31", tickers=["SPY", "GLD"], milliseconds=10, period="1d"):
    data, lens = {}, []
    for ticker in tickers:
        data[ticker] = yf.download(ticker, start=st, end=en, interval=period, multi_level_index=False).reset_index()
        data[ticker]["cper"] = data[ticker]["Close"]/data[ticker]["Close"][0]*100-100
        lens.append(len(data[ticker]["Date"]))
    frame_count = min(lens) + 50
    fig, ax = plt.subplots(1,1)
    all_percentages = pd.concat([df["cper"] for df in data.values()], ignore_index=True).to_frame("cper")
    mincper, maxcper = min(all_percentages["cper"]), max(all_percentages["cper"])
    ymin, ymax = mincper - ((maxcper - mincper)/10), maxcper + ((maxcper - mincper)/10)

    def animate(iter):
        ax.clear()
        ax.set_xlim(pd.Timestamp(st), pd.Timestamp(en))
        ax.set_ylim(ymin, ymax)
        for ticker in tickers:
            ax.plot(data[ticker]["Date"].iloc[:iter], data[ticker]["cper"].iloc[:iter], label=ticker)
        ax.legend(loc="upper left")

    anim = FuncAnimation(fig, animate, frames=frame_count, interval=milliseconds, repeat=True)
    plt.show()

stocks(tickers=["SPY", "QQQ", "DIA"], st="2000-01-01", en="2003-12-31", milliseconds=100, period="1d")