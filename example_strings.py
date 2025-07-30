# import pymysql
import time
import sys

class string_fn():

    def is_pelindrome(self, value):
        return value == value[::-1]

    def check_pelindrome(self, value):
        reverse_string = ''
        for i in range(len(value) - 1, -1, -1):
            reverse_string += value[i] 
        return reverse_string == value

    def get_str_occurence(self, str_val):

        new_dict = {}
        for char in str_val:
            if char in new_dict:
                new_dict[char] += 1
            else:
                new_dict[char] = 1
        # for index, char in enumerate(str_val):
        #     if new_dict.get(char) is not None:
        #         new_dict[char] += 1
        #     else:
        #         new_dict[char] = 1
        print(new_dict)



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
str_input = input('Enter String: ')
print(str_obj.check_pelindrome(str_input))
# str_obj.latters_count('shubhneet')
# res = str_obj.get_str_occurence([2,1,6,5,4,89,5,0])
# print(str_obj.sort_list_desc([2,1,6,5,4,89,5,0]))
