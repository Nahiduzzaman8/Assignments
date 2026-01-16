#1. List: Create a list of numbers from 1 to 10 and print only the even numbers.
nums = [1,2,3,4,5,6,7,8,9,10]
for a in nums:
  if a%2==0:
    print(a)

#2. Tuple: Given t = (3, 5, 7, 3), count how many times 3 appears.
t = (3, 5, 7, 3)
print(t.count(3))

#3. Set: Find the common elements between {1,2,3,4} and {3,4,5,6}.
common_elements = {1,2,3,4} & {3,4,5,6}
print(common_elements)

#4. For Loop: Print all numbers from 1 to 20 that are divisible by 3.
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,9,20]
for a in nums:
  if a%3 == 0:
    print(a)

#5. Dictionary: Create a dictionary of 3 students with their marks, then print the student with the highest mark.
students = {
    's1':55, 
    's2':80, 
    's3':32
}
min_val = min(students.values())
print(min_val)

#7. List & Function: Write a function that takes a list and returns a new list with all elements doubled.
def dbl_els(lis):
    lis2 = []
    for a in lis:
        lis2.append(a*2)
    return lis2
    
a = [1,2,3,4,5]
res = dbl_els(a)
print(res)

# 8. Dictionary & Loop: Given {'a': 1, 'b': 2, 'c': 3}, write a loop to print keys with even values.
dic = {'a': 1, 'b': 2, 'c': 3}
for k, v in dic.items():
  if v%2==0:
    print('keys :',k, 'values :', v )

#9. Set & Function: Write a function that takes a list and returns a set of unique elements.
a = [1,2,2,3,4,5]
def makeset(a):
    return set(a)

print(makeset(a))

#10. Combined Challenge: Given a list of dictionaries like [{'name':'Ali','age':20},{'name':'Sara','age':25}], write code to print names of people older than 21.
peoples = [{'name': 'Ali', 'age': 20}, {'name': 'Sara', 'age': 25}]

for people in peoples:
    if people['age'] > 21:
        print(people['name'])




























