from animals import Animals
from dog import Dog
from cat import Cat
from hamster import Hamster
from horse import Horse
from donkey import Donkey
from camel import Camel
from zoo import Zoo
from menu import Menu
from datetime import datetime
from command import Commands

if __name__ == '__main__':
    dog = Dog("Jack","2023-01-02")
    hamster = Hamster("Jack","2023-01-02")
    hamsterTwo = Hamster("Like","2023-01-02")
    cat = Cat("Jack","2023-01-02")
    horse = Horse("Jack","2023-01-02")
    donkey = Donkey("Jack","2023-01-02")
    camel = Camel("Jack","2023-01-02")
    zoo = Zoo()
    zoo.add(dog)
    zoo.add(hamster)
    zoo.add(hamsterTwo)
    zoo.add(cat)
    zoo.add(horse)
    zoo.add(camel)
    zoo.add(donkey)
    command = Commands()
    # dog.commamd("Лежать")
    # dog.commamd("Сидеть")
    # dog.commamd("Ко мне")
    menu = Menu()
    # print(1 in zoo.get_Zoo_id())
    while True:
        choice = menu.show_menu()
        try:
            if  choice == '1':
                print('\n')
                zoo.show_animals()
                input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
                continue
            elif choice == '2':
                print('\n')
                zoo.show_pets()
                input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
            elif choice == '3':
                print('\n')
                zoo.show_pack_animals()
                input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
            elif choice == '4':
                zoo.show_pet()
                class_animals = input("""
            Введите порядковый номер животного, которого вы хотите завести: """)
                try:
                    if int(class_animals) in zoo.show_pets_id():
                        name_animals = input("""
            Введите имя вашего животного: """)
                        birthday_year = input("""
            Введите год рождения животного: """)
                        birthday_mouth = input("""
            Введите месяц рождения животного цифрой (1-12): """)
                        birthday_day = input("""
            Введите день рождения животного: """)
                        try:
                            if int(birthday_year) < datetime.now().year and int(birthday_mouth) in range(1,13) and 1 <= int(birthday_day):
                                if int(birthday_mouth) in [1,3,5,7,8,10,12] and int(birthday_day) <= 31:
                                    birthday_animals = f"{birthday_year}-{birthday_mouth}-{birthday_day}"
                                elif int(birthday_day) <= 30 and int(birthday_mouth) in [4,6,9,11]:
                                    birthday_animals = f"{birthday_year}-{birthday_mouth}-{birthday_day}"
                                elif int(birthday_day) <= 28 and int(birthday_mouth) == 2:
                                    birthday_animals = f"{birthday_year}-{birthday_mouth}-{birthday_day}"
                                else:
                                    raise Exception
                            else:
                                raise Exception
                        except:
                            print("""
            Вы ввели некорректную дату!""")
                            input("""
                Нажмите 'Enter' для того, чтобы продолжить""")
                        if class_animals == '1':
                            zoo.add(Cat(name_animals,birthday_animals))
                        elif class_animals == '2':
                            zoo.add(Dog(name_animals,birthday_animals))
                        elif class_animals == '3':
                            zoo.add(Hamster(name_animals,birthday_animals))
                        elif class_animals == '4':
                            zoo.add(Horse(name_animals,birthday_animals))
                        elif class_animals == '5':
                            zoo.add(Donkey(name_animals,birthday_animals))
                        elif class_animals == '6':
                            zoo.add(Camel(name_animals,birthday_animals))
                        print("""
            Животное успешно добавлено в Зоопарк!
            Ему очень понравиться у нас!""")
                        input("""
                Нажмите 'Enter' для того, чтобы продолжить""")
                    else:
                        raise Exception
                except:
                    print("""
                Вы ввели не существующий пункт!
                Такого животного у нас нет""")
                    input("""
                Нажмите 'Enter' для того, чтобы продолжить""")
                
            elif choice == '5':
                choice_id = input("""
            Введите порядковый номер животного, которого хотите обучить новым командам: """)
                try:
                    if int(choice_id) in zoo.get_Zoo_id():
                        print("""\n
            Список доступных команд, которым можно обучить животное: """)
                        command.get_List_command()
                        ch_command = input("""
            Введите номер команды, которой хотите обучить животное: """)
                        try:
                            if int(ch_command) in command.get_Id_command():
                                print()
                                zoo.get_animal(int(choice_id)).commamd(command.get_Command(int(ch_command)))
                                input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
                            else:
                                raise Exception
                        except:
                            print("""
            Введен некорректный номер команды""")
                            input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
                    else:
                        raise Exception
                except:
                    print("""
            Вы ввели не сушествующий порядковый номер животного""")
                    input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
                    
            elif choice == '6':
                ch = input("""
            Введите порядковый номер животного команды, которого хотите увидеть: """)
                try:
                    if int(ch) in zoo.get_Zoo_id():
                        ch = int(ch)
                        zoo.get_animal_command(ch)
                                                
                    else:
                        raise Exception
                except:
                    print("""
            Вы ввели не сушествующий порядковый номер животного""")
                    input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
                else:
                    input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
            elif choice == '7':
                choice_id = input("""
            Введите порядковый номер животного, которого хотите удалить из Зоопарка: """)
                try:
                    if int(choice_id) in zoo.get_Zoo_id():
                        zoo.del_Zoo(int(choice_id))
                        input("""
                Нажмите 'Enter' для того, чтобы продолжить""")
                    else:
                        raise Exception
                except:
                    print("""
            Вы ввели не сушествующий порядковый номер животного""")
                    input("""
            Нажмите 'Enter' для того, чтобы продолжить""")
            elif choice == '8':
                menu.show_end()
                break
            else:
                raise Exception()
        except:
            input("""
            Не правильный ввод!
            Введите цифру пункта меню!""")
    