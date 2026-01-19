from .sorting import binary_insertion_sort

def generate_report1(disciplines):
    '''Генерация отчета 1: Полный список всех дисциплин'''
    print("\n" + "=" * 80)
    print("ГЕНЕРАЦИЯ ОТЧЕТА 1")
    print("Полный список всех дисциплин")
    print("Сортировка: семестр(↑), кафедра(↑), часы(↓)")
    print("=" * 80)
    
    # Определяем функцию ключа для сортировки
    def sort_key(disc):
        '''Ключ сортировки: семестр (по возрастанию), кафедра (по возрастанию), часы (по убыванию)'''
        return (disc.start_semester, disc.department, -disc.total_hours)
    
    # Сортируем дисциплины с помощью бинарных вставок
    sorted_disciplines = binary_insertion_sort(disciplines, sort_key)
    
    # Выводим результат на экран
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(sorted_disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    
    print("=" * 80)
    print(f"Всего дисциплин: {len(sorted_disciplines)}")
    return sorted_disciplines


def generate_report2(disciplines, assessment_type):
    '''Генерация отчета 2: Дисциплины с заданным видом отчётности'''
    print(f"\n" + "=" * 80)
    print("ГЕНЕРАЦИЯ ОТЧЕТА 2")
    print(f"Дисциплины с видом отчётности: '{assessment_type}'")
    print("Сортировка: длительность(↑), часы(↓)")
    print("=" * 80)
    
    # Фильтруем дисциплины по виду отчетности
    filtered_disciplines = []
    for disc in disciplines:
        if disc.assessment_type == assessment_type:
            filtered_disciplines.append(disc)
    
    # Проверяем, есть ли дисциплины с заданным видом отчетности
    if not filtered_disciplines:
        print(f"Нет дисциплин с видом отчётности '{assessment_type}'")
        return []
    
    # Определяем функцию ключа для сортировки
    def sort_key(disc):
        '''Ключ сортировки: длительность (по возрастанию), часы (по убыванию)'''
        return (disc.duration, -disc.total_hours)
    
    sorted_disciplines = binary_insertion_sort(filtered_disciplines, sort_key)
    
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(sorted_disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    
    print("=" * 80)
    print(f"Найдено дисциплин: {len(sorted_disciplines)}")
    
    return sorted_disciplines


def generate_report3(disciplines, n1, n2):
    '''Генерация отчета 3: Дисциплины с общим количеством часов от N1 до N2'''
    print(f"\n" + "=" * 80)
    print("ГЕНЕРАЦИЯ ОТЧЕТА 3")
    print(f"Дисциплины с количеством часов от {n1} до {n2}")
    print("Сортировка: кафедра(↑), часы(↓)")
    print("=" * 80)
    
    # Фильтруем дисциплины по диапазону часов
    filtered_disciplines = []
    for disc in disciplines:
        if n1 <= disc.total_hours <= n2:
            filtered_disciplines.append(disc)
    
    if not filtered_disciplines:
        print(f"Нет дисциплин с количеством часов от {n1} до {n2}")
        return []
    
    # Определяем функцию ключа для сортировки
    def sort_key(disc):
        '''Ключ сортировки: кафедра (по возрастанию), часы (по убыванию)'''
        return (disc.department, -disc.total_hours)
    
    # Сортируем отфильтрованные дисциплины с помощью бинарных вставок
    sorted_disciplines = binary_insertion_sort(filtered_disciplines, sort_key)
    
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(sorted_disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    
    print("=" * 80)
    print(f"Найдено дисциплин: {len(sorted_disciplines)}")
    return sorted_disciplines


def show_all_disciplines(disciplines):
    '''Вывод всех дисциплин без сортировки'''
    print("\n" + "=" * 80)
    print("ВСЕ ДИСЦИПЛИНЫ (БЕЗ СОРТИРОВКИ)")
    print("=" * 80)
    
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    
    print("=" * 80)
    print(f"Всего дисциплин: {len(disciplines)}")
