# Ejercicio 1
employee_id: int = 46220629
employee_name: str = 'Javier'
employee_salary: float = 2800.45

print(f'El ID del empleado es: {employee_id}')
print(f'El nombre del empleado es: {employee_name}')
print(f'El salario del empleado es: {employee_salary}')

# Ejercicio 2
def sum_salaries(salary1: float, salary2: float) -> float:
    '''
    Devuelve la suma de ambos salarios
    '''
    return salary1 + salary2

employee_salary1: float = 2800.45
employee_salary2: float = 1000.91

print(sum_salaries(employee_salary1,employee_salary2))
#Es una buena practica redondear los numeros
print(round(sum_salaries(employee_salary1,employee_salary2),2))

# Ejercicio 3
import random
from typing import Optional

def find_employee(employees: list[str], name: str) -> Optional[str]:
    ''''
    Devuelve en nombre del empleado si existe en la lista
    de lo contraerio, None
    '''
    if name in employees:
        return name
    else:
        return None

employees = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
name = employees[random.randint(0,len(employees)-1)]
print(find_employee(employees,name))
print(find_employee(employees,'Carly'))


# Ejercicio 4
from typing import Union
def process_age(age: Union[int,str]) -> int:
    '''
    Convierte la variable a tipo entero
    '''
    if isinstance(age, int):
        return age
    elif '.' in age:
        return round(float(age))
    else:
        return int(age)

print (process_age('30'))
print (process_age(2))
print (process_age('33.3'))
print (process_age('59.6'))

# Ejercicio 5
class Employee:
    name: str
    age: int
    salary: float
    def __init__(self, name:str, age:int, salary:float):
        self.name = name
        self.age = age
        self.salary = salary
    
    def introduce(self) -> str:
        return f'Hi!, my name is {self.name}. I am {self.age} years old and my salary is {self.salary}'
    
person = Employee('juan', 19, 2350.21)
print(person.introduce())