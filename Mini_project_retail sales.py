import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. Read the CSV file
# ==============================
df = pd.read_csv("sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("=== Retail Sales Data ===")
print(df)
print("\n")

# ==============================
# 2. Data Preparation
# ==============================
# Total sales per day
daily_sales = df.groupby("Date")["Sales"].sum().reset_index()

# Total sales per product
product_sales = df.groupby("Product")["Sales"].sum().reset_index()

# Sales of each product over time (for line chart)
pivot_df = df.pivot(index="Date", columns="Product", values="Sales")

print("=== Daily Total Sales ===")
print(daily_sales)
print("\n=== Product-wise Total Sales ===")
print(product_sales)
print("\n")

# ==============================
# 3. Create Visualizations
# ==============================
plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Retail Sales Dashboard", fontsize=18, fontweight="bold", y=0.98)

# ----- Chart 1: Line Chart - Daily Total Sales -----
axes[0, 0].plot(daily_sales["Date"], daily_sales["Sales"], 
                marker="o", linewidth=2.5, color="#2E86AB", markersize=8)
axes[0, 0].set_title("Daily Total Sales (Line Chart)", fontsize=13, fontweight="bold")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Total Sales")
axes[0, 0].tick_params(axis="x", rotation=30)
axes[0, 0].grid(True, alpha=0.3)

# ----- Chart 2: Bar Chart - Sales by Product -----
colors = ["#E94F37", "#44AF69"]
bars = axes[0, 1].bar(product_sales["Product"], product_sales["Sales"], 
                      color=colors, edgecolor="black", linewidth=0.7)
axes[0, 1].set_title("Total Sales by Product (Bar Chart)", fontsize=13, fontweight="bold")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Total Sales")

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    axes[0, 1].annotate(f"{int(height)}",
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 5), textcoords="offset points",
                        ha="center", va="bottom", fontweight="bold")

# ----- Chart 3: Line Chart - Product-wise Sales Trend -----
axes[1, 0].plot(pivot_df.index, pivot_df["Pen"], marker="o", label="Pen", 
                linewidth=2.5, color="#E94F37")
axes[1, 0].plot(pivot_df.index, pivot_df["Book"], marker="s", label="Book", 
                linewidth=2.5, color="#44AF69")
axes[1, 0].set_title("Product-wise Sales Trend (Line Chart)", fontsize=13, fontweight="bold")
axes[1, 0].set_xlabel("Date")
axes[1, 0].set_ylabel("Sales")
axes[1, 0].legend()
axes[1, 0].tick_params(axis="x", rotation=30)
axes[1, 0].grid(True, alpha=0.3)

# ----- Chart 4: Grouped Bar Chart - Daily Sales by Product -----
x = range(len(pivot_df.index))
width = 0.35

bars1 = axes[1, 1].bar([i - width/2 for i in x], pivot_df["Pen"], width, 
                       label="Pen", color="#E94F37", edgecolor="black")
bars2 = axes[1, 1].bar([i + width/2 for i in x], pivot_df["Book"], width, 
                       label="Book", color="#44AF69", edgecolor="black")

axes[1, 1].set_title("Daily Sales by Product (Grouped Bar Chart)", fontsize=13, fontweight="bold")
axes[1, 1].set_xlabel("Date")
axes[1, 1].set_ylabel("Sales")
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels([d.strftime("%Y-%m-%d") for d in pivot_df.index], rotation=30)
axes[1, 1].legend()

plt.tight_layout(rect=(0, 0, 1, 0.95))
plt.savefig("retail_sales_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()

print("Dashboard saved as 'retail_sales_dashboard.png'")