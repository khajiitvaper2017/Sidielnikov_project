# %% [markdown]
# ---
# title: "Лабораторна робота №4. Логічні значення. Умовне виконання. Цикли"
# description:
#   Документ зроблено в [Quarto](https://quarto.org/)
# author: "Сідєльніков Даніїл, 2023"
# date: "09.22.2023"
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
# __Мета:__ _освоїти роботу з логічними змінними, операторами розгалуження та операторами циклів_

# %% [markdown]
# ## Оператори порівняння

# %% [markdown]
# ### Завдання 1
# 
# Використовуючи один з операторів порівняння в Python, напишіть просту дворядкову програму, яка приймає як вхідні дані параметр `n`, який є цілим числом, і друкує `False`, якщо `n` менше `100` і `True`, якщо `n` більше або дорівнює `100`.  
# Не створюйте жодних блоків `if`. Протестуйте свій код, використовуючи дані, надані нижче.

# %%
n = int(input())

print((True, False)[n < 100])

# %% [markdown]
# __Тестові дані__  
# 
# Приклад введення: `55`
# 
# Очікуваний вивід: `False`
# 
# 
# Приклад введення: `100`
# 
# Очікуваний вивід: `True`
# 
# 
# Приклад введення: `-5`
# 
# Очікуваний вивід: `False`

# %% [markdown]
# ### Завдання 2
# 
# Написати програму визначення найбільшого з двох дійсних чисел, використовуючи констуркцію `if-else`.

# %%
num1 = float(input())
num2 = float(input())

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print('Numbers are equal')

# %% [markdown]
# ###  Завдання 3

# %% [markdown]
# ## Конструкції `if-else` та `if-elif-else`

# %% [markdown]
# Спатифіллум, більш відомий як лілія світу або біле вітрило, є одним з найпопулярніших кімнатних рослин, що фільтрують шкідливі токсини з повітря. Деякі з токсинів, які він нейтралізує, включають бензол, формальдегід та аміак.
# 
# Уявіть, що ваша комп'ютерна програма любить ці рослини. Щоразу, коли вона отримує введення у вигляді слова Spathiphyllum, вона мимоволі вигукує в консоль наступний рядок: "Spathiphyllum is the best plant ever!"
# 
# 
# Напишіть програму, яка використовує концепцію умовного виконання, приймає рядок як вхідні дані та:
# 
# * виводить на екран пропозицію "Yes - Spathiphyllum is the best plant ever!", якщо введений рядок - "Spathiphyllum" (верхній регістр)
# * друкує "No, I want a big Spathiphyllum!", якщо введений рядок - "spathiphyllum" (у нижньому регістрі)
# виводить "Spathiphyllum! Not [input]!" в іншому випадку.  
# __Примітка.__ [input] - це рядок, прийнятий як вхідний.
# 
# Протестуйте свій код, використовуючи дані, які надано нижче.

# %% [markdown]
# __Тестові дані__

# %% [markdown]
# Приклад введення: `spathiphyllum`
# 
# Очікуваний вивід: `No, I want a big Spathiphyllum!`
# 
# 
# Приклад введення: `pelargonium`
# 
# Очікуваний вивід: `Spathiphyllum! Not pelargonium!`
# 
# 
# Приклад введення: `Spathiphyllum`
# 
# Очікуваний вивід: `Yes - Spathiphyllum is the best plant ever!`

# %%
text = input()

if text == 'spathiphyllum':
    print('No, I want a big Spathiphyllum!')
elif text == 'pelargonium':
    print('Spathiphyllum! Not pelargonium!')
elif text == 'Spathiphyllum':
    print('Yes - Spathiphyllum is the best plant ever!')



# %% [markdown]
# ### Завдання 4

