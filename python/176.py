import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.sort_values(by="salary", ascending=False).drop_duplicates(subset=["salary"])[["salary"]]
    if employee.shape[0] > 1:
        return employee.iloc[1,2].rename(columns={"salary": "SecondHighestSalary"})
    else:
        return pd.DataFrame({"SecondHighestSalary": [None]})