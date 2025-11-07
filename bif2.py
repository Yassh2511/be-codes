# 📌 RNA-Seq Differential Expression Analysis (Beginner Friendly)

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# -------------------------------
# 1) LOAD DATA
# -------------------------------

# If you have your file, use this:
# df = pd.read_csv("RNAseq_counts.csv").set_index("Gene")

# Sample toy dataset (genes × samples)
data = {
    "Gene": ["GeneA","GeneB","GeneC","GeneD","GeneE","GeneF"],
    "Control_1": [50, 10, 300, 5, 200, 22],
    "Control_2": [45, 15, 290, 4, 220, 18],
    "Treatment_1": [100, 5, 310, 3, 250, 40],
    "Treatment_2": [110, 8, 320, 2, 240, 35]
}

df = pd.DataFrame(data).set_index("Gene")

# -------------------------------
# 2) NORMALIZATION — CPM
# -------------------------------
# Counts Per Million: (gene_count / total_counts_per_sample) * 1e6

cpm = df.div(df.sum(axis=0), axis=1) * 1e6

control = cpm[["Control_1", "Control_2"]]
treatment = cpm[["Treatment_1", "Treatment_2"]]

# -------------------------------
# 3) STATISTICAL TEST + FOLD CHANGE
# -------------------------------

pvals = []
log2FC = []

for gene in cpm.index:
    p = ttest_ind(control.loc[gene], treatment.loc[gene]).pvalue
    pvals.append(p)
    
    fc = (treatment.loc[gene].mean() + 1) / (control.loc[gene].mean() + 1)
    log2FC.append(np.log2(fc))

df["p_value"] = pvals
df["log2FC"] = log2FC


df["Significant"] = (df["p_value"] < 0.05)

# -------------------------------
# 4) SHOW RESULTS
# -------------------------------

print("\n✅ Differential Gene Expression Results:\n")
print(df)

deg = df[df["Significant"] == True]
print("\n🔥 Significantly Differentially Expressed Genes (p < 0.05):\n")
print(deg)

# -------------------------------
# 5) VOLCANO PLOT
# -------------------------------

plt.figure(figsize=(7,5))
plt.scatter(df["log2FC"], -np.log10(df["p_value"]))
plt.axvline(x=1, linestyle="--")     # Up
plt.axvline(x=-1, linestyle="--")    # Down
plt.axhline(y=-np.log10(0.05), linestyle="--")
plt.title("Volcano Plot — RNA-Seq DEG Analysis")
plt.xlabel("Log2 Fold Change")
plt.ylabel("-Log10(p-value)")
plt.show()
