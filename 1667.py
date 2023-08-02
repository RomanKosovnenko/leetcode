import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["Name"] = users["Name"].str.capitalize()
    return users.sort_values(by="user_id")