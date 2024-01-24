# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.Функция
# возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
file = 'C:/GB/DataEngineer/PYTHON/Seminars/_Семинар 5. Погружение в Python. Итераторы и генераторы.pptx'

def file_path(path: str) ->tuple[str, str, str]:
    *file_path, file_name = file.split('/')
    *file_name, file_ext = file_name.split('.')
    return ('/').join(file_path)+'/', ('.').join(file_name), file_ext

print(file_path(file))
