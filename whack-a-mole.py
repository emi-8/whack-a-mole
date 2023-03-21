import random
import time 


def mole(r):
    m = ''
    n = ''

    for i in range(8):
        hole = '.'
        if i == r:
            hole = '0'
            m = m + '_' + hole + '_'
        else:
            m = m + '_' + hole + '_'
        n = n + '[' + str(i) + ']'
    print(m)
    print(n)


def play():
    print('======== START! ========')
    start_time = time.time()
    num = 10
    count = 0
    
    while num > 0:
        r = random.randint(0, 7)
        mole(r)
        hit = input('Where is a mole? ')
        if int(hit) == r:
            print("HIT!\n")
            count += 1
        else:
            print("MISS\n")
        num -= 1
    t = int(time.time() - start_time)

    # calculate bonus
    bonus = 0
    if t < 60:
        bonus = 60 - t

    print('======== Finish! ========\n')
    print(f'TIME {t} SEC')
    print(f'HIT {count} X BONUS {bonus}')
    print('SCORE', count * bonus)


play()






