import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher[["teacher_id", "subject_id"]].rename(columns={"subject_id":"count"}).drop_duplicates().groupby("teacher_id", as_index=False)["subject_id"].count()