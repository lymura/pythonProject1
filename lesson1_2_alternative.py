a = int(input("Введите время в секундах: "))
if a < 60:       # секунды
    print(f"ЧЧ:ММ:СС = 00:00:{a}")
elif a < 3600:     # минуты + секунды
    print(f"ЧЧ:ММ:СС = 00:{a // 60}:{a % 60}")      # часы + минуты + секунды
else:
    print(f"ЧЧ:ММ:СС = 00:{a // 3600}:{a % 3600 // 60}:{a % 60}")
