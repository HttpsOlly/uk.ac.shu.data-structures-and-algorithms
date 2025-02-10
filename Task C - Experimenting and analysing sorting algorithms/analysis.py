import pandas as pd
import matplotlib.pyplot as plt

file_path = "sorted_results.csv"

df = pd.read_csv(file_path)

df["Duration (seconds)"] = df["Duration (nanoseconds)"] / 1_000_000_000

df = df.rename(columns={"Duration (seconds)": "Duration"})

df_bubble = df[df["Sort Method"] == "Bubble"]
df_heap = df[df["Sort Method"] == "Heap"]

#Undo below comments to plot only 10, 1000 and 5000. Else, it will plot all dataset sizes
avg_duration_bubble = df_bubble.groupby("Dataset Size")["Duration"].mean()#.iloc[:3]
avg_duration_heap = df_heap.groupby("Dataset Size")["Duration"].mean()#.iloc[:3]

plt.figure(figsize=(10, 6))

plt.plot(avg_duration_bubble.index, avg_duration_bubble.values, color="blue", label="Bubble Sort", alpha=0.8)
plt.plot(avg_duration_heap.index, avg_duration_heap.values, color="red", label="Heap Sort", alpha=0.8)

plt.xlabel("Dataset Size", fontsize=12)
plt.ylabel("Sorting Duration (secs)", fontsize=12)
plt.title("Bubble Sort vs Heap Sort Performance", fontsize=14)

plt.xticks(avg_duration_bubble.index, rotation=25)

plt.legend()
plt.grid(True)

#Undo comment below to save plt
#plt.savefig("oliverpotts-bubble-sort-heap-sort-analysis.png")

plt.show()
