import datetime as dt

def day_of_week(day, month, year):
    d = dt.date(year, month, day)
    names = [
        "Понедельник","Вторник","Среда",
        "Четверг","Пятница","Суббота","Воскресенье"
    ]
    return names[d.weekday()]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calc_age(day, month, year):
    today = dt.date.today()
    birth = dt.date(year, month, day)
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    return age

DIGITS = {
    "0":["***","* *","* *","* *","***"],
    "1":["  *","  *","  *","  *","  *"],
    "2":["***","  *","***","*  ","***"],
    "3":["***","  *","***","  *","***"],
    "4":["* *","* *","***","  *","  *"],
    "5":["***","*  ","***","  *","***"],
    "6":["***","*  ","***","* *","***"],
    "7":["***","  *","  *","  *","  *"],
    "8":["***","* *","***","* *","***"],
    "9":["***","* *","***","  *","***"],
    " ":["   ","   ","   ","   ","   "],
}

def render_stars_date(day, month, year):
    s = f"{day:02d} {month:02d} {year:04d}"
    lines = ["","","","",""]
    for ch in s:
        pattern = DIGITS[ch]
        for i in range(5):
            lines[i] += pattern[i] + " "
    return "\n".join(lines)

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Введите число")

def main():
    day = read_int("День: ")
    month = read_int("Месяц: ")
    year = read_int("Год: ")
    try:
        dt.date(year, month, day)
    except:
        print("Некорректная дата")
        return
    print("День недели:", day_of_week(day, month, year))
    print("Год", "високосный" if is_leap_year(year) else "невисокосный")
    print("Возраст:", calc_age(day, month, year))
    print()
    print(render_stars_date(day, month, year))

if __name__ == "__main__":
    main()
