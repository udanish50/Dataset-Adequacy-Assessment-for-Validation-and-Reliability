import pandas as pd
import numpy as np
from sklearn.decomposition import FactorAnalysis
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import squareform

# Load dataset
data_clean = pd.read_csv(".csv")  # Replace with your actual dataset file

# Define sub-sections based on the questionnaire structure
sub_sections_full = {
    "Instructional Program": ["ITEM 1", "ITEM 2", "ITEM 3", "ITEM 4", "ITEM 5", "ITEM 6"],
    "Involvement of Stakeholders": ["ITEM 7", "ITEM 8", "ITEM 9", "ITEM 10", "ITEM 11"],
    "Assessment": ["ITEM 12", "ITEM 13", "ITEM 14", "ITEM 15", "ITEM 16"],
    "Functioning Facilities": ["ITEM 17", "ITEM 18", "ITEM 19", "ITEM 20", "ITEM 21"],
    "Learning Environment": ["ITEM 22", "ITEM 23", "ITEM 24", "ITEM 25", "ITEM 26"],
    "Personal Development": ["ITEM 27", "ITEM 28", "ITEM 29", "ITEM 30", "ITEM 31"]
}

# Function to calculate Cronbach's Alpha
def calculate_cronbach_alpha(df):
    n_items = df.shape[1]
    item_variances = df.var(axis=0, ddof=1)
    total_variance = df.sum(axis=1).var(ddof=1)
    alpha = (n_items / (n_items - 1)) * (1 - (item_variances.sum() / total_variance))
    return alpha

# Perform EFA for all sub-sections
efa_results_full = {}
for section, items in sub_sections_full.items():
    fa = FactorAnalysis(n_components=1)  # Assuming 1 factor per sub-section for simplicity
    factors = fa.fit_transform(data_clean[items])
    loadings = np.abs(fa.components_)  # Use absolute values for easier interpretation
    efa_results_full[section] = {
        "loadings": loadings,
        "eigenvalue": np.var(factors, axis=0)[0],
        "cronbach_alpha": calculate_cronbach_alpha(data_clean[items])
    }

# Print EFA results
for section, results in efa_results_full.items():
    print(f"Section: {section}")
    print(f"Eigenvalue: {results['eigenvalue']:.3f}")
    print(f"Cronbach's Alpha: {results['cronbach_alpha']:.3f}")
    print("Factor Loadings:", results['loadings'])
    print("")

# Save results to a CSV file (optional)
efa_df = pd.DataFrame.from_dict(efa_results_full, orient='index')
efa_df.to_csv("efa_results.csv")
