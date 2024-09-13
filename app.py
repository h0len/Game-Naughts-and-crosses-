import random
import sys

def one_move_plus_check():
    global player_num
    check = 0
    while check != 1:
        answer = list(filter(None, (str(input()).split(" "))))  # Записываем ответ и уничтожаем все лишние пробелы, которые могли появиться
        if len(answer) != 2:
            print_wrong_input()
        else:
            if all(elem.isdigit() for elem in answer) == True:
                if all([4 > int(element) > 0 for element in answer]) == True:
                        ans_string, ans_collumn = int(answer[0]) - 1, int(answer[1]) - 1  # Записываем номер строки и номер столбца
                        if is_avalible(ans_string, ans_collumn) == True:
                            field[ans_string][ans_collumn] = dif_for_players()
                            print_field()
                            check += 1
                            if check_win() == True:
                                print(f"{definitior_of_player()} выиграл! Поздравляем!")
                                sys.exit(0)
                            else:
                                print("Ход засчитан!")
                        else:
                            print("Клеточка уже занята! Введите другой ответ:")
                            continue
                else:
                    print_wrong_input()
            else:
                print_wrong_input()
    player_num += 1
    print("Пришло время хода другого игрока!")

def print_field():
    for stringg in field:
        print(stringg)

def print_wrong_input():
    print("Вы ввели свой ответ в неправильном формате! Введите еще раз:")

def dif_for_players():
    if player_num % 2 == 0:
        return "O"
    else:
        return "X"

def definitior_of_player():
    if player_num % 2 == 0:
        return "Второй игрок"
    else:
        return "Первый игрок"

def is_avalible(ans1, ans2):
    if field[ans1][ans2] == "-":
        return True
    else:
        return False

def check_win():
    if field[0][0] == field[1][0] == field[2][0] and field[0][0] != "-" and field[1][0] != "-" and field[2][0] != "-":  # 1 столбец
        return True
    if field[0][1] == field[1][1] == field[2][1] and field[0][1] != "-" and field[1][1] != "-" and field[2][1] != "-":  # 2 столбец
        return True
    if field[0][2] == field[1][2] == field[2][2] and field[0][2] != "-" and field[1][2] != "-" and field[2][2] != "-":  # 3 столбец
        return True
    if field[0][0] == field[0][1] == field[0][2] and field[0][0] != "-" and field[0][1] != "-" and field[0][2] != "-":  # 1 строка
        return True
    if field[1][0] == field[1][1] == field[1][2] and field[1][0] != "-" and field[1][1] != "-" and field[1][2] != "-":  # 2 строка
        return True
    if field[2][0] == field[2][1] == field[2][2] and field[2][0] != "-" and field[2][1] != "-" and field[2][2] != "-":  # 3 строка
        return True
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != "-" and field[1][1] != "-" and field[2][2] != "-":  # 1 диагональ
        return True
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != "-" and field[1][1] != "-" and field[2][0] != "-":  # 2 диагональ
        return True
    else:
        return False


print("""Добро пожаловать в игру \"КРЕСТИКИ-НОЛИКИ\"!
Для начала сядьте слева и справа от компьютера. Игрок слева будет первым, а справа вторым.
Подбросим монетку и определим, кто ходит первым!\n""")

lst = ["Первый игрок начинает первым!", "Второй игрок игрок начинает первым!\n"]
print(random.choice(lst))

field = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
print_field()

print("""\nВведите куда поставить крестик. Запрос должен быть сделан в виде: {число обозначающее строку} {число обозначающее стобец}
Например: 1 2. Данная запись обозначает, что игрок заберет себе верхнюю центральную клеточку.""")

player_num = 1
while True:
    check = 0
    while check != 1:
        answer = list(filter(None, (str(input()).split(" "))))  # Записываем ответ и уничтожаем все лишние пробелы, которые могли появиться
        if len(answer) != 2:
            print_wrong_input()
        else:
            if all(elem.isdigit() for elem in answer) == True:
                if all([4 > int(element) > 0 for element in answer]) == True:
                    print("Ход засчитан!")
                    ans_string, ans_collumn = int(answer[0]) - 1, int(answer[1]) - 1  # Записываем номер строки и номер столбца
                    field[ans_string][ans_collumn] = "X"
                    print_field()
                    check += 1
                else:
                    print_wrong_input()
            else:
                print_wrong_input()
    print("Пришло время хода другого игрока!")
    player_num += 1
    for i in range(8):
        one_move_plus_check()
    print("Ничья! Победила дружба!")
    break