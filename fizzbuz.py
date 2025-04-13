def fizzbuzz(num):
    if num % 3 == 0 and num % 7 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 7 == 0:
        return "Buzz"
    else:
        return str(num)

# Example usage
number = int(input("Enter a number: "))
print(fizzbuzz(number))
