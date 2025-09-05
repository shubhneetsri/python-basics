# import pymysql
import time
import sys

class sorting_fn():

    def sort_list_desc(self, listvalues):
        for i in range(len(listvalues)):
            for j in range(len(listvalues) - 1):
                if listvalues[j] < listvalues[j+1]:
                    # listvalues[j], listvalues[j+1] = listvalues[j+1], listvalues[j]
                    temp = listvalues[j]
                    listvalues[j] = listvalues[j+1]
                    listvalues[j+1] = temp
        return listvalues



    def sort_list(self, list_ele):
        for i in range(len(list_ele)):
            for j in range(len(list_ele) - i - 1):
                if list_ele[j] > list_ele[j+1]:
                    temp = list_ele[j+1]
                    list_ele[j+1] = list_ele[j]
                    list_ele[j] = temp
        print(list_ele)

    def merge_sort_desc(self, unsort_list):
        if len(unsort_list) <= 1:
            return unsort_list
        
        mid = len(unsort_list) // 2

        Lsort = self.merge_sort_desc(unsort_list[:mid])
        Rsort = self.merge_sort_desc(unsort_list[mid:])

        i = j = 0
        sorted_list = []
        while i < len(Lsort) and j < len(Rsort):
            if(Lsort[i] > Rsort[j]):
                sorted_list.append(Lsort[i])
                i += 1
            else:
                sorted_list.append(Rsort[j])
                j += 1
            
        sorted_list.extend(Lsort[i:])
        sorted_list.extend(Rsort[j:])
        
        return sorted_list
                    


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

# To test
str_obj = sorting_fn()
print(str_obj.merge_sort_desc([2,1,6,5,4,89,5,0]))
