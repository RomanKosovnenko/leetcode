import pandas as pd

# def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
#     return store[(store.amount > 500)]["customer_id"].to_frame().drop_duplicates().count().to_frame("rich_count")

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'rich_count': [store[(store.amount > 500)]["customer_id"].nunique()]})