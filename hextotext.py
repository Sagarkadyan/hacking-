'''def print_pattern(rows, cols):
    # Write your code here
    for i in range(rows):
         print(('*' * cols +'\n') , end = '') 
  
    

# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern(rows, cols)'''
'''a=int(input())

c=0
for i in range(a):
    b=int(input())    
    c+=b
print(c)    
a=int(input())
b=0
for i in range(1,10001,1):
        b+=i
def hell():
  for j in range(a):
   print(b)    
hell()   
def hell():
        print(a*b)
        
a=int(input())
b=int(input())
hell()   
b=1
def square_number():
        b=n**2
        return b
n=int(input())

result = square_number()
print(result)   
  

         

def sigma():
    b = 0  # Initialize b to 0
    for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
        b = b + i  # Accumulate the sum
    return b  # Return the result

# Get input from the user
n = int(input())  # Prompt the user for input
result = sigma()  # Call the sigma function with n

print(result)  # Print the result   
            
import random 
random.random()
choices=[3,4,5,6]
get=random.choice(choices)
print(get)
shopping_list=["bread","eggs","milk","butter"]
print(shopping_list)
lst = input().split(",")
# Write your code below
a=[]
b=[]
for i in range(0,len(lst)):
     
       a.append(len(lst[i]))
for j in range(0,len(a)):
        if a[j]>5:
          b.append(lst[j]) 
                
print(b)            

text = input()
b=0
# Write your code below
for i in range(len(text)):
     text=text.lower()
     if  text[i]=='p':
      b+=1
      print(text[i+1])
     
print(b)    
text = input()
delimiter = input()
# Write your code below
lst=text.split()
lst=delimiter.join(lst)


print(lst)'''
lst = input().split(",")
ls=[]
a=len(lst)
if  a==1:
     ls.append(lst[0])  
     print(ls) 
elif a%2==0:
  b=a//2
  ls.append(lst[b-1])
  ls.append(lst[b])
  print(ls)
else:
  b=a//2
  ls.append(lst[b-1])
  ls.append(lst[b])
  ls.append(lst[b+1])
  
  print(ls)     