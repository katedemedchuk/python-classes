# Программи принимает два значения скорости
# Первое в  km/h второе m/s
# Выводит следуюее сообение (Скорости равны/ km/h больше / m/s больше)

speed_kmh = input('Enter your speed km/h: ')
speed_ms = input("Enter your speed m/s: ")
speed_kmh = int(speed_kmh)
speed_ms = int(speed_ms)
speed_kmh_ms = speed_kmh / 3,6
if speed_kmh_ms == speed_ms:
    print("Speeds are equal")
if speed_kmh_ms > speed_ms:
    print("Km/h > m/s")
if speed_kmh_ms < speed_ms:
    print("Km/h < m/s")