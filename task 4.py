import random

class Group:
    """
    A class to represent the study group.

    Attributes:
    number_group (str): The group number.
    """
    def __init__(self, number_group):
        self.number_group = number_group

class Teacher:
    """
    A class to represent the teacher.

        Attributes:
            name_teacher (str): The name of the teacher.
            course (str): The name of the course.
            course_teacher (dict): The relationship between the course and the name of the teacher.
    """
    course_teacher = {}

    def __init__(self, name_teacher, course):
        self.name_teacher = name_teacher
        self.course = course
        self.course_teacher[course] = name_teacher

class Schedule:
    """
    A class for drawing up a study schedule.

        Attributes:
            time (dict): The start time of classes for each couple.
            schedule (dict): The schedule of classes by day of the week.
            course (str): The name of the course.
            count_course (int): The number of classes in this course.
    """
    time = {
        1: '9:00 - 10:30',
        2: '10:50 - 12:25',
        3: '12:40 - 14:15',
        4: '14:30 - 16:05',
        5: '16:20 - 17:55'
    }
    schedule = {'Понедельник': [],
                'Вторник': [],
                'Среда': [],
                'Четверг': [],
                'Пятница': [],
                'Суббота': []
    }

    def __init__(self, course, count_course):
        self.course = course
        self.count_course = count_course

    def add_course(self, course, count_course):
        """
        Adds classes for the course on random days of the week.
        """
        while count_course != 0:
            day = random.choice(['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'])
            Schedule.schedule[day].append(course)
            count_course -= 1

    def get_schedule(self):
        """
        Displays the class schedule.
        """
        for day in Schedule.schedule:
            print(day)
            time_lesson = 1
            for lesson in range(len(Schedule.schedule[day])):
                if time_lesson <= 5:
                    print(f'{Schedule.time[time_lesson]} {Schedule.schedule[day][lesson]}'
                          f'{Teacher.course_teacher[Schedule.schedule[day][lesson]]}')
                else:
                    break
                time_lesson += 1




with open('course.txt', 'r',encoding='utf8') as file:
    lines = file.readlines()

for line in lines:
    data = line.split(',')
    teacher = Teacher(data[1], data[0])
    schedule_group = Schedule(data[0], data[2])
    schedule_group.add_course(str(data[0]), int(data[2]))

schedule_group.get_schedule()

