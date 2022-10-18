import os
import shutil


class FileManager:

    def Path(self, name):  # получение полной рабочей директории и преемещениет в нуднрое имя
        try:
            path = os.path.abspath("WorkFlow") + '/' + name
            return path
        except:
            print("Нельзя получить путь к файлу!!!")

    def ShowContent(self, name):
        try:
            file = open(name, "r")
            print(file.read())
        except:
            print("Такого файла не существует!!!")

    def ShowCatalogue(self, directory):
        try:
            for filename in os.listdir(directory):
                print(filename)
        except:
            print("Нельзя получить доступ")

    def Proverka(self, name, directory):  # защита от того чтобы пользователь положил файл не в то место
        shutil.move(name, os.path.abspath(directory))

    def CreateFolder(self, name):
        os.mkdir(name)
        self.Proverka(name, "WorkFlow")
        self.ShowCatalogue("WorkFlow")

    def DeleteFolder(self, name):  # удаляем папку и ее все содержимое
        try:
            path = self.Path(name)
            os.rmdir(path)
            self.ShowCatalogue("WorkFlow")
        except FileNotFoundError:
            print("Такого файла не существует")

    def Move(self, name):
        try:
            if name != "WorkFlow":
                path = self.Path(name)
                os.chdir(path)
                print(os.getcwd())
            else:
                self.Move("")
        except FileNotFoundError:
            print("Такого файла не существует")

    def CreateFile(self, name):
        try:
            open(name, "w")
            self.Proverka(name, "WorkFlow")
            self.ShowCatalogue("WorkFlow")
        except shutil.Error:
            print("Нельзя создать файл, он уже существует!!!")

    def WriteToFile(self, name, content):
        print(f"Имя файла куда хотите положить: {name}, переданная информация: {content}")
        files = []
        flag = 0
        for filename in os.listdir("Workflow"):
            files.append(filename)

        for i in range(len(files)):
            if files[i] == name:
                flag += 1
                textFile = open(name, "w")
                textFile.write(content)

        if flag == 0:
            print("Информация не записана, такого файла не существует!")

    def removeFile(self, name):
        try:
            os.remove(self.Path(name))
            print("Файл успешно удален!!!")
        except:
            print("Нет такого файла")

    def CopyFiles(self, CatalogueNameStart, CatalogueNameFinish):
        try:
            shutil.copy(self.Path(CatalogueNameStart), self.Path(CatalogueNameFinish), follow_symlinks=True)
        except:
            print("Неправильная директория, слдеовательно копирование не разрашеается")

    def RenameFile(self, OldName, NewName):
        try:
            os.rename(OldName, NewName)
        except:
            print("Такого файла не сущетсвует!!!")


test = FileManager()
# test.CreateFolder("Codessswefefsdrrdd")
# test.DeleteFolder("Codessswefefsdrrdd")
# test.Move("Codessssdddee")
# test.CreateFile("efjrrkwnfjnef.txt")
# test.WriteToFile("efjkwnfjnef.txt", "hefbwkfhciuwehfiunifw")
# test.ShowContent("efjkwnfjnef.txt")
#test.removeFile("eiurhfiuheriufhiuerh")
test.CopyFiles("Codessswefefsddd", "Codessssddd")


