def simple_gen():
    yield "0"
    yield "yas 22"
    yield "yaslanıyoruz ve zaman kalmadı."


for i in simple_gen():
    print(i)

#hangi piksel 5,1,1
# hızlandırılmış kod ama okuması zor.
CORRECT_COMBO = (5,1,1)
found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo:{}'.format((c1, c2, c3)))
                found_combo = True
                break

#hangi piksel 3,6,1
# okuması kolay. fonksiyonlaştırılması kolay
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

CORRECT_COMBO = (3,6,1)
for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)))
        break
















