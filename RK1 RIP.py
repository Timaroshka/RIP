from operator import itemgetter


class Student:

    def __init__(self, id, name, rating, group_id):
        self.id = id
        self.name = name
        self.rating = rating
        self.group_id = group_id

class Group:

    def __init__(self, id, number):
        self.id = id
        self.number = number


class StudGroup:

    def __init__(self, group_id, student_id):
        self.group_id = group_id
        self.student_id = student_id


students = [
    Student(1, 'Абдуллаев', 14, 2),
    Student(2, 'Аникин', 2, 2),
    Student(3, 'Жидков', 13, 2),
    Student(4, 'Киреев', 3, 1),
    Student(5, 'Калашников', 31, 3),
    Student(6, 'Кокозов', 23, 3),
    Student(7, 'Зудин', 40, 2),
    Student(8, 'Рудзинский', 17, 1)
]

groups = [
    Group(1, 'Первая группа'),
    Group(2,'Вторая группа'),
    Group(3,'Третья группа')
]

studgroups = [
    StudGroup(1,4),
    StudGroup(1,8),
    StudGroup(2,1),
    StudGroup(2,2),
    StudGroup(2,3),
    StudGroup(2,7),
    StudGroup(3,5),
    StudGroup(3,6)
]


def main():

    # Один ко многим
    o_to_m = [(s.name, s.rating, c.number)
                   for s in students
                   for c in groups
                   if s.group_id == c.id]

    # Многие ко многим
    m_to_m_temp = [(g.number, sg.group_id, sg.student_id)
                         for g in groups
                         for sg in studgroups
                         if g.id == sg.group_id]

    m_to_m = [(s.name, student_name)
                    for student_name, student_id, group_id in m_to_m_temp
                    for s in students if s.id == group_id]

    print('Задание B1')
    res_B1 = list(filter(lambda x: x[0].startswith('А'), o_to_m))
    print(res_B1)
    
    print('\nЗадание B2')
    res_B2_unsorted = []
    for g in groups:
        t = list(filter(lambda i: i[2] == g.number, o_to_m))
        if len(t) > 0:
            count = [rating for _, rating, _ in t]
            count_min = min(count)
            res_B2_unsorted.append((g.number, count_min))

    res_B2 = sorted(res_B2_unsorted, key=itemgetter(1), reverse=False)
    print(res_B2)

    print('\nЗадание B3')
    res_B3 = sorted(m_to_m, key=itemgetter(0))
    print(res_B3)
    

if __name__ == '__main__':
    main()