# %% [markdown]
# Жила-була земля -- земля молока та меду, населена щасливими та заможними людьми. Звісно, люди платили податки – їх щастя мало межі. Найважливіший податок, так званий податок на доходи фізичних осіб (скорочено ПДФО), повинен був сплачуватись один раз на рік та оцінювався за таким правилом:
# 
# * якщо дохід громадянина не перевищував 85528 талерів, податок становив 18% від доходу мінус 556 талерів і 2 центи (це було те, що вони називали податковими пільгами)  
# * якщо дохід був вищим за цю суму, податок становив 14 839 талерів 2 центи плюс 32% надлишку понад 85 528 талерів.  
# Ваше завдання – написати калькулятор податків.
# 
# Він повинен приймати одне значення з плаваючою комою: дохід.
# Потім він має вивести розрахований податок, заокруглений до повних талерів. Є функція з ім'ям `ound()`, яка виконуватиме заокруглення за вас -- ви знайдете її в скелетному коді нижче.  
# __Примітка:__ ця щаслива країна ніколи не повертала своїм громадянам грошей. Якщо розрахований податок був меншим за нуль, це означало б тільки повну відсутність податку (податок дорівнював нулю). Врахуйте це під час розрахунків.
# 
# Подивіться на код нижче - він зчитує лише одне вхідне значення та виводить результат, тому вам потрібно завершити його деякими розумними обчисленнями.
# 
# Протестуйте свій код, використовуючи тестові дані, наведені нижче.

# %%
income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = (income * 0.18) - 556.02
else:
    tax = 14839.02 + ((income - 85528) * 0.32)

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# %% [markdown]
# __Тестові дані__
# 
# Очикуваний вивод:
# 
# Приклад введення: `10000`
# 
# Очікуваний вивід: `The tax is: 1244.0 thalers`
# 
# Приклад введення: `100000`
# 
# Очікуваний вивід: `The tax is: 19470.0 thalers`
# 
# Приклад введення: `1000`
# 
# Очікуваний вивід `The tax is: 0.0 thalers`
# 
# Приклад введення: `-100`
# 
# Очікуваний вивід `The tax is: 0.0 thalers`

# %% [markdown]
# ### Завдання 5

# %% [markdown]
# Як ви, напевно, знаєте, з деяких астрономічних причин роки можуть бути високосними або звичайними. Перші тривають 366 днів, а другі – 365 днів.
# 
# З моменту введення григоріанського календаря (1582) для визначення року використовується наступне правило:
# 
# * якщо номер року не ділиться на чотири, це звичайний рік;
# * в іншому випадку, якщо номер року не ділиться на 100, це високосний рік;
# * в іншому випадку, якщо номер року не ділиться на 400, це звичайний рік;
# * інакше це високосний рік.  
# 
# Подивіться на код у редакторі -- він читає лише номер року і має бути доповнений інструкціями, що реалізують тест, який описаний вище.
# 
# Код має виводити одне з двох можливих повідомлень: `Leap year` або `Common year`, залежно від введеного значення.
# 
# Було б добре перевірити, чи належить введений рік до григоріанської ери, і вивести попередження інакше: `Not within the Gregorian calendar period.`  
# 
# __Підказка:__ використовуйте оператори `!=` та `%`.
# 
# Протестуйте свій код, використовуючи надані нами дані.

# %%
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")

# %% [markdown]
# __Тестові дані__
# 
# Приклад введення: `2000`
# 
# Очікуваний вивід: `Leap yea`r
# 
# Приклад введення: `2015`
# 
# Очікуваний вивід: `Common yea`r
# 
# Приклад введення: `1999`
# 
# Очікуваний вивід: `Common yea`r
# 
# Приклад введення: `1996`
# 
# Очікуваний вивід: `Leap yea`
# 
# Приклад введення: `1580`
# 
# Очікуваний вивід: `Not within the Gregorian calendar period`вивід

# %% [markdown]
# ## Організація циклів за допомогою `while`

# %% [markdown]
# ### Завдання 6 

