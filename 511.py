import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.sort_values("event_date").groupby("player_id",as_index=False)["event_date"].first().to_frame()