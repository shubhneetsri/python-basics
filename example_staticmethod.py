import os
import pandas as pd

class A():
    base_path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, filename):
        """
        In a staticmethod, you don’t have access to the implicit cls or self arguments, 
        so you can’t directly reference class attributes using cls.attribute
        Following is useless for staticlasses
        """
        self.file_loc = os.path.join(A.base_path, filename)
    
    @staticmethod
    def readecsv(filename):
        file_loc = os.path.join(A.base_path, filename)
        
        if os.path.exists(file_loc):
            print(f"Reading file: {file_loc}")
            A.readfile(file_loc)
        else:
            print("File does not exist.")

    @staticmethod
    def readfile(file_loc):
        try:
            df = pd.read_csv(file_loc)  # read the Excel file
            print(df.head())              # print first 5 rows

            # ✅ Example operation: Filter rows where 'Salary' > 50000 (if that column exists)
            if 'Ticket Number' in df.columns:
                high_salary = df[df['Ticket Number'] > 2000]
                print("\nEmployees with Ticket Number > 2000:")
                print(high_salary)
        except Exception as e:
            print("Error reading Excel file:", e)

# Example usage
obj = A('open_tickets.csv')
obj.readecsv('open_tickets.csv')  # replace with your actual Excel filename