# %% [markdown]
# Молодший чарівник вибрав таємне число. Він сховав його в змінну з ім'ям `secret_number`. Він хоче, щоб кожен, хто запускає його програму, грав у гру _Вгадай секретний номер_ і вгадав, яке число він вибрав для них. Ті, хто не вгадає число, назавжди застрянуть у нескінченній петлі! На жаль, він не знає, як завершити код.
# 
# Ваше завдання допомогти фокуснику доповнити код у редакторі таким чином, щоб код:
# 
# * попросив користувача ввести ціле число;
# * використовувавши цикл `while`;
# * перевірити, чи включає введене користувачем число з числом, вибраним фокусником. Якщо число, обране користувачем, відрізняється від секретного числа чарівника, користувач повинен побачити повідомлення `"Ха-ха! Ви застрягли у моїй петлі!"` і отримати запит на повторне введення числа. Якщо число, введене користувачем, співпадає з числом, вибраним фокусником, число має бути надруковане на екрані, і фокусник повинен вимовити наступне слово: `«Молодець, магле! Тепер ти вільний»`. 
# 
# Чарівник розраховує на Вас! Не розчаровуйте його.
# 
# 
# ДОДАТКОВА ІНФОРМАЦІЯ
# 
# До речі, подивитесь на функцію `print()`. Те, як ми це використовували тут, називається багаторядковим друком. Ви можете використовувати три кавички для друку рядка в кількох рядках, щоб текст був легшим для читання, або для створення спеціального текстового дизайну. Поекспериментуйте з цим.

# %%
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Введіть ціле число: "))
while number != secret_number:
    print("Ха-ха! Ви застрягли у моїй петлі!")
    number = int(input("Введіть ціле число: "))
print("Вітаю! Ви вгадали моє число!")

# %% [markdown]
# ## Організація циклів за допомогою `for` 

# %% [markdown]
# ### Завдання 7 

# %% [markdown]
# Ви знаєте, що таке Міссісіпі? Ну, це назва одного зі штатів та річок у Сполучених Штатах. Довжина річки Міссісіпі становить близько 2340 миль, що робить її другою за довжиною річкою у Сполучених Штатах (найдовшою з них є річка Міссурі). Це так багато, що одній краплі води потрібно 90 днів, щоб пройти весь її шлях!
# 
# Слово Міссісіпі також використовується для дещо іншої мети: для рахунку Міссісіпі.
# 
# Якщо ви не знайомі з цією фразою, ми можемо пояснити вам, що вона означає: вона використовується для підрахунку секунд.
# 
# Ідея полягає в тому, що додавання слова Міссісіпі до числа при підрахунку секунд вголос змушує рахунок бути хронологічно точніше, і, отже, вимова "один Міссісіпі, два Міссісіпі, три Міссісіпі" займе приблизно три секунди! Рахунок Міссісіпі часто використовують діти, які грають у хованки, щоб переконатися, що той, хто шукає чесно, підраховує час.
# 
# Ваше завдання тут дуже просте: напишіть програму, яка використовує цикл `for` для «рахунку Міссісіпі» до п'яти. Порахувавши до п'яти, програма повинна вивести на екран фінальне повідомлення `"Ready or not, here I come!"`
# 
# Використовуйте код, який ми надали у редакторі.
# 
# ДОДАТКОВА ІНФОРМАЦІЯ
# 
# Зверніть увагу, що код редактора містить два елементи, які можуть бути наразі вам не зовсім зрозумілі: оператор `import time` і метод `sleep()`. Ми незабаром про них поговоримо.
# 
# Наразі ми просто хотіли, щоб ви знали, що ми імпортували модуль `time` і використовували метод `sleep()` для припинення виконання кожної наступної функції `print()` всередині циклу `for` на одну секунду, щоб повідомлення, яке виводиться на консоль, було схоже на фактичний підрахунок.

# %%
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

for i in range(1, 6):
    time.sleep(1)
    print(i, "Mississippi")

# Write a print function with the final message.

print("Ready or not, here I come!")

