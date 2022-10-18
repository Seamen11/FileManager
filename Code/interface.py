import main

def menu():
    num = input('Выберите действие:\n'
                '1.Создание папки\n'
                '2.Удаление папки\n'
                '3.Перемещение между папками\n'
                '4.Создание пустых файлов\n'
                '5.Запись текста в файл\n'
                '6.Просмотр содержимого текстового файла\n'
                '7.Удаление файлов по имени\n'
                '8.Копирование файлов из одной папки в другую\n'
                '9.Перемещение файлов\n'
                '10.Переименование файлов\n'
                '11.exit\n'
                '---')

    if (num == '1'):
        param = input('Введите название папки: ')
        main.file.mkdir(param)
        menu()
    elif (num == '2'):
        param = input('Введите название папки: ')
        main.file.rmdir(param)
        menu()
    elif (num == '3'):
        param = input('Введите название папки: ')
        main.file.chdir(param)
        menu()
    elif (num == '4'):
        param = input('Введите название файла: ')
        main.file.touch(param)
        menu()
    elif (num == '5'):
        name = input('Введите название файла: ')
        text = input('Введите текст: ')
        main.file.write(name, text)
        menu()
    elif (num == '6'):
        name = input('Введите название файла: ')
        main.file.cat(name)
        menu()
    elif (num == '7'):
        name = input('Введите название файла: ')
        main.file.remove(name)
        menu()
    elif (num == '8'):
        name1 = input('Введите название папки1: ')
        name2 = input('Введите название папки2: ')
        main.file.copyFiles(name1,name2)
        menu()
    elif (num == '9'):
        name1 = input('Введите название файла1: ')
        name2 = input('Введите название файла2: ')
        main.file.replace(name1,name2)
        menu()
    elif (num == '10'):
        name1 = input('Введите название файла1: ')
        name2 = input('Введите название файла2: ')
        main.file.rename(name1,name2)
        menu()
    elif (num == '11'):
        return False
    else:
        menu()



menu()