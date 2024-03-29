import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby("class", as_index=False)["student"].count()
    print(df)
    return df[(df["student"]>=5)][["class"]]