# %% [markdown]
# _Очикуваний вивід_
# 
# `1 Mississippi`  
# `2 Mississippi`  
# `3 Mississippi`  
# `4 Mississippi`  
# `5 Mississippi`

# %% [markdown]
# ## Оператори `break` і `continue` 

# %% [markdown]
# ### Завдання 8 

# %% [markdown]
# Оператор `break` використовується для завершення/виходу з циклу.
# 
# Розробте програму, яка використовує цикл `while` і постійно просить користувача ввести слово, якщо користувач не вводить `"chupacabra"` як секретне вихідне слово, і в цьому випадку повідомлення `"You've successfully left the loop."` має бути виведений на екран, а цикл має завершитись.
# 
# Не друкуйте жодне із введених користувачем слів. Використовуйте концепцію умовного виконання та інструкцію `break`.

# %%
secret_word = "chupacabra"
while True:
    word = input("Введіть слово: ")
    if word == secret_word:
        break

print("You have successfully left the loop.")

# %% [markdown]
# ### Завдання 9

# %% [markdown]
# Оператор `continue` використовується для пропуску поточного блоку та переходу до наступної ітерації без виконання операторів усередині циклу.
# 
# Його можна використовувати з циклами `while` та `for`.
# 
# Ваше завдання тут особливе: Ви повинні створити пожирача голосних! Напишіть програму, яка використовує:
# 
# * цикл `for`;
# * концепцію умовного виконання (`if-elif-else`)
# * оператор `continue`.  
# 
# Ваша програма повинна:
# 
# * попросити користувача ввести слово;
# * використовувати `user_word = user_word.upper()`, щоб перетворити слово, введене користувачем, у верхній регістр; ми  поговоримо про рядкові методи та метод `upper()` у наступних лекціях;
# * використовуйте умовне виконання та оператор `continue`, щоб "з'їсти" наступні голосні `A`, `E`, `I`, `O`, `U` у введеному слові;
# * виведіть на екран нез'їдені літери, кожну в окремому рядку.
# 
# Протестуйте свою програму з даними, які надані нижче.

# %%
# Prompt the user to enter a word
# and assign it to the user_word variable.

# for letter in user_word:
    # Complete the body of the for loop.

user_word = input("Введіть слово: ")

user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)

# %% [markdown]
# __Тестові дані__
# 
# Зразкове введення: `Gregory`
# 
# Очікуваний вивід:
# 
# `G`   
# `R`   
# `G`   
# `R`   
# `Y`   
# 
# Зразкове введення: `abstemious`
# 
# Очікуваний вивід:
# 
# `B`  
# `S`  
# `T`  
# `M`  
# `S`  
# 
# Зразкове введення: `IOUEA`
# 
# Очікуваний вивід:
# 
# ` `

# %% [markdown]
# ### Завдання 10

# %% [markdown]
# Ваше завдання тут ще особливіше, ніж раніше: Ви повинні переробити (потворного) пожирача голосних із попереднього завдання і створити кращого, покращеного (красивого) пожирача голосних! Напишіть програму, яка використовує:
# 
# * цикл `for`;
# * концепцію умовного виконання (`if-elif-else`)
# * оператор `continue`.
# 
# Ваша програма повинна:
# 
# * попросити користувача ввести слово;
# * використовувати `user_word = user_word.upper()`, щоб перетворити слово, введене користувачем, у верхній регістр; * використовувати умовне виконання та оператор `continue` , щоб "з'їсти" наступні голосні `A, E, I, O, U` від введеного слова;
# * присвоїти нез'їдені літери змінної `word_without_vowels` та вивести змінну на екран.
# 
# Подивіться код нижче. Ми створили `word_without_vowels` і надали йому порожній рядок. Використовуйте операцію конкатенації, щоб попросити Python об'єднати вибрані літери у довший рядок у наступних ітераціях циклу та призначити її змінною `word_without_vowels`.
# 
# Протестуйте свою програму з даними, які ми надали.

