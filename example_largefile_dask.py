import dask.dataframe as dd

# Read CSV lazily
df = dd.read_csv('files/*.csv', blocksize='64MB')  
# blocksize splits the file into manageable chunks (~64MB each)

# Iterate over partitions (each partition is a pandas DataFrame)
for i, partition in enumerate(df.partitions):
    pdf = partition.compute()  # convert Dask partition to pandas DataFrame
    for index, row in pdf.iterrows():
        print(row.to_dict())  # prints row as a dictionary