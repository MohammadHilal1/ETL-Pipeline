# Grocery Sales ETL Pipeline

This repository contains a simple ETL (Extract, Transform, Load) pipeline for processing grocery sales data using **Python** and **Pandas**.

## 📊 Overview

The ETL process performs the following steps:

- **Extract** data from a CSV and a Parquet file.
- **Transform** the data by cleaning, formatting, and engineering features.
- **Load** both the cleaned data and aggregated metrics into separate CSV files.
- **Validate** output files to ensure correctness.

---

## 🛠️ Project Structure

```plaintext
.
├── grocery_sales.csv          # Raw sales data (CSV)
├── extra_data.parquet         # Supplemental data (Parquet)
├── etl_pipeline.py            # Python script with the ETL logic
├── grocery_sales_c.csv        # Cleaned data output (Generated)
├── agg_data.csv               # Aggregated data output (Generated)
└── README.md                  # This file
