import os
import sys
import pandas as pd

# sys.path.append(
#     os.path.abspath(
#         os.path.join(os.path.dirname(__file__),'..')
#     )
# )

data = {
    'companies': ['TCS', 'MPHASIS', 'LTI', 'HCL', 'GlobalLogic', 'MagicEdTech'],
    'joining_date': ['2012-03-01', '2025-07-12', '2025-01-04', '2025-06-09', '2024-08-09', '2023-09-10'],
    'relieving_date': ['2025-08-12','2025-08-12','2025-08-12','2025-08-12','2025-08-12','2025-08-12'],
    'candidate_count': [10,22,33,1,45,7]
}

sheet = pd.DataFrame(data)
sheet['joining_date'] = pd.to_datetime(sheet['joining_date'])
sheet['relieving_date'] = pd.to_datetime(sheet['relieving_date'])
sheet['day_worked'] = (sheet['joining_date'] - sheet['relieving_date']).dt.days

print(sheet.describe())
# print(sheet.groupby('relieving_date')['day_worked'].transform('mean'))
