#There are diff. list methods that you can use

'''List Methods'''
list = [2, 1, 3]
list.append(4) #adds one element at the end  [2, 1, 3, 4]

list.insert(idx,el) #insert element at your choice index   

list.sort( ) #sorts in ascending order  [1,2,3] 

list.reverse( ) #reverses list  [3,1,2]
 
list.sort( reverse=True ) #sorts in descending order [3,2,1]

'''list methods'''
list = [2, 1, 3, 1]
list.remove(1) #removes first occurrence of element

list.pop( idx ) #removes element at idx  [2, 3, 1]



'''List slicing'''

marks = [23,45,67,54,67,97,45,98]
print(marks[1:6])

'''Code for list for change value( proceed)''' 
student = ["ishan" , 56 , "delhi"]
student[0] = "arjun"
print(student) 


