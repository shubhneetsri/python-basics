import pymysql
import time
import sys

class string_fn():

    def latters_count(self, name): 
        list_values = [char for char in name if char != ' ']
        list_values = sorted(list_values)
        counter_list = {}

        for value in list_values:
            counter_list[value] = counter_list.get(value, 0) + 1

        return self.get_count(counter_list)

    def process_it(self, item):
        return f"{item[0]} has {item[1]} occurences"

    def get_count(self, counter_list):
        res = map(self.process_it, counter_list.items())
        return list(res)

# To test
str_obj = string_fn()
str_obj.latters_count('shubhneet')
