# %% [markdown]
# ---
# title: 'Лабораторна робота №5. Списки'
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
# __Мета:__ _освоїти роботу зі списками_

# %% [markdown]
# ## Що ви будете вміти?
# * створювати та оперувати списками.
# * використовувати функції та методи `len()`, `append()`, `insert()`, `sort()`, `reverse()`.
# * виконувати зрізи та використовувати директиву `dell`.
# * використовувати оператори `in` та `not in`.
# * використовувати генератори списків.
# * створювати та оперувати багатовимірними списками

# %% [markdown]
# ## Створення та обробка списків

# %% [markdown]
# ### Завдання 1
# 
# Жив-був капелюх. У капелюсі не було кролика, натомість був список із п'яти чисел: `1`, `2`, `3`, `4` та `5`.
# 
# Ваше завдання:
# 
# * напишіть рядок коду, що пропонує користувачеві замінити число всередині списку цілим числом, введеним користувачем (крок 1)
# * напишіть рядок коду, який видаляє останній елемент зі списку (крок 2)
# * напишіть рядок коду, який друкує довжину існуючого списку (крок 3).  
# 
# Чи готові до цього випробування?

# %%
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

hat_list[len(hat_list)//2] = int(input("Enter a number: "))

# Step 2: write a line of code that removes the last element from the list.

hat_list.pop()

# Step 3: write a line of code that prints the length of the existing list.

print(len(hat_list))

print(hat_list)

# %% [markdown]
# ### Сортування списків 

# %% [markdown]
# ### Завдання 2
# 
# Написати програму сортування списку у порядку зростання методом бульбашки.

# %%
# Тут має бути Ваш код
# 1 реалізувати інтерактивне введення елементів масива
# 2 оптимізувати процедуру сортування

input_str = input("Enter a list of numbers: ")
list_of_numbers = input_str.split()

for i in range(len(list_of_numbers)):
    list_of_numbers[i] = int(list_of_numbers[i])

i = 0
while i < len(list_of_numbers) - 1:
    j = 0
    while j < len(list_of_numbers) - 1 - i:
        if list_of_numbers[j] > list_of_numbers[j+1]:
            list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
        j += 1
    i += 1

print(list_of_numbers)


# %% [markdown]
# ### Конструкції `in` та `not in`

# %% [markdown]
# ###  Завдання 3

# %% [markdown]
# Уявіть список - не дуже довгий, не дуже складний, просто звичайний список, що містить деякі цілі числа. Деякі з цих чисел можуть повторюватись, і це ключ до розгадки. Ми не хочемо повторень. Ми хочемо, щоб їх видалили.
# 
# Ваше завдання – написати програму, яка видаляє всі дублікати чисел зі списку. Ціль полягає в тому, щоб скласти список, в якому всі числа зустрічаються не більше одного разу.

# %%
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []
while len(my_list) > 0:
    item = my_list.pop()
    if item in my_list:
        continue
    else:
        unique_list.append(item)

unique_list.reverse()
my_list = unique_list

print("The list with unique elements only:")
print(my_list)

# %% [markdown]
# ## Багатовимірні списки. Генератори списків 

# %% [markdown]
# ### Приклад 

# %% [markdown]
# Уявіть, що Ви розробляєте програмне забезпечення автоматичної метеостанції. Прилад фіксує температуру повітря щогодини та робить це протягом місяця. Це дає Вам загалом 24 × 31 = 744 значення. Спробуємо скласти список, здатний зберігати ці результати.

# %%
temps = [[0.0 for h in range(24)] for d in range(31)]
# print(temps)

# %% [markdown]
# Визначимо середньомісячну полуденну температуру. Складіть усі 31 покази, записані опівдні, та поділіть отриману суму на 31. Ви можете припустити, що спочатку зберігається північна температура. Ось відповідний код:

# %%
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

# %% [markdown]
# ### Завдання 4

# %% [markdown]
# Погляньте на шахівницю. Кожне поле містить кілька індексів, які необхідно вказати для доступу до вмісту клітини:  
# ![image.png](attachment:2d271334-cc44-489c-a2cc-cb043c18f105.png)

# %% [markdown]
# Напишіть код, використоувуючи генератори списків, який створює матрицю 8х8 з пустими клітинками (пуста клітинка задається як "_") для задання шахівниці і розставте чотири тури по кутках шахівниці

# %%
chessboard = [['_'] * 8 for i in range(8)]

chessboard[0][0] = 'Rook'
chessboard[0][7] = 'Rook'
chessboard[7][0] = 'Rook'
chessboard[7][7] = 'Rook'

def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end='\t')
        print()

print_grid(chessboard)

# %% [markdown]
# ## Завдання для самостіної роботи
# 
# 1. Виконати завдання 1-4 наведені вище у цьому зошиті.
# 
# 1. Створити файл __lab_5_StudentLastName.py__ з написаним кодом. 
# 
# 1. Закомітити файл у локальний репозиторій.
# 
# 1. Відправити ("запушити") поточну версію Git-проєкта у віддалений репозиторій на GitHub.
# 
# 1. Звіт має складатися з файлу (за основу взяти __цей Python-зошит__)  `lab_5_StudentLastName.ipynb`. (Можливі якісь додакові файли)

# %% [markdown]
# ## Контрольні запитання
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:5d28959e-4e57-46f2-95a6-7ba12476be71.png)
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:79a1289e-9f0b-4b4c-a048-a35cf0ec2c94.png)
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:f3688bdd-8da1-40ab-b0f8-ecf197bfea84.png)
# 
# 1. Який вивод наступного фрагмента?  
# ![image.png](attachment:d4f43c8f-137a-4815-b776-49f3ea51c7e1.png)
# 

# %% [markdown]
# 1. "C"
# 
# 1. "B", "C"
# 
# 1. Нічого
# 
# 1. A, B, C

# %% [markdown]
# ## References

# %% [markdown]
# 1. [Anaconda (Python distribution)](https://uk.wikipedia.org/wiki/Anaconda_(Python_distribution))
# 2. [Conda](https://conda.io/en/latest/)
# 3. [Pro Git Book](https://git-scm.com/book/en/v2)
# 4. [OpenEDG Python Institute](https://pythoninstitute.org/)
# 5. [Cisco. Networking Academy](https://www.netacad.com/)
# 6. [Научно-издательская система Quarto](https://data-visualization-blog.netlify.app/posts/quarto/)