# %%
word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.


# for letter in user_word:
    # Complete the body of the loop.

# Print the word assigned to word_without_vowels.

user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter != "A" and letter != "E" and letter != "I" and letter != "O" and letter != "U":
        word_without_vowels += letter
print(word_without_vowels)

# %% [markdown]
# __Тестові дані__
# 
# Зразкове введення:` Gregory`
# 
# Очікуваний вивід:
# 
# `GRGRY`
# 
# Зразкове введення: abstemious
# 
# Очікуваний вивід:
# 
# `BSTMS`
# 
# Зразкове введення: `IOUEA`
# 
# Очікуваний вивід:
# 
# ` `

# %% [markdown]
# ### Завдання 11

# %% [markdown]
# Послухайте цю історію: хлопчик та його батько, програміст, грають із дерев'яними кубиками. Вони будують піраміду (рис. 1).
# 
# Їхня піраміда трохи дивна, тому що насправді це стіна у формі піраміди -- вона плоска. Піраміда складається за одним простим принципом: кожен нижній шар містить на один блок більше, ніж шар вище.
# 
# На рис. 1 показано правило, що використовується будівельниками:

# %% [markdown]
# ![Рис. 1](attachment:a41b02e3-9575-4e30-949d-2a3d3a0cdd64.png)

# %% [markdown]
# Ваше завдання – написати програму, яка зчитує кількість блоків, що є у будівельників, та виводить висоту піраміди, яку можна побудувати з цих блоків.
# 
# __Примітка:__ висота вимірюється кількістю повністю завершених шарів –- якщо будівельники не мають достатньої кількості блоків та не можуть завершити наступний шар, вони негайно закінчують свою роботу.
# 
# Протестуйте свій код, використовуючи надані нами дані.

# %%
num_of_blocks = int(input("Enter the number of blocks: "))

height = 0

while num_of_blocks > 0:
    if num_of_blocks >= height + 1:
        height += 1
        num_of_blocks -= height
    else:
        break
print("The height of the pyramid:", height)

# %% [markdown]
# __Тестові дані__
# 
# Зразкове введення: `6`
# 
# Очікуваний вивід: `The height of the pyramid: 3`
# 
# Зразкове введення: `20`
# 
# Очікуваний вивід: `The height of the pyramid: 5`
# 
# Зразкове введення: `1000`
# 
# Очікуваний вивід: `The height of the pyramid: 44`
# 
# Зразкове введення: `2`
# 
# Очікуваний вивід: `The height of the pyramid: 1`

# %% [markdown]
# ### Завдання 12

# %% [markdown]
# 1937 року німецький математик Лотар Коллатц сформулював інтригуючу гіпотезу (вона досі не доведена), яку можна описати так:
# 
# * візьміть будь-яке невід'ємне та ненульове ціле число та назвіть його `c0`;
# * якщо воно парне, обчисліть нове `c0` як `c0÷2`;
# * в іншому випадку, якщо воно непарне, висиліть нове `c0 `як `3 × c0 + 1`;
# * якщо `c0 ≠ 1`, поверніться до пункту 2.
# 
# Гіпотеза свідчить, що незалежно від початкового значення `c0` воно завжди дорівнюватиме `1`.
# 
# Звичайно, використання комп'ютера для доведення гіпотези для будь-якого натурального числа -- надзвичайно складне завдання (для цього може знадобитися навіть штучний інтелект), але ви можете використовувати Python для перевірки деяких окремих чисел. Можливо, Ви навіть знайдете те, що спростує гіпотезу.
# 
# 
# Напишіть програму, яка зчитує одне натуральне число і виконує вказані вище кроки до тих пір, поки `c0` залишається відмінним від `1`. Ми також хочемо, щоб ви підрахували кроки, необхідні для досягнення мети. Ваш код також повинен виводити усі проміжні значення `c0`.
# 
# Підказка: найважливіша частина проблеми –- як перетворити ідею Коллатца на цикл `while` – це ключ до успіху.
# 
# Протестуйте свій код, використовуючи надані нами дані.

