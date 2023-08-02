import pandas as pd

# def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     return customers[~customers["id"].isin(orders["customerId"])]["name"].to_frame().rename(columns={"name": "Customers"})

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers.merge(orders, left_on="id", right_on="customerId", how="left").query("customerId.isnull()")["name"].to_frame().rename(columns={"name": "Customers"})