# %% [markdown]
# ---
# title: 'Лабораторна робота №6. Функції'
# description:
#    Документ зроблено за допомогою [Quarto](https://quarto.org/)
# author: "Сідєльніков Даніїл, 2023"
# date: "10.05.2023"
# lang: ukr
# format:
#   html:
#     code-fold: true
#     toc: true # меню
#     toc_float: # спливаюче меню  
#       collapsed: true # авто
#       number_sections: true
# jupyter: python3
# ---

# %% [markdown]
# __Мета:__ _навчитися писати функції та користуватися ними_

# %% [markdown]
# ## Що ви будете вміти?
# * створювати користувацькі функції.
# * викликати користувацькі функції з параметрами та без.
# * освоїте обробку списків за допомогою функцій.

# %% [markdown]
# ## Створення функції

# %% [markdown]
# ### Завдання 1
# 
# Написати і протестувати функцію, яка приймає один аргумент (рік) і повертає `True`, якщо рік є високосним, або `False` інакше.
# 
# Основу функції вже закладено у коді в редакторі.
# 
# ::: callout-note
# ## Примітка
# Для вас підготовлено короткий тестуючий код, який можна використовувати для перевірки своєї функції.
# :::
# 
# У коді використовуються два списки - один із тестовими даними, інший - з очікуваними результатами. Код повідомить Вам, якщо якісь із Ваших результатів неправильні.

# %%
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# %% [markdown]
# ### Завдання 2 

# %% [markdown]
# Написати та протестувати функцію, яка приймає два аргументи (рік і місяць) і повертає кількість днів для даної пари рік-місяць (у той час, як тільки лютий чутливий до значення `year`, Ваша функція має бути універсальною).
# 
# Початок функції готовий. Тепер переконайте функцію повернути `None`, якщо її аргументи не мають сенсу.
# 
# Звичайно, Ви можете (і повинні) використовувати раніше написану та протестовану функцію (див. попередні лаб. роб.). Це може бути дуже корисним. Ми рекомендуємо використовувати список із зазначенням довжини місяців. Ви можете створити його всередині функції – цей трюк значно скоротить код.
# 
# Ми підготували тестуючий код. Розвійте його, щоб увімкнути більше тестових випадків.

# %%
def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

test_years = [1900, 2000, 2016, 1987, 2020, 2021, 2024]
test_months = [2, 2, 1, 11, 2, 2, 4]
test_results = [28, 29, 31, 30, 29, 28, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


# %% [markdown]
# ### Завдання 3
# 
# Написати та протестувати функцію, яка приймає три аргументи (рік, місяць та день місяця) та повертає відповідний день року або None, якщо якийсь із аргументів невірний.
# 
# Використовуйте раніше написані та протестовані функції. Додайте до коду свої власні тестові випадки.

# %%
def day_of_year(year, month, day):
    days = day
    for i in range(1, month):
        days += days_in_month(year, i)
    return days

dates = [(1900, 1, 1), (2000, 12, 31), (2016, 1, 1), (1987, 8, 12), (2020, 2, 29), (2021, 3, 1), (2024, 4, 30)]
days = []
for i in range(len(dates)):
    from datetime import date
    yr, mo, da = dates[i]
    days.append(date(yr, mo, da).timetuple().tm_yday)

for i in range(len(dates)):
    yr, mo, da = dates[i]
    print(yr, mo, da, "->", end="")
    result = day_of_year(yr, mo, da)
    if result == results[i]:
        print("OK")
    else:
        print("Failed")
        print(result, "!=", results[i])


# %% [markdown]
# ###  Завдання 4

# %% [markdown]
# Натуральне число є простим, якщо воно більше 1 і не має дільників, крім 1 і самого себе.
# 
# Важко? Зовсім ні. Наприклад, 8 не є простим числом, оскільки Ви можете розділити його на 2 та 4 (ми не можемо використовувати дільники, рівні 1 та 8, оскільки визначення забороняє це).
# 
# З іншого боку, 7 - просте число, оскільки ми можемо знайти йому підходящих дільників.
# 
# 
# Ваше завдання - написати функцію, що перевіряє, чи є число простим чи ні.
# 
# Функція:
# 
# * називається `is_prime`;
# * приймає один аргумент (значення для перевірки)
# * повертає `True`, якщо аргумент є простим числом, і `False` інакше.  
# 
# ::: callout-note
# ## Підказка
# Спробуйте розділити аргумент на всі наступні значення (починаючи з 2) і перевірте залишок - якщо він дорівнює нулю, Ваше число не може бути простим; добре подумайте, коли вам слід зупинити процес.
# :::
# 
# Якщо вам потрібно знайти квадратний корінь із будь-якого значення, Ви можете використовувати оператор `**`. Пам'ятайте: квадратний корінь `x` дорівнює $x^{0,5}$.
# 
# Доповніть код у редакторі.

# %%
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
                return False
    return True

for i in range(1, 50):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

# %% [markdown]
# ### Очікуваний вивод

# %% [markdown]
# `2 3 5 7 11 13 17 19`

# %% [markdown]
# ### Завдання 5

# %% [markdown]
# Витрата палива автомобіля можна висловити по-різному. Наприклад, у Європі він відображається як кількість витраченого палива на 100 кілометрів шляху.
# 
# У США він відображається як кількість миль, пройдених автомобілем під час витрачання одного галону палива.
# 
# Ваше завдання - написати дві функції, що конвертують л/100км в миль на галон, і навпаки.
# 
# Функції:
# 
# * названі `liters_100km_to_miles_gallon` та `miles_gallon_to_liters_100km` відповідно;
# * приймають один аргумент (значення, що відповідає їхнім іменам)  
# 
# Доповніть код у редакторі.
# 
# Запустіть свій код і перевірте, чи Ваш результат збігається з нашим.
# 
# Ось деяка інформація, яка може допомогти Вам:
# 
# * 1 американська мідя = 1609.344 метрів;
# * 1 американський галон = 3.785411784 літрів.

# %%
meters_in_mile = 1609.344
liters_in_gallon = 3.785411784

def liters_100km_to_miles_gallon(liters_per_100km):
    return 10e4 * liters_in_gallon / (liters_per_100km * meters_in_mile)

def miles_gallon_to_liters_100km(miles_per_gallon):
    return 10e4 * liters_in_gallon / (miles_per_gallon * meters_in_mile)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# %% [markdown]
# ### Очікуваний вивод

# %% [markdown]
# `60.31143162393162`  
# `31.36194444444444`  
# `23.52145833333333`  
# `3.9007393587617467`  
# `7.490910297239916`  
# `10.009131205673757`

# %% [markdown]
# ### Приклад 1

# %% [markdown]
# Давайте напишемо функцію оцінки індексу маси тіла (ІМТ, BMI).
# $$BMI = \frac{m}{h^2}$$
# тут $m$ -- маса у _кг_, $h$ -- зріст у _м_.

# %%
def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))

