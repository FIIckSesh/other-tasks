#Заводим глобальные переменные
current_len = 0
best_len = 0
best_path = ''
current_path = ''

def search_path(path):
  global current_path
  global current_len
  global best_len
  global best_path

  #Если директория пуста (мы пришли в конец), проверяем является ли путь наибольшим, запоминаем его
  if len(path) == 0:
    if current_len > best_len:
      best_path = current_path
      best_len = current_len
    return

  #Основной цикл, если директория, продолжаем углубляться
  if isinstance(path, dict):
    for key in path.keys():
      current_len += 1
      current_path = current_path + '/' + str(key)
      search_path(path[key])

      #Откатываем путь
      current_len -=1
      current_path = current_path[0:len(current_path) - len(key) - 1]
  else: #Если файлы, то удаляем файлы с одинаковым именем
    files = path
    amount = [files.count(file) for file in files]

    for i in range(len(amount) - 1, -1, -1):
      if amount[i] > 1:
        files.pop(i)
    #Если файлов не осталось, выходим
    if len(files) == 0:
      return

    #Если файлы есть, добавляем первый из списка в путь
    if current_len > best_len:
      best_path = current_path + '/' + files[0]
      best_len = current_len
    return

def biggestPath(X: dict) -> str:

  #Вызываем функцию рекурсивного обхода
  search_path(X)

  global best_path
  global best_len
  result = best_path
  best_path = ''
  best_len = 0

  #Если пути нет, возвращаем слэш
  return(result if result != '' else '/')

biggestPath({'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}})
