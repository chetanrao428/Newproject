def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

class Employee:
    def __init__(self, emp_number, name):
        self.__emp_number = emp_number
        self.__name = name

    def get_emp_number(self):
        return self.__emp_number

    def get_name(self):
        return self.__name

def main():
    result_add = add_numbers(5, 3)
    print(f"The result of addition is: {result_add}")
    
    result_subtract = subtract_numbers(5, 3)
    print(f"The result of subtraction is: {result_subtract}")
    
    result_multiply = multiply_numbers(5, 3)
    print(f"The result of multiplication is: {result_multiply}")
    
    emp = Employee(1, "John Doe")
    print(f"Employee Number: {emp.get_emp_number()}, Name: {emp.get_name()}")
    
    emp_info = {
        "emp_number": emp.get_emp_number(),
        "name": emp.get_name()
    }
    print(f"Employee Information: {emp_info}")

if __name__ == "__main__":
    main()
