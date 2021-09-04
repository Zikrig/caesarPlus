import copy
def caesar_simple(message,shift,key):
    message = message.lower()   #Переводим обе строчные переменные в нижний регистр
    key = key.lower()           #Во избежании конфликтов
    keyset=set(key)             #Делаем из списка множество
    if(len(key)>len(keyset)):   #Проверка ключа - является ли он множеством.
        return "ОШИБКА! В КЛЮЧЕ ПОВТОРЯЮТСЯ БУКВЫ"
    al='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet=list(al)           #Создание списка алфавита и его копии
    alphabet_notkey=list(al)
    for ch in key:              #Удаление из второго алфавита ключей
        alphabet_notkey.remove(ch)
    newTT=len(alphabet_notkey)  #Длина алфавита без ключа
            #составление нового алфавита
    alphabet_new=alphabet_notkey[newTT-shift:newTT]+list(key)+alphabet_notkey[0:newTT-shift]
    #print(alphabet_new)
    #print(alphabet)
    mes_new=''
    for ch in message:          #Поиск и замена букв в сообщении
        if ch in alphabet:
            mes_new+=alphabet_new[alphabet.index(ch)]
        else:
            mes_new+=ch         #...Кроме тех, которые есть в алфавите

    return mes_new