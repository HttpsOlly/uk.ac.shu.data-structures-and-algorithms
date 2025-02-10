import pandas as pd
import matplotlib.pyplot as plt

file_path = "benchmark-20250112T185129.csv"

df = pd.read_csv(file_path)

df_linear = df[df["method"] == "linear"]
df_binary = df[df["method"] == "binary"]

plt.figure(figsize=(10, 6))

plt.plot(df_linear["stalls"], df_linear["duration"], color="blue", label="Linear", alpha=0.8)
plt.plot(df_binary["stalls"], df_binary["duration"], color="red", label="Binary", alpha=0.8)

plt.xlabel("Number of Stalls", fontsize=12)
plt.ylabel("Duration in Seconds to Allocate Cows to Stalls", fontsize=12)
plt.title("Linear vs Binary Search: Analysing Operations and Input Data Size", fontsize=14)

plt.legend()

plt.savefig("oliverpotts-linear-vs-binary-search.png")

plt.show()
