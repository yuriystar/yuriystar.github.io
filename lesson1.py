import random

ura_hp = int(input("здоровье Юры: "))
ura_dmg = int(input("дамаг Юры: "))
egor_hp = int(input("здоровье Егора: "))
egor_dmg = int(input("дамаг Егора: "))
r = 0
print("здоровье Юры\n", ura_hp, "дамаг Юры\n", ura_dmg)
print("здоровье Егора\n", egor_hp, "дамаг Егора", egor_dmg)

while ura_hp > 0 and egor_hp > 0:
    a = random.randint(0, 1)
    c = random.randint(0, 100)
    s = random.randint(0, 100)
    cubeu = random.randint(0, 100)
    cubee = random.randint(0, 100)
    r += 1
    print("round:", r)
    if a == 0:
        if c <= 25:
            cubeu = random.randint(0, 100)
            cubee = random.randint(0, 100)
            egor_hp -= (ura_dmg + ura_dmg*(100/cubeu)) 
            ura_hp -= (egor_dmg + egor_dmg*(100/cubee))
            if egor_hp == 0:
                break
        else:
            print("Уклонение успешно, попал в 25%")
            continue
    elif a == 1:
        if s <= 25:
            cubeu = random.randint(0, 100)
            cubee = random.randint(0, 100)
            ura_hp -= (egor_dmg + egor_dmg*(100/cubee))
            egor_hp -= (ura_dmg + ura_dmg*(100/cubeu))
            if ura_hp == 0:
                break
        else:
            print("Уклонение успешно, попал в 25%")
            continue
if ura_hp <= 0 and egor_hp <= 0:
       print("ничья")
elif egor_hp <= 0:
        print("Егор победил") 
elif ura_hp <= 0:
        print("Юра победил")   
   