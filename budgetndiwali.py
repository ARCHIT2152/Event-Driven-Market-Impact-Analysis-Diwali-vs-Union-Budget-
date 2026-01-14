import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/nifty50.csv")

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.rename(columns={"Price": "Close"})
df["Close"] = df["Close"].astype(str).str.replace(",", "").astype(float)
df = df.sort_values("Date").reset_index(drop=True)

diwali_dates = {
    2006: "2006-10-21", 2007: "2007-11-09", 2008: "2008-10-28",
    2009: "2009-10-17", 2010: "2010-11-05", 2011: "2011-10-26",
    2012: "2012-11-13", 2013: "2013-11-03", 2014: "2014-10-23",
    2015: "2015-11-11", 2016: "2016-10-30", 2017: "2017-10-19",
    2018: "2018-11-07", 2019: "2019-10-27", 2020: "2020-11-14",
    2021: "2021-11-04", 2022: "2022-10-24", 2023: "2023-11-12",
    2024: "2024-11-01", 2025: "2025-10-21"
}

budget_dates = {
    2006: "2006-02-28", 2007: "2007-02-28", 2008: "2008-02-29",
    2009: "2009-07-06", 2010: "2010-02-26", 2011: "2011-02-28",
    2012: "2012-03-16", 2013: "2013-02-28", 2014: "2014-02-17",
    2015: "2015-02-28", 2016: "2016-02-29", 2017: "2017-02-01",
    2018: "2018-02-01", 2019: "2019-02-01", 2020: "2020-02-01",
    2021: "2021-02-01", 2022: "2022-02-01", 2023: "2023-02-01",
    2024: "2024-02-01", 2025: "2025-02-01"
}

def analyze_event(event_dates, event_name):
    data = []
    for year, date in event_dates.items():
        d = pd.to_datetime(date)
        before = df[(df["Date"] >= d - pd.Timedelta(days=15)) & (df["Date"] < d)]
        after = df[(df["Date"] > d) & (df["Date"] <= d + pd.Timedelta(days=15))]
        b = before["Close"].mean()
        a = after["Close"].mean()
        r = ((a - b) / b) * 100
        impact = "Positive" if r > 0 else "Negative" if r < 0 else "Neutral"
        data.append([year, d.date(), round(b, 2), round(a, 2), round(r, 2), impact])
    return pd.DataFrame(
        data,
        columns=["Year", f"{event_name} Date", "Avg Before", "Avg After", "Impact Return (%)", "Impact"]
    )

diwali_df = analyze_event(diwali_dates, "Diwali")
budget_df = analyze_event(budget_dates, "Budget")

#print(diwali_df)
#print(budget_df)

comparison_df = pd.merge(
    diwali_df,
    budget_df,
    on="Year",
    how="inner",
    suffixes=("_Diwali", "_Budget")
)

print(comparison_df)

years = list(range(2006, 2026))

plt.figure()
plt.plot(diwali_df["Year"], diwali_df["Avg Before"], label="Avg Before")
plt.plot(diwali_df["Year"], diwali_df["Avg After"], label="Avg After")
plt.xlim(2006, 2025)
plt.xticks(years, rotation=45)
plt.xlabel("Year")
plt.ylabel("NIFTY Value")
plt.title("Diwali: Avg Before vs After (2006–2025)")
plt.legend()
plt.show()

plt.figure()
plt.plot(diwali_df["Year"], diwali_df["Impact Return (%)"], marker="o")
plt.xlim(2006, 2025)
plt.xticks(years, rotation=45)
plt.xlabel("Year")
plt.ylabel("Impact Return (%)")
plt.title("Diwali Impact Trend (2006–2025)")
plt.axhline(0)
plt.show()

plt.figure()
plt.plot(budget_df["Year"], budget_df["Avg Before"], label="Avg Before")
plt.plot(budget_df["Year"], budget_df["Avg After"], label="Avg After")
plt.xlim(2006, 2025)
plt.xticks(years, rotation=45)
plt.xlabel("Year")
plt.ylabel("NIFTY Value")
plt.title("Budget: Avg Before vs After (2006–2025)")
plt.legend()
plt.show()

plt.figure()
plt.plot(budget_df["Year"], budget_df["Impact Return (%)"], marker="o")
plt.xlim(2006, 2025)
plt.xticks(years, rotation=45)
plt.xlabel("Year")
plt.ylabel("Impact Return (%)")
plt.title("Budget Impact Trend (2006–2025)")
plt.axhline(0)
plt.show()

comparison_df.to_csv("diwali_vs_budget_comparison.csv", index=False)

