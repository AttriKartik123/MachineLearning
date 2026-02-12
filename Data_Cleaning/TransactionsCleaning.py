import pandas as pd
df = pd.read_csv("Data_Cleaning/Transactions.csv")


#removing duplicates
df = df.drop_duplicates(subset=['transaction_id'],keep='first')

# 3. HANDLING MISSING VALUES (Nulls)
# Your data has a few missing 'currency_type' and 'deposited_date' entries.
# We fill missing currency with 'Unknown' and drop rows with missing dates (as they are unusable).

df["currency_type"] = df["currency_type"].fillna('Unknown')