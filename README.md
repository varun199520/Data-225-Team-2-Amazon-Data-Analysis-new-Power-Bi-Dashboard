# Cloud Analytics and Data Warehouse Project Report

## Abstract
This group project focuses on implementing Cloud Analytics and Data Warehouse using the Amazon Products Dataset from Kaggle (historic data) and real-time APIs from RapidApi. The objective is to analyze customer behaviors, product trends, and market dynamics through a dashboard. Cloud-based databases such as MySQL, Redshift, and MongoDB are utilized along with ETL/ELT processes implemented in Python for seamless data extraction, transformation, and loading. The project also constructs a Data Warehouse using cloud solutions like Snowflake, BigQuery, and RedShift, ensuring compatibility with ETL/ELT tools.

## Dataset Links
1. **Real Time API**: [RapidApi - Real Time Amazon Data](https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data/)
2. **Historical Dataset**: [Amazon Products Dataset on Kaggle](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset2023-1-4m-products)

## Database Schema
The database schema includes three tables: amazon_fact_table, category_dimension table, and product_dimension table. These tables follow the star schema, ensuring efficient analytics by organizing data into fact and dimension tables.

## Cloud Architecture
The architecture utilizes Amazon Web Services (AWS) for collecting, storing, transforming, and analyzing both real-time and historical data related to Amazon categories and products. AWS services such as S3, Redshift, Glue, and RDS are integrated into a cohesive pipeline, ensuring scalability, security, and efficiency in handling data.

## ETL Process
- **Historic ETL**: Python scripts are used for data cleaning, transformation, and loading of historical data into MySQL and RDS.
- **Live Data ETL**: Real-time data is fetched from Rapid API, stored in S3, transformed using Glue, and loaded into Redshift for analysis.
- **Apache Airflow**: DAGs are created to schedule tasks for data gathering and ETL processes.

## Data Warehouse Schema
A Star Schema is implemented for the data warehouse, facilitating optimized querying of large datasets by organizing data into fact and dimension tables.

## Business Intelligence
Tableau is used for data visualization and analysis, providing insights into Amazon categories and products based on archived and real-time datasets.

### Power BI Dashboard
- View the interactive dashboard here: [Power BI Report](https://app.powerbi.com/view?r=eyJrIjoiMjg0ZTc3MTYtNmNkZi00Mjk5LTg0YjMtOGY5MzMzZjA5YTc0IiwidCI6Ijk4NGJiNWVmLTEyMmItNDU0NC05NzVkLTRhOWFjYTVhNGNjOCIsImMiOjZ9)

## Analysis and Recommendation
- Machine learning algorithms such as Decision Tree and Logistic Regression are utilized for sales forecasting and bestseller prediction.
- Statistical analysis and correlation insights are derived for product strategy and marketing recommendations.

## Conclusion
The project demonstrates the capabilities of Cloud Analytics and Data Warehouse in providing data-driven insights for understanding customer behaviors, product trends, and market dynamics in the e-commerce domain.

## References
- [Kaggle Amazon Products Dataset](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products/data)
- [Data-Driven Decision Making in E-commerce](https://www.easternenterprise.com/wp-content/uploads/2023/05/Data-Driven-Decision-Making-in-Ecommerce-Leveraging-Analytics-for-Growth.pdf)
- [Harvard Business School Online: Data-Driven Decision Making](https://online.hbs.edu/blog/post/data-driven-decision-making)
# Data-225-Team-2-Amazon-Data-Analysis
