import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values("score", ascending=False)
    scores["rank"] = scores["score"].rank(ascending=False, method="dense")
    return scores[["score", "rank"]]