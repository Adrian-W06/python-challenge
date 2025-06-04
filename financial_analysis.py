import os
import pandas as pd

# Automatically find the CSV file in the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "C:\\Users\\bnewz\\Downloads\\Repo\\Python-Challenge\\PYbank\\Resources\\budget_data.csv")


df = pd.read_csv(file_path)


total_months = df.shape[0]


net_total = df["Profit/Losses"].sum()


df["Change"] = df["Profit/Losses"].diff()

#
average_change = df["Change"].iloc[1:].mean()
max_increase = df["Change"].max()
max_increase_date = df.loc[df["Change"].idxmax(), "Date"]

max_decrease = df["Change"].min()
max_decrease_date = df.loc[df["Change"].idxmin(), "Date"]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${int(max_increase)})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${int(max_decrease)})")


lines = []
lines.append("Financial Analysis")
lines.append("----------------------------")
lines.append(f"Total Months: {total_months}")
lines.append(f"Total: ${net_total}")
lines.append(f"Average Change: ${average_change:.2f}")
lines.append(f"Greatest Increase in Profits: {max_increase_date} (${int(max_increase)})")
lines.append(f"Greatest Decrease in Profits: {max_decrease_date} (${int(max_decrease)})")

# Print to terminal
for line in lines:
    print(line)
output_path = os.path.join(script_dir, "financial_analysis_results.txt")
with open(output_path, "w") as f:
    for line in lines:
        f.write(line + "\n")