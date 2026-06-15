# n,k = map(int,input().split())
# arr = [1,2,3,4,5]
# k=k%n
# result = arr[-k:]+arr[:-k]
# for num in result:
#     print(num,end="")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("That was not a valid number!")
except ZeroDivisionError as e:
    print(f"Mathematical error: {e}")
else:
    print(f"Success! The calculation result is {result}")
finally:
    print("This message will always print.")