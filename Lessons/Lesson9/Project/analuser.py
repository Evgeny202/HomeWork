def get_reg(reg):
    if "пар" in reg.lower():
        say_couple()

    if "звон" in reg.lower():
        say_calls()

    if "трен" in reg.lower():
        say_coach()

    if "коман" in reg.lower():
        say_team()

    if "оплат" in reg.lower():
        say_payment()



def say_couple():
     print("Основы программирования,Основы работы с сетевыми операционными системами,Алгоритмы и структуры данных, Применение микропроцессорных систем.")

def say_calls():
    print("09:00 - 10:30, 10:45 - 12:15, 13:15 - 14:45, 15:00 - 16:30.")

def say_coach():
    print("88005553535")

def say_team():
    print("ЦСКА – Динамо")

def say_payment():
    print("с вас 2000 рублей")