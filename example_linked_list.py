"""
Example of linked list
"""
import sys

class MyNode():
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def add_node(self, value):
        current = self

        """
        Code for Keep pointer move to end
        This checks if next node is there then move forward
        """
        while current.next:
            current = current.next
        
        """
        Now add the new node at the end
        """
        current.next = MyNode(value)

base = MyNode('a')
base.add_node('b')
base.add_node('c')

current = base
while current:
    print(current.data)
    current = current.next






























# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None

#     def create_links(self, data_list):
#         for data in data_list:
#             self.append_links(data)
    
#     def append_links(self, data):
#         current = self
#         while current.next:
#             current = current.next
#         current.next = Node(data)

#     def insert_at(self, index, data):
#         new_node = Node(data)
#         current_node = self
#         position = 0

#         if index == 0:
#             new_node.next = self
#             return new_node
        
#         while position < index:
#             current_node = current_node.next
#             position += 1
        
#         new_node.next = current_node.next
#         current_node.next = new_node

            
            

# node_obj = Node(input('Enter the First value of node: '))
# node_obj.create_links([1,2,3,4])
# node_obj.insert_at(0, 'C')
# # while True:
# #     user_input = input('Enter next value of node: ')
# #     if user_input.lower() == 'exit':
# #         break
# #     node_obj.append_links(user_input)

# # node_obj = node_obj.insert_at(0, 'C')
# # node_obj = node_obj.insert_at(1, 'C')

# current = node_obj
# while current:
#     print(current.data)
#     current = current.next