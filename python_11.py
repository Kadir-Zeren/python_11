sayi = 5
while sayi:
    print('I love Python')
    sayi -= 1

flag = True
times = 0
while flag:
    print('I love Python -')
    times +=1
    if times == 10:
        flag = False

number = 0
while number < 6:
    print(number)
    number += 1
print('now, number is bigger or equal to 6')

my_list=["a", "b", "c", "d", "e"]
a = 0
while a < len(my_list) :
    print('square of {} is : {}' .format(a, a ** 2))
    a+=1

'123' .isdigit()
'123a123' .isdigit()
'abc' .isdigit()

# yas = input('Yasinizi giriniz : ')
# while not yas.isdigit():
#     print('Girdigin ifade yas olamaz')
#     yas = input('Yasinizi giriniz : ')
# print('Evet girdigin deger yasin olabilir.')

# yas = input('Yasinizi giriniz : ')
# flag = True
# while flag:
#         if yas.isdigit():
#             print('Evet girdigin deger yasin olabilir.')
#             flag = False
#         else:
#             print('Girdigin ifade yas olamaz')
#             yas = input('Yasinizi giriniz : ')

# age = input("Enter your age please : ")

# while not age.isdigit():
#     print ("You entered incorrectly!")
#     age = input("Enter your age please : ")

# print("Great! You enter valid input : ", age)

# sayi = 50
# print("Let's play a game")
# while True:
#     girdi = int(input('Tuttugum sayiyi tahmin et : '))
#     if girdi == sayi:
#         print('Tebrik ederim Bildin')
#         break
#     elif girdi<sayi:
#         print('Biraz arttir')
#     else:
#         print('biraz azalt')

sayi = 50
print("Let's play a game")
tahmin_sayisi = 1
while tahmin_sayisi < 6:
    girdi = int(input('Tuttugum sayiyi tahmin et : '))
    if girdi == sayi:
        print('Tebrik ederim Bildin')
        break
    elif girdi < sayi:
        print('Biraz arttir')
    else:
        print('biraz azalt')
    print(tahmin_sayisi ,'kez tahmin ettiniz')
    if tahmin_sayisi == 5:
        print('Butun haklarını kullandin')