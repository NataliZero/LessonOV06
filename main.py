# Класс Hero, представляющий героя с именем, здоровьем и силой атаки
class Hero:
    def __init__(self, hero_name, health=100, attack_power=20):
        self.name = hero_name
        self.health = health
        self.attack_power = attack_power

    # Метод атаки другого героя
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона!")
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    # Метод для проверки, жив ли герой
    def is_alive(self):
        return self.health > 0


# Класс Game, представляющий саму игру
class Game:
    def __init__(self, player_hero_name):
        self.player = Hero(player_hero_name)
        self.computer = Hero("Компьютер", health=120, attack_power=15)

    # Метод для начала игры
    def start(self):
        print("Добро пожаловать в игру: Битва героев!")
        print(f"{self.player.name} против {self.computer.name}\n")

        # Цикл игры: пока оба героя живы, чередуются их ходы
        while self.player.is_alive() and self.computer.is_alive():
            input("Нажмите Enter для вашего хода...")
            self.player.attack(self.computer)

            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            print("Ход компьютера:")
            self.computer.attack(self.player)

            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break


# Основная функция для запуска игры
def main():
    unique_player_name = input("Введите имя вашего героя: ")
    game_instance = Game(unique_player_name)
    game_instance.start()


if __name__ == "__main__":
    main()
