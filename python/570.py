import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId", as_index=False)["id"].count().rename(columns={"id":"count"})
    df = employee.merge(right=df, how="inner", left_on="id", right_on="managerId")
    return df[df["count"]>=5][["name"]]

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

print(find_managers(Employee))