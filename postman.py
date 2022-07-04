# Первая задача
point_1 = (0, 2)
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)

min_dist = 0
best_route = []

route = []
distance = 0


def calc_dist(point_1, point_2):

    #Функция - калькулятор расстояния

    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def function(coord0, route, distance, points):

    # Функция запускает цикл перебора с рекурсией

    global q
    global min_dist
    global best_route

    for point in points[1:]:

        if point not in route:
            distance += calc_dist(coord0, point)
            route.append(point)

            if len(route) == 4:
                # Проверка последнего пункта
                distance += calc_dist(point, points[0])

                if min_dist == 0 or distance < min_dist:
                    # Проверка минимального расстояния
                    min_dist = distance
                    best_route = route.copy()

            function(point, route, distance, points[:points.index(point)] + points[points.index(point) + 1:])

            # отменяем последние изменения
            route.remove(point)
            distance = distance - calc_dist(coord0, point)


function((0, 2), route, distance, [point_1, point_2, point_3, point_4, point_5])


# Вывод
first_step = calc_dist(point_1, best_route[0])
sec_step = first_step + calc_dist(best_route[0], best_route[1])
third_step = sec_step + calc_dist(best_route[1], best_route[2])
fourth_step = third_step + calc_dist(best_route[2], best_route[3])
last_step = fourth_step + calc_dist(best_route[3], point_1)

print(f'{point_1} -> {best_route[0]}[{first_step}] -> '
      f'{best_route[1]}[{sec_step}] -> '
      f'{best_route[2]}[{third_step}] -> '
      f'{best_route[3]}[{fourth_step}] -> '
      f'{point_1}[{last_step}] = '
      f'{min_dist}')
