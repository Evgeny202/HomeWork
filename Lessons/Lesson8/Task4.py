"""
Во время хоккейных матчей на игроков может накладываться дисциплинарный штраф — удаление с поля на 2 или 10 минут.

Программа должна:
1) Спрашивать «Удалить с поля?» и запрашивать количество минут штрафа.
2) Печатать сообщение: «Вы удалена с поля на _ минут(-ы)» и ставить паузу в работе на это время.
3) Спустя 2 или 10 минут печатать новое сообщение: «Возвращайтесь на поле!»
Дабы не ждать 2 и 10 минут сделайте 2 и 10 секунд.
"""
import time

a = input("Удалить с поля? (да ли нет):")
if a =="да":
    b = int(input("Время штрафа:"))
    print("Вы удалены на", b, "минут(-ы)")
    time.sleep(b*60)
    print("Возращайтесь на поле!")
else:
    print()