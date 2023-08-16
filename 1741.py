import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    print(employees)
    return employees.groupby(["event_day", "emp_id"])["total_time"].sum().reset_index().rename(columns={"event_day":"day"}, inplace=True)