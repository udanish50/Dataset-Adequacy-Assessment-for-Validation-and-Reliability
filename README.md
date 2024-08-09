# Dataset Adequacy Assessment for Validation and Reliability

This repository contains a Python script to assess the adequacy of a dataset for factor analysis using two key statistical tests: Bartlett's Test of Sphericity and the Kaiser-Meyer-Olkin (KMO) Measure.

## Overview
Factor analysis is a powerful statistical method used to identify underlying relationships between variables. However, it's essential to confirm that your dataset is suitable for factor analysis before proceeding. This script performs the necessary checks using:
- **Bartlett's Test of Sphericity**: This test checks whether the correlation matrix of the dataset is an identity matrix, which would indicate that the variables are unrelated and unsuitable for factor analysis.
- **Kaiser-Meyer-Olkin (KMO) Measure**: The KMO statistic quantifies the proportion of variance among variables that might be common variance, thus assessing the sampling adequacy for factor analysis.

## Steps Performed
1. **Loading the Dataset**: The script reads the dataset from a CSV file.
2. **Data Cleaning**: Column names are stripped of leading/trailing spaces, and non-numeric columns are converted to numeric where possible. Rows with missing values are removed.
3. **Bartlett's Test**: The script performs Bartlett's test to check if the correlation matrix is significantly different from an identity matrix.
4. **KMO Measure**: The KMO statistic is calculated to assess whether the dataset is appropriate for factor analysis.

## Usage
- Ensure your dataset is in CSV format and adjust the file path in the script accordingly.
- Run the script to obtain the Bartlett's chi-square value, p-value, and the KMO measure.
- Interpret the results:
  - **Bartlett's Test**: A significant p-value (< 0.05) suggests that the dataset is adequate for factor analysis.
  - **KMO Measure**: Values closer to 1.0 indicate that the dataset is well-suited for factor analysis. Values between 0.7 and 0.8 are considered middling, while values below 0.6 suggest unsuitability.

## Requirements
- Python 3.x
- Pandas
- Scipy

## Example Output
The script will output the following:
- Bartlett's test chi-square value
- Bartlett's test p-value
- KMO value

## Conclusion
This script provides a straightforward way to assess whether your dataset is appropriate for factor analysis, ensuring that subsequent analysis is built on a solid foundation.
"""
