import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Vehicle' : [np.random.choice(['Car', 'Bike']) for _ in range(14)],
    'Miles' : [np.random.choice(['Greater Than 5000', 'Less Than 5000']) for _ in range(14)],
    'Price' : [np.random.choice(['Greater Than 100000', 'Less Than 100000']) for _ in range(14)],
    'Insured' : [np.random.choice(['Yes', 'No']) for _ in range(14)],
})

print(df)
print()

total_yes = len(df[df['Insured'] == 'Yes'])
total_no = len(df[df['Insured'] == 'No'])

print(f'P(Insured = Yes) = {total_yes}/14 = {total_yes/14}')
print(f'P(Insured = No) = {total_no}/14 = {total_no/14}')

data = {df.columns[0] : 0}
for column in df.columns[:-1]:
    data[column] = pd.crosstab(df[column], df['Insured'])
    print(pd.crosstab(df[column], df['Insured']))
    print()

print(data['Vehicle'])
print()
print(data['Miles'])
print()
print(data['Price'])
print()

query = [np.random.choice(df[column]) for column in df.columns[:-1]]
print(f'Vehicle : {query[0]}\nMiles : {query[1]}\nPrice : {query[2]}')
print()

mult = 1
for i in [data[df.columns[i]]['Yes'][query[i]]/total_yes for i in range(3)]:
    mult *= i
print(f'P(Yes) P({query[0]}|Yes) P({query[1]}|Yes) P({query[2]}|Yes) = {np.round(mult, 3)}')

mult = 1
for i in [data[df.columns[i]]['No'][query[i]]/total_no for i in range(3)]:
    mult *= i
print(f'P(No) P({query[0]}|No) P({query[1]}|No) P({query[2]}|No) = {np.round(mult, 3)}')