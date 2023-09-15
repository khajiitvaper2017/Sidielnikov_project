# %% [markdown]
# ---
# title: "Лабораторна робота №2. Функція `print()`"
# description:
#   Документ зроблено за допомогою [Quarto](https://quarto.org/)
# author: "&copy; [<span style='color: blue;'>Valeriy Sydorenko </span>](https://www.linkedin.com/in/valeriy-sydorenko-6782279a/), 2023"
# date: "09.14.2023"
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
# __Мета:__ _навчитися писати і запускати найпростіші програми на Python з використанням функції `print()`_

# %% [markdown]
# ::: callout-note
# ## Примітка
# Перед виконанням лабораторної роботи необхідно опрацювати матеріал __Лекції 2__.
# :::

# %% [markdown]
# ::: callout-note
# ## Примітка
# У лабораторній роботі використано матеріали [python institute.](https://pythoninstitute.org/pcep) 
# :::

# %% [markdown]
# #### Що ви будете вміти?
# * використовувати функцію `print()` Python.
# * писати, выдлагоджувати та запускати прогарми на Python у середовищі IDE PyCharm.
# * обчислювати математичні вирази з використанням математичних операцій.

# %% [markdown]
# ## Функція `print()`

# %% [markdown]
# Розглянемо можливості функції `print()`, виконавши низку прикладів.
# 
# 1. Змінити код програми, щоби очикуваний результат виглядав наступним чином:

# %% [markdown]
# `Programming***Essentials***in...Python`

# %%
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# %% [markdown]
# <!-- 2 --> 

# %% [markdown]
# 2. Написати програму, яка виводила б на екран наступну картинку:

# %% [markdown]
# ![](attachment:image.png)

# %%
print("    *    ")
print("   * *   ")
print("  *   *  ")
print(" *     * ")
print("***   ***")
print("  *   *  ")
print("  *   *  ")
print("  *****  ")

# %% [markdown]
# 3. Вивести на екран наступний рядок:

# %% [markdown]
# `I'm student`

# %%
print("I'm student")

# %% [markdown]
# 4. Написати фрагмент кода в один рядок, використовуючи функцію `print()`, а також символи нового рядка та esсape-символи, щоби відповідати очикуваному результату, виведеному у трьох рядках: 

# %% [markdown]
# ![](attachment:image-2.png)

# %%
print('"I\'m"\n""learning""\n"""Python"""')

# %% [markdown]
# 5. Чому в десятковій системі дорівнює $500_8$? Написати код на Python.

# %%
int = 0o500

print(int)

# %% [markdown]
# 6. Чому в десятковій системі дорівнює $777_{16}$? Написати код на Python.

# %%
int = 0x777

print(int)

# %% [markdown]
# ## Завдання для самостіної роботи
# 
# 1. Виконати п. 1-6, наведені вище у цьому зошиті.
# 
# 1. Створити файл __lab_2_StudentLastName.py__ з написаним кодом. 
# 
# 1. Закомітити файл у локальний репозиторій.
# 
# 1. Відправити ("запушити") поточну версію Git-проєкта у віддалений репозиторій на GitHub.
# 
# 1. Звіт має складатися з файлу (за основу взяти __цей Python-зошит__)  `lab_2_StudentLastName.ipynb`.

# %% [markdown]
# ## Контрольні запитання
# 
# 1. Записати ієрархію операторів.
# 
# 1. Записти на Python обчислення виразу $3^{3^4}$
# 
# 1. Що робить escape-символ \n при виводі на екран функцією `print()`?

# %% [markdown]
# ## References

# %% [markdown]
# 1. [Anaconda (Python distribution)](https://uk.wikipedia.org/wiki/Anaconda_(Python_distribution))
# 2. [Conda](https://conda.io/en/latest/)
# 3. [Pro Git Book](https://git-scm.com/book/en/v2)
# 4. [OpenEDG Python Institute](https://pythoninstitute.org/)
# 5. [Cisco. Networking Academy](https://www.netacad.com/) 
# 6. [ЧТО ТАКОЕ ЯП PYTHON? УСТАНОВКА ПАЙТОНА НА WINDOWS 11 !](https://www.youtube.com/watch?v=nQMddf_6KoM&list=PLV0FNhq3XMOKljD7POtuWVAZn8wXcn4-L)


