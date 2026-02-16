import pandas as pd
df = pd.read_csv("Data_Cleaning/Transactions.csv")


#removing duplicates
df = df.drop_duplicates(subset=['transaction_id'],keep='first')

# HANDLING MISSING VALUES (Nulls)
# Your data has a few missing 'currency_type' and 'deposited_date' entries.
# We fill missing currency with 'Unknown' and drop rows with missing dates (as they are unusable).

df["currency_type"] = df["currency_type"].fillna('Unknown')

#"Only delete the row if the missing value is found in the deposited_date or deposited_time columns. If it's missing somewhere else, leave it alone for now."
df = df.dropna(subset=['deposited_date', 'deposited_time'])

#  DATE FORMATTING
# Converting the date column to a standard YYYY-MM-DD format.
df['deposited_date'] = pd.to_datetime(df['deposited_date'], dayfirst=True).dt.date


# Removes leading/trailing whitespace and converts text to lowercase for uniform categories
df['currency_type'] = df['currency_type'].str.strip().str.lower()


# EXTRA STEP: VALUE VALIDATION (Sanity Check)
# In financial data, a transaction of 0 or negative might be an error.
# We filter out any non-positive values.
df = df[df['usd_value']>0]


#Final polish 
#resetting the index 
df = df.reset_index(drop=True)
df.to_csv("Transactions_Cleaned.csv", index=False)

print("--- Transactions Cleaning Complete ---")

print(df.head())