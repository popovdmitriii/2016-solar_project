# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            print(line)
            if len(line.split()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            else:
                if object_type == "planet":  ## FIXME: do the same for planet
                    planet = Planet()
                    parse_planet_parameters(line, planet)
                    objects.append(planet)
                else:
                    print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    type, R, color, m, x, y, Vx, Vy = line.split()
    R = int(R)
    m = float(m)
    x=float(x)
    y=float(y)
    Vx=float(Vx)
    Vy=float(Vy)
    star.type=type.lower() ## FIXME: not done yet...
    star.R=R
    star.color=color
    star.m=m
    star.x=x
    star.y=y
    star.Vx=Vx
    star.Vy=Vy 
    
    
    
    
    
    
    
    ## FIXME: 

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    type, R, color, m, x, y, Vx, Vy = line.split()
    R = int(R)
    m = float(m)
    x=float(x)
    y=float(y)
    Vx=float(Vx)
    Vy=float(Vy)
    planet.type=type.lower() ## FIXME: not done yet...
    planet.R=R
    planet.color=color
    planet.m=m
    planet.x=x
    planet.y=y
    planet.Vx=Vx
    planet.Vy=Vy
    
    
    
    
    


def write_space_objects_data_to_file(output_filename, space_objects):
   

    
    
    
    
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy, file=out_file)
            print('lfw')
            ## FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
