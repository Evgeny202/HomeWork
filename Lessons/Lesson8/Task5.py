"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
import random
import time

start = input("Подбросить кубик(напишите start):")
if start == "start":
    print("Подбрасываю кубики.")
    cube_1 = random.randint(1, 6)
    cube_2 = random.randint(1, 6)

    time.sleep(2)
    print(cube_1, cube_2)
else:
    print()
