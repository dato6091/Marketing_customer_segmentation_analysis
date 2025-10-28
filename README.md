# Customer Segmentation with Python

This project performs a **customer segmentation analysis** using clustering algorithms to uncover patterns in user behavior and group similar customers based on their characteristics.  
The analysis includes **exploratory data analysis (EDA)**, **feature engineering**, and **modeling** using both **Hierarchical** and **K-Means Clustering**, followed by **cluster profiling and interpretation**.

---

## 🎯 Project Goal

The main objective of this project is to identify distinct customer groups to help the business understand:
- Which customers share similar behavioral and demographic profiles.
- How each segment differs in terms of engagement, spending, or product preferences.
- How to tailor marketing strategies and offerings for each customer group.

By the end of the analysis, meaningful segments were obtained that can guide **targeted marketing**, **personalized recommendations**, and **strategic decision-making**.

---

## 📂 Repository Structure

The repository is organized into modular components that guide you from exploration to modeling:

- 1_EDA.ipynb — Performs initial exploration, descriptive analysis, and visualization to uncover relationships between variables.
- 2_Model_Implementation_and_Interpretation.ipynb — Implements and interprets clustering models (Hierarchical & K-Means) to identify meaningful customer segments.
- customer_segmentation_data.csv - Raw input file.
- customer_segmentation_data_clean.csv - Input file after some preprocessing.
- Segmentation data legend.xlsx — Provides feature definitions, measurement units, and metadata.
- requirements.txt — Lists all dependencies exported from Poetry for reproducible environments.
- README.md — Documentation describing the project’s purpose, methodology, and results.

---

## 🧠 Methodology Overview

1. **Exploratory Data Analysis (EDA)**
   - Checked for missing values and outliers.
   - Examined feature distributions and relationships through univariate and multivariate analysis.
   - Identified key drivers of customer differentiation.

2. **Feature Engineering**
   - Applied transformations to normalize skewed variables.
   - Created new derived features that capture behavioral patterns.

3. **Data Standardization**
   - Scaled features to ensure equal weight in clustering algorithms.

4. **Clustering Implementation**
   - Applied **Hierarchical Clustering** to explore natural groupings and determine an optimal cluster range.
   - Used **K-Means Clustering** for final segmentation, with cluster number selection based on **Elbow Method** and **Silhouette Analysis**.

5. **Model Evaluation & Interpretation**
   - Validated cluster compactness and separation.
   - Profiled clusters by comparing means across key metrics and visualizing their characteristics.

---

## 📊 Results Summary

- **Optimal number of clusters:** 5  
- **Silhouette score:** indicated good separation and internal cohesion.  
- **Cluster profiling revealed:**
  - High-value customers with strong engagement and high lifetime value.
  - Moderate-value customers with potential for upselling.
  - Price-sensitive and low-engagement groups requiring retention strategies.
  - Niche segments showing unique behavior patterns useful for tailored campaigns.

Each cluster was characterized by demographic, behavioral, and transactional variables, enabling actionable insights for **marketing personalization** and **business growth strategies**.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`  
- **Visualization:** heatmaps, pairplots, boxplots, and cluster distribution charts  
- **Clustering Algorithms:** Hierarchical and K-Means

