import pandas as pd

# def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
#     activities = activities.drop_duplicates().sort_values(["sell_date","product"]).reset_index()[["sell_date", "product"]]
#     df = activities.groupby("sell_date", as_index=False).aggregate({"product": ["count", lambda x: ','.join(x)]})
#     df.columns = ["sell_date", "num_sold", "products"]
#     return df

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups = activities.groupby('sell_date')

    stats = groups.agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()

    stats.sort_values('sell_date', inplace = True)

    return stats

# data = [['2020-05-30', 'Headphone'],
#         ['2020-06-01', 'Pencil'],
#         ['2020-06-02', 'Mask'],
#         ['2020-05-30', 'Basketball'],
#         ['2020-06-01', 'Bible'],
#         ['2020-06-02', 'Mask'],
#         ['2020-05-30', 'T-Shirt']]
data = [[ '2020-7-2'  , 'Slip'       ],
        [ '2020-6-22' , 'Slip'       ],
        [ '2020-7-17' , 'Handlotion' ],
        [ '2020-6-20' , 'Slip'       ],
        [ '2020-7-2'  , 'Hoodie'     ],
        [ '2020-6-9'  , 'Hoodie'     ],
        [ '2020-7-5'  , 'Handlotion' ],
        [ '2020-6-22' , 'Handlotion' ],
        [ '2020-6-14' , 'Slip'       ],
        [ '2020-6-28' , 'Hoodie'     ],
        [ '2020-6-12' , 'Hoodie'     ],
        [ '2020-6-5'  , 'Handlotion' ],
        [ '2020-6-1'  , 'Slip'       ],
        [ '2020-6-11' , 'Slip'       ],
        [ '2020-6-19' , 'Handlotion' ]
]
Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})

print(categorize_products(Activities))