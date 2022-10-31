feedback = int(input("Стоимость товаров:"))
while feedback != 0:
    feedback1 = feedback - ((feedback / 100) * 10)  # 10 - это процент скидки
    print(feedback1)
    feedback = int(input("Стоимость товаров:"))
else:
    print("Работа завершена.")

