import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby("customer_number", as_index=False)["order_number"].count().sort_values("order_number", ascending=False).reset_index()
    return df[["customer_number"]].head(1)