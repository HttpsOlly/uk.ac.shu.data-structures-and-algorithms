import pandas as pd
import matplotlib.pyplot as plt

# Only loads one restart - I chose restart number 11

file_path = "results.csv"
df = pd.read_csv(file_path)

restart_num = 11

#Uncomment any of the three below to generate different graphs based on iterations on Restart 5
# df_filtered = df[(df["Restart"] == restart_num) & (df["Iteration"] <= 15)].drop(columns=['Solution'])
# df_filtered = df[(df["Restart"] == restart_num) & (df["Iteration"] <= 1000)].drop(columns=['Solution'])
df_filtered = df[(df["Restart"] == restart_num) & (df["Iteration"] <= 4000)].drop(columns=['Solution'])

df_iterations = df_filtered["Iteration"]
df_fitness = df_filtered["Fitness"]


plt.figure(figsize=(6, 4))
plt.plot(df_iterations, df_fitness, marker="d", markersize=0.5, linestyle="-", linewidth=2, color="crimson", alpha=0.8)
plt.xlabel("Iterations", fontsize=10)
plt.ylabel("Fitness", fontsize=10)
plt.title("Fitness Score Advancing Through Iterations \n Restart 11", fontsize=12)
plt.xlim(min(df_iterations), max(df_iterations))

plt.grid(True)

#Undo comment below to save plt - used for Word document
# plt.savefig("fig1.png")

plt.show()
