#Exception = an event that interrupt the flow of program
#zeroDivisionError,typeError,ValueError)
try:
    number = int(input("enter number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some clean up here")

