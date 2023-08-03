import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:


    low = accounts.loc[accounts["income"] < 20000].shape[0]
    high = accounts.loc[accounts["income"] > 50000].shape[0]
    avarage = accounts.shape[0]-low-high
    data = {
        "category": ["High Salary", "Average Salary", "Low Salary"],
        "accounts_count": [high, avarage, low]
    }

    return pd.DataFrame(data)