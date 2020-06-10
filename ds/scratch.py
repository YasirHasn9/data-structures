'''
what is the big O notation ?
it is a way for developers to describe how long an algorithm takes to run. 
because devs
needs a way to compare efficiencies solutions  for different problems
like
1. how quickely the runtime grows
2. the size of data
3.relative to the input

-----------------linked list
we dont have to store our data[box] in serialized order
but where ever we found a memory space each piece of data made of like an array
one index hold the actual value and the other points to the next 
piece of data

prepends for dynamic arr is O(n)
prepends for linked list O(1)

these appends and prepends are so fast because the nodes of the linked list
are free to go anywhere in the memory as long as there is an available space 
and it is not have to be one next other

@why we store data in array rather than linked list?
because array has O(1)-time lookups


in BigO we dont need the measure the actual time for an algorithm like saying this function
takes 30s to finish but this is wrong because every machine is taking different time to
finish a task depeneding on the HW the space of RAM


O(1)
it means it does not matter how big is our data or input is the operations
 would stay the same


'''
# O(1) the num of operation stays the same no matter how large is the data
# def get_item(items):
#     # this would return the first el in the array
#     # of items no matter how big is the array
#     return items[0]

'''
linear time
it means the operation that been implemting depends on the size of our data
O(n)
n = the size of the input data
'''
# def get_items(items):
#     # it does matter the size of the array of the items
#     # because the operation would change accordingly
#     for item in items:
#         print(item)

'''
Quadratic time
O(n^2)
the operation would run depends on the size of the data multiple by the size of itself
'''
# def get_all_passible_pairs(items):
#     for item in items:
#         for sub_item in items:
#             print(item , sub_item)

'''
linked list usually have a head a tail
the head tells where is the start => first item
and tail is where it ends => last item

list linked have O(1) for append and prepand and O(n) for lookups
Dynamic Array have O(n) for append and prepand and O(1) for lookups
'''
'''
to make a node when need the value and the next_node(next postions)
# '''

'''
stack tracks the functions call in the program and the execution context in the functions

Link list is data structure for storing a collection of items
it like many boxes that connect to each other and each box has head and tail
the head contains the data that each box contain [head.data ]
and also a next that references to the next box [head.next]

and head.next.data => the data of the next box => the head of the box

linked list are often implementing stack LIFO
Last in first out 

def outer():
    return middel()

def middle():
    return inner()

def inner():
    return something

when we invoke the outer , the engine will push it to stack to be in 
frame element of the stack . the stack will take a look at the context of 
outer function okey it return another fun (middle) okey push to the stack 
now we have 2 function are waiting of the execution context again take a look 
at  the content of the middle function and also it returns the inner() function 
push the inner() to the top of the stack check its content and then call it

the stack would be like this 
                             inner() last in first out popped off --> 1
                             middle()               popped off --> 2
                  stack =>   outer () first in last out  popped off --> 3


    '''
