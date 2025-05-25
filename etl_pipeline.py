import pandas as pd
import os

# Extract function is used to extract data from multiple sources
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df
    
# Call the extract() function and store it as the "merged_df" variable
grocery_sales = pd.read_csv("grocery_sales.csv")
merged_df = extract(grocery_sales, "extra_data.parquet")

#Create a transform method to clean, format and handle missing data
def transform(raw_data):
    raw_data.set_index("index", inplace=True)
    raw_data.dropna(subset=["Date", "Weekly_Sales"], inplace=True)
    raw_data_red = raw_data[["Store_ID", "Date", "Dept", "IsHoliday", "Weekly_Sales", "CPI", "Unemployment"]]
    raw_data_red["Date"] = pd.to_datetime(raw_data_red["Date"])
    raw_data_red["Month"] = raw_data_red["Date"].dt.month
    return raw_data_red

# Create the avg_weekly_sales_per_month function that takes in the cleaned data from the last step
def avg_weekly_sales_per_month(clean_data):
    agg_data = clean_data.groupby("Month")["Weekly_Sales"].mean().reset_index()
    return agg_data
  
#load function saves cleaned data and aggreagate data to seperate files
def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    try:
        full_data.to_csv(full_data_file_path, index=False)
        print(f"Cleaned data saved to {full_data_file_path}")
        agg_data.to_csv(agg_data_file_path, index=False)
        print(f"Aggregated date saved to {agg_data_file_path}")
    except Exception as e:
        print(f"An error occured while saving file: {e}")

# Validation() function with one parameter: file_path - to check whether the previous function was correctly executed
def validation(file_path):
    # Write your code here
    try:
        if not os.path.exists(file_path):
            print(f"File does not exists at : {file_path}")
            return False
        df = pd.read_csv(file_path)
        if(df.empty):
            print(f"File exists but contains no data at : {file_path}")
            return False
        print(f"Validation Successful : File exists and contains data at :         {file_path}")
        return True
    except Exceptions as e:
        print(f"An error occured during file validation")

clean_data= trasnform(merged_df)
avg_weekly_sales_per_month = avg_weekly_sales_per_month(clean_data)
load(clean_data, "grocery_sales_c", avg_weekly_sales_per_month, "avg_weekly_sales_per_month")
validation("grocery_sales.csv")
validation("avg_weekly_sales_per_month")
