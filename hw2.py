import csv


def get_info():
    """Возвращает список департаментов и список словарей в формате OrderedDict"""
    departments = []
    employees_info = []
    with open('./Corp Summary.csv', 'r', newline='\r\n', encoding='utf-8') as csvfile:
        summary = csv.DictReader(csvfile, delimiter=';')
        for row in summary:
            departments.append(row['Департамент'])
            employees_info.append(row)

    return list(set(departments)), employees_info


def hierarchy():
    """Выводит иерархию команд."""
    departments, employees_info = get_info()

    for name in departments:
        teams = []
        for employee in list(filter(lambda item: item['Департамент'] == name, employees_info)):
            teams.append(employee['Отдел'])
        print_teams = ', '.join(list(set(teams)))
        print(f'Департамент {name} содержит отделы: {print_teams}\n')


def make_report():
    """Формирует отчет по департаментам."""
    departments, employees_info = get_info()

    department_reports = []
    for name in departments:
        department = {'Департамент': name}
        count = 0
        min_salary = 999999999
        max_salary = 0
        sum_salary = 0
        for employee in list(filter(lambda item: item['Департамент'] == name, employees_info)):
            salary = int(employee['Оклад'])
            count += 1
            sum_salary += salary
            if salary < min_salary:
                min_salary = salary
            if salary > max_salary:
                max_salary = salary

        department['Численность'] = count
        department['Разброс зарплат'] = f'{min_salary} - {max_salary}'
        department['Средняя запрлата'] = round(sum_salary / count, 3)
        department_reports.append(department)

    return department_reports


def print_report():
    """Сохраняет отчет по департаментам."""
    department_reports = make_report()

    for report in department_reports:
        for k, v in report.items():
            print(k, ': ', v)
        print('\n')


def save_report():
    """Сохраняет отчет по департаментам."""
    department_reports = make_report()

    with open('report.csv', 'w', newline='\r\n', encoding='utf-8') as csvfile:
        fieldnames = ['Департамент', 'Численность', 'Разброс зарплат', 'Средняя запрлата']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()
        for row in department_reports:
            writer.writerow(row)


if __name__ == '__main__':
    while True:
        print('Меню:\n'
              '1. Вывести иерархию команд.\n'
              '2. Вывести сводный отчёт по департаментам. \n'
              '3. Сохранить сводный отчёт по департаментам. \n'
              '4. Выход.\n\n'
              'Введите номер нужного действия.\n')
        choice = input()
        if choice == '1':
            hierarchy()
        elif choice == '2':
            print_report()
        elif choice == '3':
            save_report()
        elif choice == '4':
            break
        else:
            print('Введите корректный номер.')
