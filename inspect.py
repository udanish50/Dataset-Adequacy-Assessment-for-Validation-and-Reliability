import pandas as pd
from scipy.stats import bartlett
import numpy as np

# Step 1: Load the dataset
file_path = '/mnt/data/data.csv'
data = pd.read_csv(file_path)

# Step 2: Inspect and clean the data
# Remove leading and trailing spaces from column names
data.columns = data.columns.str.strip()

# Convert 'ITEM 31' column to numeric, handling errors by converting to NaN
data['ITEM 31'] = pd.to_numeric(data['ITEM 31'], errors='coerce')

# Drop rows with missing values
data_clean = data.dropna()

# Step 3: Perform Bartlett's test of sphericity
chi_square_value, p_value = bartlett(*[data_clean[col] for col in data_clean.columns])

# Display Bartlett's test results
print(f"Bartlett's test chi-square value: {chi_square_value}")
print(f"Bartlett's test p-value: {p_value}")

# Step 4: Calculate the KMO measure
def calculate_kmo(dataset):
    corr_matrix = np.corrcoef(dataset, rowvar=False)
    inv_corr_matrix = np.linalg.inv(corr_matrix)
    partial_corr_matrix = -inv_corr_matrix / np.sqrt(np.outer(np.diag(inv_corr_matrix), np.diag(inv_corr_matrix)))
    
    np.fill_diagonal(partial_corr_matrix, 0)
    kmo_num = np.sum(np.square(corr_matrix)) - np.sum(np.square(np.diag(corr_matrix)))
    kmo_denom = kmo_num + (np.sum(np.square(partial_corr_matrix)) - np.sum(np.square(np.diag(partial_corr_matrix))))
    
    kmo = kmo_num / kmo_denom
    return kmo

# Calculate KMO for the cleaned dataset
kmo_value = calculate_kmo(data_clean)

# Display KMO results
print(f"KMO value: {kmo_value}")
