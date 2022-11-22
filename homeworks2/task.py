# рассчитать расстояние между двумя точками на плоскости
import math

coordinate_x1 = int(input("Введите координату x1: "))
coordinate_y1 = int(input("Введите координату y1: "))
coordinate_x2 = int(input("Введите координату x2: "))
coordinate_y2 = int(input("Введите координату y2: "))

distance_between_points = math.sqrt((pow(coordinate_x2 - coordinate_x1, 2)) +
                                    (pow(coordinate_y2 - coordinate_y1, 2)))
print("Расстояние между точками: ", round(distance_between_points, 2))
