def user_name():
    name = input("What is your name? ")

    if not name or name.isspace() or not all(char.isalpha() or char.isspace() for char in name) or len(name) < 2:
        print("You did not enter a name.")
        return user_name()

    return name


def user_age():
    age = int(input("What is your age? "))

    if age <= 0:
        print("You did not enter a valid age.")
        return user_age()

    return age


def user_salary():
    salary = float(input("What is your salary? "))

    if salary <= 0:
        print("You did not enter a valid salary.")
        return user_salary()

    return salary


def annual_salary(salary):
    return salary * 12


def summery(name, age, salary, annual_salary):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Salary: {salary}")
    print(f"Annual Salary: {annual_salary}")


name = user_name()
age = user_age()
salary = user_salary()
annual = annual_salary(salary)

summery(name, age, salary, annual)