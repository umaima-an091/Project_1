import pandas as pd

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
file_path = "Dataset for Data Analytics.xlsx"
data1 = pd.read_excel(file_path)

# --------------------------------------------------
# 1. Check Missing Values
# --------------------------------------------------
print("\nMissing Values in Each Column:")
print(data1.isnull().sum())

# --------------------------------------------------
# 2. Remove Duplicate Records
# --------------------------------------------------
duplicate_count = data1.duplicated().sum()
print(f"\nNumber of Duplicate Rows: {duplicate_count}")

data1 = data1.drop_duplicates()

# --------------------------------------------------
# 3. Handle Missing Values
# --------------------------------------------------
if "CouponCode" in data1.columns:
    data1["CouponCode"] = data1["CouponCode"].fillna("No Coupon")

# --------------------------------------------------
# 4. Clean Text Columns
#    Remove Leading and Trailing Spaces
# --------------------------------------------------
text_columns = data1.select_dtypes(include=["object","string"]).columns

for column in text_columns:
    data1[column] = data1[column].str.strip()

# --------------------------------------------------
# 5. Correct Data Formats
# --------------------------------------------------
if "Date" in data1.columns:
    data1["Date"] = pd.to_datetime(data1["Date"], errors="coerce")

numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

for column in numeric_columns:
    if column in data1.columns:
        data1[column] = pd.to_numeric(data1[column], errors="coerce")

# --------------------------------------------------
# 6. Save Cleaned Dataset
# --------------------------------------------------
output_file = "Cleaned_Dataset.xlsx"
data1.to_excel(output_file, index=False)

# --------------------------------------------------
# Summary Report
# --------------------------------------------------
print("\nData Cleaning Completed Successfully!")
print(f"Cleaned dataset saved as: {output_file}")
print(f"Final Dataset Shape: {data1.shape}")