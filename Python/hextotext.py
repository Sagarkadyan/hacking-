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


print(lst)
lst = input().split(",")
b=len(lst)
b=b//2
# Write your code below
lst1=[]
lst2=[]
lst3=[]
lst1=lst[1:len(lst):2]
lst2=lst[-1::-6]
lst3=lst[b::2]
print(lst1)
print(lst2)
print(lst3)

print("Welcome to the Daily Expense Tracker!\n")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses") 
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expense_list=[]
a=0
while True:
        it=int(input())
        if it==1:
            i=float(input())
           
            expense_list.append(i)
            print("Expense added successfully!")
            
        elif it==2:
           if  not expense_list:
               print("No expenses recorded yet.")
           else:
               print("Your expenses:")    
               for i in range(len(expense_list)):    
                print(f"{i+1}. {expense_list[i]}")        
        elif it==3:
               if  not expense_list:
                 print("No expenses recorded yet.") 
               else:
                 for i in range(len(expense_list)):
                        a+=expense_list[i]
                 print("Total expense:",a)
                 print("Average expense:",a/(len(expense_list)))       
                          
        elif it==4:
              expense_list.clear()
              
        elif it==5:
          print("Exiting the Daily Expense Tracker. Goodbye!")
          break
        else:
                print("Invalid choice. Please try again.")'''
'''
n=int(input())
for i  in range(1,n+2,2):
        print("*"*i)
prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0


# Write your code below
for i in range(len(prices)):
        if prices[i] > budget_per_item :
                cant_afford+=1
        else:
                affordable_items.append(items[i])
                total_needed+=prices[i]







print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
'''
from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
conn.commit()
conn.close()

# HTML Template
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>To-Do List</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-xl mx-auto bg-white rounded-xl shadow-md p-6">
        <h1 class="text-2xl font-bold mb-4">To-Do List</h1>
        <form action="/add" method="post" class="flex mb-4">
            <input type="text" name="task" placeholder="New task..." required class="flex-1 p-2 border rounded-l">
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-r">Add</button>
        </form>
        <ul>
            {% for task in tasks %}
            <li class="flex justify-between items-center mb-2">
                <span>{{ task[1] }}</span>
                <a href="/delete/{{ task[0] }}" class="text-red-500">Delete</a>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template_string(HTML, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

