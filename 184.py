import pandas as pd

# def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
#     maxdf = employee[["salary", "departmentId"]].groupby(["departmentId"]).max().reset_index()
#     employee = employee.merge(maxdf, how="inner",  left_on=["departmentId", "salary"], right_on=["departmentId", "salary"])
#     df = employee.merge(department.rename(columns={"name":"Department"}), how="left",  left_on="departmentId", right_on="id")
#     print(df)
#     return df.rename(columns={"salary": "Salary", "name": "Employee"})[["Department", "Employee", "Salary"]]


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, how = 'inner', left_on = 'departmentId', right_on = 'id')
    max_sal = df.groupby('departmentId')['salary'].transform('max')
    new_df = df[df['salary'] == max_sal]
    new_df = new_df.rename(columns = {'name_y':'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    return new_df[['Department','Employee','Salary']]