import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(right=subjects, how="cross")
    examinations["subject_count"] = examinations["subject_name"]
    examinations = examinations.groupby(["student_id", "subject_name"], as_index=False)["subject_count"].count()
    df = df.merge(right=examinations, left_on=["student_id", "subject_name"], right_on=["student_id", "subject_name"], how='left')
    return df.sort_values(["student_id", "subject_name"]).fillna(0).astype({'subject_count':'Int64'})


data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
Students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
Examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

print(students_and_examinations(Students, Subjects, Examinations))