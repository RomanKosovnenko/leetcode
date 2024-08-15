import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    condition = users["mail"].str.contains("^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com", regex=True)
    return users[condition]