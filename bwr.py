def BVR_simulation_model(time, amount):
    work_time = 6*60

    cbu_work_time = 0 #В часах

    max_length = 200
    length = 200
    square = 20
    depth = 3.2
    rock_mass = 3.4
    sum_rock_mass = 0
    shovel_volume = 7

    count_bang = 0

    amount_pdm = amount
    pdm = {'len_ride': 0, 'count_ride': 0, 'pdm_work_time': 0}
    pdms = [pdm.copy() for _ in range(amount)]

    #Граничные значения
    if time >= 2.5*60 and time < 6*60:
        cbu_work_time += 2.5
        return [count_bang, cbu_work_time, sum_rock_mass, pdms]
    elif time < 2.5*60:
        return [count_bang, cbu_work_time, sum_rock_mass, pdms]

    length -= depth
    count_bang += 1
    rock_volume = depth * square * rock_mass
    time -= work_time
    time -= 2*60
    cbu_work_time += 2.5
    work_time = work_time if time > work_time else time #Если время на следующую смену меньше 6 часов, ставим по факту

    # Работаем пока есть время, пока выработка не закончилсь
    while time > 0 and length > 0:

        # Если есть порода и время, вывозим
        while rock_volume > 0 and work_time > 0:
            for i in range(amount): #ПДМ собирают руду, если руда заканчивается, ПДМ прекращают работу.
                if rock_volume == 0: break
                vol = shovel_volume if rock_volume > shovel_volume else rock_volume #Если руды много, добавляем обьем ковша, иначе остатки
                rock_volume -= vol
                sum_rock_mass += vol
                pdms[i]['count_ride']+=1
                pdms[i]['len_ride']+= (max_length - length) * 2 #Считаем по текущей глубине метры проходки
                pdms[i]['pdm_work_time'] += 10
            work_time-=10

        # Если осталось время, выполняем бурение - закладку - взрыв (Если на последнюю смену прихоится меньше 6 часов, взрыв не считаем)
        # work_time == time, только в том случае, если смена последняя по времени, при этом ПДМ не работали
        if work_time >= 3.5 * 60 and work_time != time or work_time == 6*60:
            length -= depth
            count_bang += 1
            rock_volume = depth * square * rock_mass
            cbu_work_time += 2.5
        elif work_time == time and time >= 2.5: #Считаем, если СБУ успела сделать свою работу в смену, на которой закончилось время
            cbu_work_time += 2.5

        # Обновляем смену, уменьшаем время, пересменка
        work_time = 6*60
        time -= work_time
        time -= 2*60

        work_time = work_time if time > work_time else time #Если время на следующую смену меньше 6 часов, ставим по факту

    return [count_bang, cbu_work_time, sum_rock_mass, pdms]

model = None
sum_count_bang = 0
sum_len_ride = 0
cbu = 0
pdm = 0
mass = 0

for i in range(1, 5):
    print(f'Выработка {i}')
    time = int(input('Введите количество часов: ')) * 60
    amount = int(input('Количество ПДМ: '))
    model = BVR_simulation_model(time, amount)

    print(f'Количество взрывов в выработке {i}: {model[0]}')
    sum_count_bang+=model[0]

    for j in range(0, amount):
        print(f"Метры проходки в выработке {i}, ПДМ под номером {j + 1}: {round(model[3][j]['len_ride'], 1)}")
        sum_len_ride+=round(model[3][j]['len_ride'], 1)

    print(f'Полезное время работы СБУ: {model[1]}')
    cbu+=model[1]

    for j in range(0, amount):
        print(f"Полезное время работы ПДМ под номером {j + 1}: {round(model[3][j]['pdm_work_time']/60, 1)}")
        pdm+=round(model[3][j]['pdm_work_time'], 1)

    print(f'Масса добытой руды: {round(model[2],2)}')
    mass+=model[2]

    for j in range(0, amount):
        print(f"Количество рейсов ПДМ под номером {j + 1}: {model[3][j]['count_ride']}")

    print('\n')

print(f'Общее количество взрывов: {sum_count_bang}')
print(f'Метры проходки в выработке: {sum_len_ride}')
print(f'Суммарное время работы СБУ: {cbu} и ПДМ: {pdm}')
print(f'Масса добытой руды: {round(mass,2)}')
