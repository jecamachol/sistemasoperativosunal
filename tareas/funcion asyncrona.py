import asyncio

async def main():

    print("empieza")

    task1 = asyncio.create_task(
        decir(2, 'Hola'))

    task2 = asyncio.create_task(
        decir(4, 'Mundo'))

    task3 = asyncio.create_task(
        decir(6, 'termina'))

    
    await task1
    await task2
    await task3

async def decir(segundos, palabra):
    await asyncio.sleep(segundos)
    print(palabra)

asyncio.run(main())