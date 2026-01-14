# Event-Driven-Market-Impact-Analysis-Diwali-vs-Union-Budget-

## Overview
This project analyzes the impact of major Indian events — **Diwali** and the **Union Budget** — on the **NIFTY 50 index** using historical price data.  
It studies market behavior **15 days before and 15 days after** each event from **2006 to 2025**, compares average prices, calculates percentage impact, and visualizes long-term trends.

The project is suitable for **financial analysis, academic research, and event-driven market studies**.

---

## Objectives
- Analyze NIFTY 50 price movement around Diwali dates  
- Analyze NIFTY 50 price movement around Union Budget dates  
- Compare pre-event and post-event average prices  
- Calculate impact return percentages  
- Create a combined comparison table (Diwali vs Budget)  
- Visualize trends using Matplotlib  

---

## Data Source
- **Index:** NIFTY 50  
- **Format:** CSV  
- **Required Columns:**
  - `Date`
  - `Price`

Dataset path:


---

## Methodology
1. Convert dates to datetime format  
2. Clean and normalize price values  
3. Sort data chronologically  
4. Define fixed event dates (Diwali and Budget)  
5. Calculate:
   - Average price 15 days before the event  
   - Average price 15 days after the event  
   - Impact return percentage  
6. Classify impact as Positive, Negative, or Neutral  
7. Merge Diwali and Budget results into one comparison table  
8. Visualize results using line graphs  

---

## Output Tables
### Diwali Impact Table
Year-wise Diwali date, average prices before and after the event, impact return percentage, and impact type.

### Budget Impact Table
Year-wise Budget date with the same metrics.

### Comparison Table
A merged table comparing Diwali and Budget impacts for each year.

Exported file:


---

## Visualizations
The script generates:
- Average NIFTY value before vs after Diwali  
- Diwali impact return trend (2006–2025)  
- Average NIFTY value before vs after Budget  
- Budget impact return trend (2006–2025)  

All graphs use a fixed year range from **2006 to 2025**.

---

## Technologies Used
- Python 3  
- Pandas  
- Matplotlib  

---

## How to Run
```bash
pip install pandas matplotlib
python budgetndiwali.py
