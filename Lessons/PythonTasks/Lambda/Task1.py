# coding=windows-1251

a = input("Введите имя:")
while a != "off":
    user = lambda x: a + ' ' + "гений"
    print(user(a))
    a = input("Введите имя:")
print("Закончена.")