# %% [markdown]
# ### Ключове слово `None` 

# %% [markdown]
# Функція у попередньому прикладі виправдовує наші очікування, але вона дещо проста – вона припускає, що значення обох параметрів завжди мають сенс. Варто перевірити, чи заслуговують вони на довіру.
# 
# Давайте перевіримо їх обидва і повернемо `None`, якщо якесь з них виглядає підозріло.

# %%
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

# %% [markdown]
# ### Завдання 6 

# %% [markdown]
# Написати функцію, яка перевіряє, чи три сторони заданої довжини побудувати трикутник. Вона має повернути `True`, якщо сторони можуть утворити трикутник, і `False` в іншому випадку. У цьому випадку `is_a_triangle(a, b, c)` – гарна назва для такої функції.

# %%
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
print(is_a_triangle(1, 3, 3))
print(is_a_triangle(3, 1, 35))


# %% [markdown]
# ### Завдання 7 

# %% [markdown]
# Написати функцію `is_a_right_triangle(a, b, c)`, яка перевіряє, чи є трикутник зі сторонами `a`, `b`, `c` прямокутним. При цьому потрібно використати функцію `is_a_triangle(a, b, c)` з завдання 6. 

# %%
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    hypo = max(a, b, c)
    return hypo ** 2 == a ** 2 + b ** 2 + c ** 2 - hypo ** 2

print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 3))
print(is_a_right_triangle(1, 1, 3))
print(is_a_right_triangle(1, 1, 1))
print(is_a_right_triangle(12, 5, 13))


# %% [markdown]
# ## Завдання для самостіної роботи
# 
# 1. Виконати завдання 1-7 наведені вище у цьому зошиті.
# 
# 1. Створити файл __lab_6_StudentLastName.py__ з написаним кодом. 
# 
# 1. Закомітити файл у локальний репозиторій.
# 
# 1. Відправити ("запушити") поточну версію Git-проєкта у віддалений репозиторій на GitHub.
# 
# 1. Звіт має складатися з файлу (за основу взяти __цей Python-зошит__)  `lab_6_StudentLastName.ipynb`. (Можливі якісь додакові файли)

# %% [markdown]
# ## Контрольні запитання
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:0f067d0c-283b-459c-b507-194d9a1b0a65.png)
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:6af6fb73-7ba8-4b30-a0ad-bc2e74adae79.png)
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:081f0c11-7b4f-4a86-b1a2-69e001093c2a.png)
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:b47cf215-9ae4-48c4-892d-f45f446ac928.png)
# 

# %% [markdown]
# 1. ERROR
# 2. 2 
# 1
# 3. 2
# 3
# 4. 2
# 2

# %% [markdown]
# ## References

# %% [markdown]
# 1. [Anaconda (Python distribution)](https://uk.wikipedia.org/wiki/Anaconda_(Python_distribution))
# 2. [Conda](https://conda.io/en/latest/)
# 3. [Pro Git Book](https://git-scm.com/book/en/v2)
# 4. [OpenEDG Python Institute](https://pythoninstitute.org/)
# 5. [Cisco. Networking Academy](https://www.netacad.com/)
# 6. [Научно-издательская система Quarto](https://data-visualization-blog.netlify.app/posts/quarto/)


