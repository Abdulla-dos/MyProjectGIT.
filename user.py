class Car:

    def __init__(self, brand, model, year, speed=0.0):
        if year > 2026:
            raise ValueError("Шыққан жылы болашақта болуы мүмкін емес!")
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = max(0.0, speed)
        print(
            f"Көлік: {self.brand} {self.model}, Жылы: {self.year}, Жылдамдық: {self.speed}"
        )

    def accelerate(self, amount):
        if amount <= 0:
            raise ValueError("Жылдамдық мөлшері 0-ден үлкен болуы керек!")
        self.speed += amount
        print(f"Жылдамдық артты: {self.speed}")

    def brake(self, amount):
        if amount <= 0:
            raise ValueError("Азайту мөлшері 0-ден үлкен болуы керек!")
        self.speed = max(0.0, self.speed - amount)
        print(f"Жылдамдық азайды: {self.speed}")

    def get_age(self):
        current_year = 2026
        age = current_year - self.year
        print(f"Көліктің жасы: {age}")
        return age


try:
    my_car = Car("Toyota", "Camry", 2012)
except ValueError as e:
    print(f"Көлік құру қатесі: {e}")
    exit()

while True:
    print("\n--- МЕНЮ ---")
    print("1 - Жылдамдықты арттыру")
    print("2 - Жылдамдықты азайту")
    print("3 - Көліктің жасын анықтау")

    try:
        choice = int(input("\nТек бір функцияны таңдаңыз (1, 2 немесе 3): "))

        if choice == 1:
            try:
                my_car.accelerate(60)
            except ValueError as e:
                print(f"1-тапсырма қатесі: {e}")

        elif choice == 2:
            try:
                my_car.brake(20)
            except ValueError as e:
                print(f"2-тапсырма қатесі: {e}")

        elif choice == 3:
            try:
                my_car.get_age()
            except Exception as e:
                print(f"3-тапсырма қатесі: {e}")

        else:
            print("Қате таңдау! Тек 1, 2 немесе 3 сандарын таңдаңыз.")

    except ValueError:
        print("Жалпы қате: Менюді таңдау үшін де тек сан енгізу керек!")