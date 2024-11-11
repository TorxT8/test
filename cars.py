car = open('abcd.txt','r')

marc_car = []
model_car = []
year_of_release = []
color_car = []
price_car = []
fari_car = []
door_car = []
engine_car = []
j = 1

j = car.readline()
file = j.split("&")
if j != "":

    if len(file[0].split()) == 1:
        marc_car = [file[0]]
        model_car = [file[1]]
        year_of_release= [file[2]]
        color_car= [file[3]]
        price_car= [file[4]]
        fari_car= [file[5]]
        door_car= [file[6]]
    else:
        marc_car = file[0].split(' ; ')
        model_car = file[1].split(' ; ')
        year_of_release = file[2].split(' ; ')
        color_car = file[3].split(' ; ')
        price_car = file[4].split(' ; ')
        fari_car = file[5].split(' ; ')
        door_car = file[6].split(' ; ')

while True:
    try:       
        print('1) Показать таблицу машин')
        print('2) Добавить машину')
        print('3) Убрать машину')
        print('4) Изменить данные машины')
        print('5) Поиск')
        print('6) Выход')
        go = int(input('Выберите действие: '))
        if go < 7 and go > 0:
        
            if go == 1:
                nom = "№"
                marca ="Марка"
                moda ="Модель"
                yer ="Год"
                col ="Цвет"
                pr ="Цена"
                far ="Фары"
                dor ="двери"
                
                print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")
                for x in range(len(marc_car)):
                    nom = f"{x+1})"
                    marca = marc_car[x]
                    moda = model_car[x]
                    yer = year_of_release[x]
                    col = color_car[x]
                    pr = price_car[x]
                    far = fari_car[x]
                    dor = door_car[x]

                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")

            if go == 2:
                carina = open('abcd.txt','w')
                mar = str(input('Введите марку машины '))
                mod = str( input('Введите модель машины '))
                year = str( input('Введите введите год машины '))
                price = str( input('Введите введите цену машины '))

                print("1) Белый")
                print("2) Чёрный")
                print("3) Красный")
                print("4) Оранжевый")
                print("5) Жёлтый")
                print("6) Зелёный")
                print("7) Голубой")
                print("8) Синий")
                print("9) Фиолетовый")
                print("+) Если вашего цвета нет в списке вы можете ввести его вручную")
                call = str(input("Выберите цвет: "))
                if call =='1':
                    color = "Белый"
                elif call =='2':
                    color = "Чёрный"
                elif call =='3':
                    color = "Красный"
                elif call =='4':
                    color = "Оранжевый"
                elif call =='5':
                    color = "Жёлтый"
                elif call =='6':
                    color = "Зелёный"
                elif call =='7':
                    color = "Голубой"
                elif call =='8':
                    color = "Синий"
                elif call =='9':
                    color = "Фиолетовый"
                elif call > 9 or call<0:
                    print('чото не то')
                else:
                    color = call

                while True:
                    try:
                        print("1) Включены")
                        print("2) Выключены")
                        qq = input("Выберите состояние фар: ")
                        if int(qq) == 1:
                            far = "Включены"
                        elif int(qq) == 2:
                            far = "Выключены"
                        else:
                            print("Выбрать можно только из двух состояний!")
                            continue
                        break
                    except ValueError:
                        print("Выбрать можно только из двух состояний!")




                while True:
                    try:
                        print("1) Открыты")
                        print("2) Закрыты")
                        qq=input("Выберите состояние дверей: ")
                        if int(qq) == 1:
                            dor = "Открыты"
                        elif int(qq) == 2:
                            dor = "Закрыты"
                        else:
                            print("Выбрать можно только из двух состояний!")
                            continue
                        break
                    except ValueError:
                        print("Выбрать можно только из двух состояний!")


                marc_car.append(mar)
                model_car.append(mod)
                year_of_release.append(year)
                color_car.append(color)
                price_car.append(price)
                fari_car.append(far)
                door_car.append(dor)

                marc_car_save = ' ; '.join(marc_car)+"&" 
                model_car_save = ' ; '.join(model_car)+"&"
                year_of_release_save = ' ; '.join(year_of_release)+"&"
                color_car_save = ' ; '.join(color_car)+"&"
                price_car_save = ' ; '.join(price_car)+"&"
                fari_car_save = ' ; '.join(fari_car)+"&"
                door_car_save = ' ; '.join(door_car) +"&"

                carina.writelines(marc_car_save)
                carina.writelines(model_car_save)
                carina.writelines(year_of_release_save)
                carina.writelines(color_car_save)
                carina.writelines(price_car_save)
                carina.writelines(fari_car_save)
                carina.writelines(door_car_save)

                carina.close()

            if go == 3:
                sol = int(input('Введите номер строки: ')) - 1
                if sol < 0:
                    print('Нет такой строки\n')
                elif sol > len(marc_car)+1:
                    print('Нет такой строки\n')
                else:
                    carina = open('car.txt','w')

                    nom = "№"
                    marca ="Марка"
                    moda ="Модель"
                    yer ="Год"
                    col ="Цвет"
                    pr ="Цена"
                    far ="Фары"
                    dor ="двери"
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")

                    print(f"{sol+1:<7}{marc_car[sol]:<20}{model_car[sol]:<20}{year_of_release[sol]:<20}{color_car[sol]:<20}{price_car[sol]:<20}{fari_car[sol]:<20}{door_car[sol]:<20}")
                    print('Вы действительно хотите удалить эту строчку')

                    sogl = str(input('Да/Нет: '))

                    if sogl == 'Да' or sogl == 'да' or sogl == 'ДА' or sogl == 'дА':
                        marc_car.pop(sol)
                        model_car.pop(sol)
                        year_of_release.pop(sol)
                        color_car.pop(sol)
                        price_car.pop(sol)
                        fari_car.pop(sol)
                        door_car.pop(sol)

                        marc_car_save = ' ; '.join(marc_car)+"&"
                        model_car_save = ' ; '.join(model_car)+"&"
                        year_of_release_save = ' ; '.join(year_of_release)+"&"
                        color_car_save = ' ; '.join(color_car)+"&"
                        price_car_save = ' ; '.join(price_car)+"&"
                        fari_car_save = ' ; '.join(fari_car) +"&"
                        door_car_save = ' ; '.join(door_car) +"&"

                        carina.writelines(marc_car_save)
                        carina.writelines(model_car_save)
                        carina.writelines(year_of_release_save)
                        carina.writelines(color_car_save)
                        carina.writelines(price_car_save)
                        carina.writelines(fari_car_save)
                        carina.writelines(door_car_save)
                        print('Строчка удалена')
                    else:
                        print('Строчка не удалена')

                    carina.close()

            if go == 4:
                carina = open('carina.txt','w')
                sol = int(input('Введите номер строки: ')) - 1
                if sol < 0:
                    print('Нет такой строки\n')
                elif sol == len(marc_car):
                    print('Нет такой строки\n')
                else:

                    print('1) Состояние фар')
                    print('2) Состояние дверей')
                    print('3) Цвет')
                    print('4) Цена')

                    a = int(input('Выберете что заменить: '))
                    if a == 1:
                        while True:
                            try: 
                                print("1) Включены")
                                print("2) Выключены")
                                qq = input("Выберите состояние фар: ")
                                if int(qq) == 1:
                                    far = "Включены"
                                    fari_car[sol] = far
                                elif int(qq) == 2:
                                    far = "Выключены"
                                    fari_car[sol] = far
                                else:
                                    continue
                                break
                            except ValueError:
                                print("Выбрать можно только из двух состояний!")


                    if a ==2:
                        while True:
                            try: 
                                print("1) Открыты")
                                print("2) Закрыты")
                                qq = input("Выберите состояние дверей: ")
                                if int(qq) == 1:
                                    dor = "Открыты"
                                    door_car[sol] = dor
                                elif int(qq) == 2:
                                    dor = "Закрыты"
                                    door_car[sol] = dor
                                else:
                                    continue
                                break
                            except ValueError:
                                print("Выбрать можно только из двух состояний!")



                    if a == 3:                  
                        print("1) Белый")
                        print("2) Чёрный")
                        print("3) Красный")
                        print("4) Оранжевый")
                        print("5) Жёлтый")
                        print("6) Зелёный")
                        print("7) Голубой")
                        print("8) Синий")
                        print("9) Фиолетовый")
                        print("+) Если вашего цвета нет в списке вы можете ввести его вручную")
                        call = str(input("выберите новый цвет: "))
                        if call == '1':
                            color = "Белый"
                        elif call == '2':
                            color = "Чёрный"
                        elif call == '3':
                            color = "Красный"
                        elif call == '4':
                            color = "Оранжевый"
                        elif call == '5':
                            color = "Жёлтый"
                        elif call == '6':
                            color = "Зелёный"
                        elif call == '7':
                            color = "Голубой"
                        elif call == '8':
                            color = "Синий"
                        elif call == '9':
                            color = "Фиолетовый"
                        else:
                            color = call
                        color_car[sol]=color

                    if a == 4:
                        price_car[sol]=input('Введите новую цену: ')

                    marc_car_save = ' ; '.join(marc_car)+"&"
                    model_car_save = ' ; '.join(model_car)+"&"
                    year_of_release_save = ' ; '.join(year_of_release)+"&"
                    color_car_save = ' ; '.join(color_car)+"&"
                    price_car_save = ' ; '.join(price_car)+"&"
                    fari_car_save = ' ; '.join(fari_car)+"&"
                    door_car_save = ' ; '.join(door_car)+"&"

                    carina.writelines(marc_car_save)
                    carina.writelines(model_car_save)
                    carina.writelines(year_of_release_save)
                    carina.writelines(color_car_save)
                    carina.writelines(price_car_save)
                    carina.writelines(fari_car_save)
                    carina.writelines(door_car_save)

                    carina.close()

            if go == 6:
                break
            if go == 5:
                print("Выберите столбец по которому будет осуществлен поиск")
                print('1)поиск Марка')
                print('2)поиск Модель')
                print('3)поиск Год')
                print('4)поиск Цвет')
                print('5)поиск Цена')
                print('6)поиск Фары')
                print('7)поиск Двери')
                vib = int(input())
                nom = "№"
                marca = "Марка"
                moda = "Модель"
                yer = "Год"
                col = "Цвет"
                pr = "Цена"
                far = "Фары"
                dor = "двери"
                if vib == 1:
                    print('Поиск')
                    poisk = str(input())
                    DP = len(poisk)
                    i = 0
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")
                    for a in marc_car:
                        i += 1
                        a = a.replace('ё', 'е', )
                        a = a.lower()
                        poisk = poisk.replace('ё', 'е', )
                        poisk = poisk.lower()
                        if poisk == a[0:DP]:
                            print(f"{i:<7}{marc_car[i - 1]:<20}{model_car[i - 1]:<20}{year_of_release[i - 1]:<20}{color_car[i - 1]:<20}{price_car[i - 1]:<20}{fari_car[i - 1]:<20}{door_car[i - 1]:<20}")
                if vib == 2:
                    print('Поиск')
                    poisk = str(input())
                    DP = len(poisk)
                    i = 0
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<10}{col:<15}{pr:<20}{far:<20}{dor:<20}")
                    for a in model_car:
                        i += 1
                        a = a.replace('ё', 'е', )
                        a = a.lower()
                        poisk = poisk.replace('ё', 'е', )
                        poisk = poisk.lower()
                        if poisk == a[0:DP]:
                            print(f"{i:<7}{marc_car[i - 1]:<20}{model_car[i - 1]:<20}{year_of_release[i - 1]:<10}{color_car[i - 1]:<15}{price_car[i - 1]:<20}{fari_car[i - 1]:<20}{door_car[i - 1]:<20}")
                if vib == 3:
                    print('Поиск')
                    poisk = str(input())
                    DP = len(poisk)
                    i = 0
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")
                    for a in year_of_release:
                        i += 1
                        a = a.replace('ё', 'е', )
                        a = a.lower()
                        poisk = poisk.replace('ё', 'е', )
                        poisk = poisk.lower()
                        if poisk == a[0:DP]:
                            print(f"{i:<7}{marc_car[i - 1]:<20}{model_car[i - 1]:<20}{year_of_release[i - 1]:<20}{color_car[i - 1]:<20}{price_car[i - 1]:<20}{fari_car[i - 1]:<20}{door_car[i - 1]:<20}")
                if vib == 4:
                    print('Поиск')
                    poisk = str(input())
                    DP = len(poisk)
                    i = 0
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")
                    for a in color_car:
                        i += 1
                        a = a.replace('ё', 'е', )
                        a = a.lower()
                        poisk = poisk.replace('ё', 'е', )
                        poisk = poisk.lower()
                        if poisk == a[0:DP]:
                            print(f"{i:<7}{marc_car[i - 1]:<20}{model_car[i - 1]:<20}{year_of_release[i - 1]:<20}{color_car[i - 1]:<20}{price_car[i - 1]:<20}{fari_car[i - 1]:<20}{door_car[i - 1]:<20}")

                if vib == 5:
                    print('Поиск')
                    poisk = str(input())
                    DP = len(poisk)
                    i = 0
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")
                    for a in price_car:
                        i += 1
                        a = a.replace('ё', 'е', )
                        a = a.lower()
                        poisk = poisk.replace('ё', 'е', )
                        poisk = poisk.lower()
                        if poisk == a[0:DP]:
                            print(f"{i:<7}{marc_car[i - 1]:<20}{model_car[i - 1]:<20}{year_of_release[i - 1]:<20}{color_car[i - 1]:<20}{price_car[i - 1]:<20}{fari_car[i - 1]:<20}{door_car[i - 1]:<20}")
                if vib == 6:
                    print('Поиск')
                    poisk = input()
                    DP = len(poisk)
                    i = 0
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")
                    for a in fari_car:
                        i += 1
                        a = a.replace('ё', 'е', )
                        a = a.lower()
                        poisk = poisk.replace('ё', 'е', )
                        poisk = poisk.lower()
                        if poisk == a[0:DP]:
                            print(f"{i:<7}{marc_car[i - 1]:<20}{model_car[i - 1]:<20}{year_of_release[i - 1]:<20}{color_car[i - 1]:<20}{price_car[i - 1]:<20}{fari_car[i - 1]:<20}{door_car[i - 1]:<20}")
                if vib == 7:
                    print('Поиск')
                    poisk = str(input())
                    DP = len(poisk)
                    i = 0
                    print(f"{nom:<7}{marca:<20}{moda:<20}{yer:<20}{col:<20}{pr:<20}{far:<20}{dor:<20}")
                    for a in door_car:
                        i += 1
                        a = a.replace('ё', 'е', )
                        a = a.lower()
                        poisk = poisk.replace('ё', 'е', )
                        poisk = poisk.lower()
                        if poisk == a[0:DP]:
                            print(f"{i:<7}{marc_car[i - 1]:<20}{model_car[i - 1]:<20}{year_of_release[i - 1]:<20}{color_car[i - 1]:<20}{price_car[i - 1]:<20}{fari_car[i - 1]:<20}{door_car[i - 1]:<20}")
                else:
                    print('Выберите другую функцию')
                    continue
        else:
            print('Выберите существующие действие')
    except:
        print("Неправельно введено значение\n")
