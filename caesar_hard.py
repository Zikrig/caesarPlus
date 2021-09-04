def caesar_hard(message,key):
    message = message.lower() #Перевод сообщения и ключа в нижний регистр
    mes_fin=''
    key = key.lower()
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') #список-алфавит
    #al_plus=[]             #Массив констант для прибавления к буквам.
    #for i in range(len(alphabet)):
    #    al_plus.append(key[i%len(key)])
    for i in range(len(message)):                       #По сообщению
        if message[i] in alphabet:                      #Если буква включена в алфавит
            keynow=alphabet.index(key[i%len(key)])      #номер буквы ключа в алфавите
            mes_fin+=alphabet[(alphabet.index(message[i])+keynow)%33]   #в новое сообщение пишем букву от суммы
        else:
            mes_fin+=message[i]
    #print("алфавит")
    #print(alphabet)
    #print("алфавит,смещенный на %",key)
    #print(al_plus)
    return mes_fin