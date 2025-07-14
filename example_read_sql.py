import pymysql
import time
import sys

class db_fn():

    def process_db(self, query):
        connection = pymysql.connect(
            host='10.11.1.136',
            port=3306,
            user='faheem',
            password='Magic@1234@',
            database='magicats',
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            start_time = time.time()
            
            cursor.execute(query)
            results = cursor.fetchall()
            end_time = time.time()

            execution_time = end_time - start_time
            print(f"Query executed in {execution_time:.4f} seconds")
            print(f"Rows fetched: {len(results)}\n")
            return f"Executing query:\n{query}\n"+f"Query executed in {execution_time:.4f} seconds"

    def read_file(self):
        count = 0
        current_query = ""
        seen_queries = set()
        in_select = False

        with open(r'D:\py\python-basics\slow queries.sql', 'r') as file, open(r'D:\helpdesk\query.txt', 'w') as outfile:
            for line in file:
                if 'Query_time' in line:
                    # outfile.write(line.strip() + '\n')
                    print(line.strip())

                stripped_line = line.strip()
                if stripped_line.upper().startswith("SELECT"):
                    in_select = True

                if in_select:
                    current_query += stripped_line + " "

                if in_select and ";" in stripped_line:
                    # Execute the complete query
                    clean_query = current_query.strip()
                    if clean_query not in seen_queries:
                        seen_queries.add(clean_query)
                        res = self.process_db(clean_query)
                        count += 1

                        # outfile.write('\n' + res + '\n')
                    current_query = ""
                    in_select = False

            # outfile.write(str(count) + '\n')


# To test
str_obj = db_fn()
str_obj.read_file()