# %%
c0 = int(input("Enter a number: "))

steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3 * c0 + 1
    print(int(c0))
    steps += 1
print("steps =", steps)

# %% [markdown]
# __Тестові дані__
# 
# Приклад введення: `15`
# 
# Очікуваний вивід:
# 
# `46`  
# `23`  
# `70`  
# `35`  
# `106`  
# `53`  
# `160`  
# `80`  
# `40`  
# `20`  
# `10`  
# `5`  
# `16`  
# `8`  
# `4`  
# `2`  
# `1`  
# `steps = 17`
# 
# Приклад введення: `16`
# 
# Очикуваний вивід: 
# 
# `8`  
# `4`  
# `2`  
# `1`  
# `steps = 4`
# 
# Приклад введення: `1023`
# 
# Очікуваний вивід:
# 
# `3070`  
# `1535`  
# `4606`  
# `2303`  
# `6910`  
# `3455`  
# `10366`  
# `5183`  
# `15550`  
# `7775`  
# `23326`  
# `11663`  
# `34990`  
# `17495`  
# `52486`  
# `26243`  
# `78730`  
# `39365`  
# `118096`  
# `59048`  
# `29524`  
# `14762`  
# `7381`  
# `22144`  
# `11072`  
# `5536`  
# `2768`  
# `1384`  
# `692`  
# `346`  
# `173`  
# `520`  
# `260`  
# `130`  
# `65`  
# `196`  
# `98`  
# `49`  
# `148`  
# `74`  
# `37`  
# `112`  
# `56`  
# `28`  
# `14`  
# `7`  
# `22`  
# `11`  
# `34`  
# `17`  
# `52`  
# `26`  
# `13`  
# `40`  
# `20`  
# `10`  
# `5` 
# `16`  
# `8`  
# `4`  
# `2`  
# `1`  
# `steps = 62`

# %% [markdown]
# ## Завдання для самостіної роботи
# 
# 1. Виконати завдання 1-12 наведені вище у цьому зошиті.
# 
# 1. Створити файл __lab_4_StudentLastName.py__ з написаним кодом. 
# 
# 1. Закомітити файл у локальний репозиторій.
# 
# 1. Відправити ("запушити") поточну версію Git-проєкта у віддалений репозиторій на GitHub.
# 
# 1. Звіт має складатися з файлу (за основу взяти __цей Python-зошит__)  `lab_3_StudentLastName.ipynb`. (Можливі якісь додакові файли)

# %% [markdown]
# ## Контрольні запитання
# 
# 1. Який вивод наступного фрагмента?
# ![image.png](attachment:65c31290-2a18-4578-868c-c45b92da46b2.png)
# 
# 
# 1. Який вивод наступного фрагмента?
# ![image.png](attachment:6f079200-c1b9-4ecc-8400-433837d5236c.png)
# 
# 1. Який вивод наступного фрагмента?
# ![image.png](attachment:97473cfe-64c8-4e49-8e3b-493f2f95f3c0.png)
# 

# %% [markdown]
# 
# 1. Вивід:
# 
# False
# 
# True

# %% [markdown]
# 2. Вивід:
# 
# False
# 
# True

# %% [markdown]
# 3. Вивід:
# 
# True
# 
# False

# %% [markdown]
# ## References

# %% [markdown]
# 1. [Anaconda (Python distribution)](https://uk.wikipedia.org/wiki/Anaconda_(Python_distribution))
# 2. [Conda](https://conda.io/en/latest/)
# 3. [Pro Git Book](https://git-scm.com/book/en/v2)
# 4. [OpenEDG Python Institute](https://pythoninstitute.org/)
# 5. [Cisco. Networking Academy](https://www.netacad.com/)
# 6. [Научно-издательская система Quarto](https://data-visualization-blog.netlify.app/posts/quarto/)


