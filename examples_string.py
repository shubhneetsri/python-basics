import pymysql
import time
import sys

class string_fn():

    def sort_list(self, list_ele):
        for i in range(len(list_ele)):
            for j in range(len(list_ele) - i - 1):
                if list_ele[j] > list_ele[j+1]:
                    temp = list_ele[j+1]
                    list_ele[j+1] = list_ele[j]
                    list_ele[j] = temp
        print(list_ele)

    def merge_sort(self, unsort_list):
        if len(unsort_list) <= 1:
            return unsort_list

        mid = len(unsort_list) // 2

        Lunsort_list = self.merge_sort(unsort_list[:mid])
        Runsort_list = self.merge_sort(unsort_list[mid:])
        
        i = j = 0
        sorted_list = []
        while i < len(Lunsort_list) and j < len(Runsort_list):
            if Lunsort_list[i] < Runsort_list[j]:
                sorted_list.append(Lunsort_list[i])
                i += 1
            else:
                sorted_list.append(Runsort_list[j])
                j += 1

        sorted_list.extend(Lunsort_list[i:])
        sorted_list.extend(Runsort_list[j:])
            
        return sorted_list

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
str_obj.latters_count('shubhneet')
res = str_obj.get_str_occurence([2,1,6,5,4,89,5,0])
print(res)
