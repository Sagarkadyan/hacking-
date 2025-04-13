i=1
a=1
def fizzbuzz(num):
   for i in  range(1,num+1):
    if i % 3 == 0 and i  % 7 == 0:
        print("FizzBuzz")
        
    elif i  % 3 == 0:
        print("Fizz")

    elif i % 7 == 0:
    
        print("Buzz")
    elif '3' in str(i):
        print("Almost Fizz")
          
    else:
        
        print(i)

# Example usage
num = int(input())
fizzbuzz(num)
