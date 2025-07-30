# import pandas as pd

# df = pd.read_csv('open_tickets.csv')

# print(df[df['Ticket Number']>25564])

def generator_read():
    with open('open_tickets.csv') as file:
        for line in file:
            yield line.strip()

for line in generator_read():
    print(line)