from datetime import date, datetime, timedelta


def get_birth_from_users(users):
    today = date.today()
    working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthdays_per_week = {day: [] for day in working_days}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        new_birthday = datetime(today.year, birthday.month, birthday.day).date() #змінюємо рік на 2023 щоб точно знати день в якому буде день народження
        if new_birthday - today < timedelta(days=0): #якщо день народження вже був то додаємо до року
            new_birthday = new_birthday.replace(year=today.year + 1)

        week_day = new_birthday.strftime('%A')
        print(week_day)

        if (new_birthday - today).days < 7:
            if week_day in ['Saturday', 'Sunday']:
                birthdays_per_week['Monday'].append(name)
            else:
                birthdays_per_week[week_day].append(name)

    return birthdays_per_week


result = get_birth_from_users([
    {'name': 'Misha', 'birthday': datetime(2004, 8, 31).date()},
    {'name': 'Bill Gates', 'birthday': datetime(1955, 8, 30).date()},
    {'name': 'Oleh', 'birthday': datetime(2000, 9, 2).date()},
    {'name': 'Ivanna', 'birthday': datetime(2001, 9, 4).date()},
    {'name': 'Katya', 'birthday': datetime(2001, 9, 15).date()}
])

print(result)

birth = datetime(2024, 6, 11).date()
day_of_week = birth.strftime("%A")
print(day_of_week)