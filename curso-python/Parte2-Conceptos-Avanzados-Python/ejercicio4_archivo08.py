# Ejercicio 4:
import asyncio
import random

async def task1():
    print('Tarea 1 en ejecución...')
    await asyncio.sleep(random.randint(1,3))
    print('Ha finalizado la tarea 1')
    
async def task2():
    print('Tarea 2 en ejecución...')
    await asyncio.sleep(random.randint(1,3))
    print('Ha finalizado la tarea 2')
    
async def task3():
    print('Tarea 3 en ejecución...')
    await asyncio.sleep(random.randint(1,3))
    print('Ha finalizado la tarea 3')
    
async def task4():
    print('Tarea 4 en ejecución...')
    await asyncio.sleep(random.randint(1,3))
    print('Ha finalizado la tarea 4')
    
async def task5():
    print('Tarea 5 en ejecución...')
    await asyncio.sleep(random.randint(1,3))
    print('Ha finalizado la tarea 5')

if __name__ == '__main__':
    async def simulate_async_task():
        print('Ejecutando tareas...')
        await asyncio.gather(
        task1(),
        task2(),
        task3(),
        task4(),
        task5()
    )
        print('Se han ejecutado todas las tareas')

    asyncio.run(simulate_async_task())
    