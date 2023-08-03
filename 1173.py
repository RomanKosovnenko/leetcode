import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = delivery[delivery.order_date == delivery.customer_pref_delivery_date]
    return pd.DataFrame({"immediate_percentage": [round(immediate.shape[0]*100/delivery.shape[0],2)]})