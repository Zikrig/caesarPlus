from caesar_simple import caesar_simple as cs
from caesar_hard import caesar_hard as ch
print("Введите вашу фразу:")
phrase=input()

print("Anykey for simple. Enter for hard")
what=input()
if (what):
    print("Введите смещение:")
    shift=int(input())
    print("Введите ключ (НЕ ПОВТОРЯЙТЕ БУКВЫ):")
    key=input()
    print(cs(phrase,shift,key))
else:
    print("Введите ключ")
    key = input()
    print(ch(phrase, key))