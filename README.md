# Customer Segmentation Using Machine Learning

## Project Overview
This project uses K-Means clustering to segment mall customers based on their annual income and spending score.

## Objectives
- Explore customer data using Pandas and visualization libraries.
- Identify customer groups using unsupervised machine learning.
- Visualize customer segments.
- Build an interactive Streamlit dashboard.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- K-Means Clustering
- Streamlit

## Dataset
The Mall Customers dataset contains 200 customer records with information about gender, age, annual income, and spending score.

## Customer Segments
The model identifies five clusters:
- Cluster 0: Average income and spending
- Cluster 1: High income and high spending
- Cluster 2: Low income and high spending
- Cluster 3: High income and low spending
- Cluster 4: Low income and low spending

## Run the Project
1. Install dependencies using `pip install -r requirements.txt`.
2. Ensure `customer_segments.csv` and `kmeans_model.pkl` are in the project folder.
3. Run `python -m streamlit run app.py`.

## Author
Javed Ali
