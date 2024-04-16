import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils import keyboard
import requests
from bs4 import BeautifulSoup as BS

def get_random_greeting_a_m():
    #головна сторінка
    pages_a_m = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/muzhchini/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 26):
        #додається у список 
        pages_a_m.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/muzhchini/{i}.htm')
    #обираємо випакову сторінку
    page_url = random.choice(pages_a_m)

    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    #з html коду витягуються всі елементи з класом ‘.content .sfst’, і їх текст зберігається в списку
    greetings_a_m = [el.get_text(" ") for el in html.select('.content .sfst')]
    #зі списку випадковим чином вибирається одне привітання.
    greeting_a_m = random.choice(greetings_a_m)
    symbols1 = []
    #якщо символ є великою літерою, то до нього додається \n і він додається в список symbols1. В іншому випадку, символ просто додається в список
    for a in greeting_a_m:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    #всі символи в списку symbols1 об’єднуються в одну строку, яка зберігається в змінній formatted_greeting
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting


# class RandomChooser:
#     def __init__(self, items):
#         self.items = items
#         self.index = len(items)

#     def choose(self):
#         if self.index == len(self.items):
#             random.shuffle(self.items)
#             self.index = 0
#         item = self.items[self.index]
#         self.index += 1
#         return item

# def get_random_greeting_a_m():
#     #головна сторінка
#     pages_a_m = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/muzhchini/']
#     #цикл для того щоб пройтись по всім сторінкам
#     for i in range(1, 26):
#         #додається у список 
#         pages_a_m.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/muzhchini/{i}.htm')
#     #обираємо випакову сторінку
#     page_url = random.choice(pages_a_m)
    
#     r = requests.get(page_url)
#     html = BS(r.content, 'html.parser')
#     #з html коду витягуються всі елементи з класом ‘.content .sfst’, і їх текст зберігається в списку
#     greetings_a_m = [el.get_text(" ") for el in html.select('.content .sfst')]
    
#     # Create a RandomChooser with the greetings
#     chooser = RandomChooser(greetings_a_m)
    
#     #зі списку випадковим чином вибирається одне привітання.
#     greeting_a_m = chooser.choose()
#     symbols1 = []
#     #якщо символ є великою літерою, то до нього додається \n і він додається в список symbols1. В іншому випадку, символ просто додається в список
#     for a in greeting_a_m:
#         if a.isupper():
#             symbols1.append('\n' + a)
#         else:
#             symbols1.append(a)
#     #всі символи в списку symbols1 об’єднуються в одну строку, яка зберігається в змінній formatted_greeting
#     formatted_greeting = ''.join(symbols1)
#     return formatted_greeting


#---------------------------------------------------------
def get_random_greeting_father():
    #головна сторінка
    pages_f = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/tatovi/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 15):
        #додається у список 
        pages_f.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/tatovi/{i}.htm')
    #обираємо випакову сторінку
    page_url = random.choice(pages_f)

    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    #з html коду витягуються всі елементи з класом ‘.content .sfst’, і їх текст зберігається в списку
    greetings_father = [el.get_text(" ") for el in html.select('.content .sfst')]
    #зі списку випадковим чином вибирається одне привітання.
    greeting_father = random.choice(greetings_father)
    symbols1 = []
    #якщо символ є великою літерою, то до нього додається \n і він додається в список symbols1. В іншому випадку, символ просто додається в список
    for a in greeting_father:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    #всі символи в списку symbols1 об’єднуються в одну строку, яка зберігається в змінній formatted_greeting
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting


def get_random_greeting_son():
    #головна сторінка
    pages_son = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/sinu/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 19):
        #додається у список 
        pages_son.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/sinu/{i}.htm')
    #обираємо випакову сторінку
    page_url = random.choice(pages_son)

    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    #з html коду витягуються всі елементи з класом ‘.content .sfst’, і їх текст зберігається в списку
    greetings_son = [el.get_text(" ") for el in html.select('.content .sfst')]
    #зі списку випадковим чином вибирається одне привітання.
    greeting_son = random.choice(greetings_son)
    symbols1 = []
    #якщо символ є великою літерою, то до нього додається \n і він додається в список symbols1. В іншому випадку, символ просто додається в список
    for a in greeting_son:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    #всі символи в списку symbols1 об’єднуються в одну строку, яка зберігається в змінній formatted_greeting
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting


def get_random_greeting_brother():
    #головна сторінка
    pages_brother = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/bratu/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 21):
        #додається у список 
        pages_brother.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/bratu/{i}.htm')
    #обираємо випакову сторінку
    page_url = random.choice(pages_brother)

    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    #з html коду витягуються всі елементи з класом ‘.content .sfst’, і їх текст зберігається в списку
    greetings_brother = [el.get_text(" ") for el in html.select('.content .sfst')]
    #зі списку випадковим чином вибирається одне привітання.
    greetings_brother = random.choice(greetings_brother)
    symbols1 = []
    #якщо символ є великою літерою, то до нього додається \n і він додається в список symbols1. В іншому випадку, символ просто додається в список
    for a in greetings_brother:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    #всі символи в списку symbols1 об’єднуються в одну строку, яка зберігається в змінній formatted_greeting
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting


def get_random_greeting_friend_m():
    #головна сторінка
    pages_friend_m = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/bratu/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 21):
        #додається у список 
        pages_friend_m.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/bratu/{i}.htm')
    #обираємо випакову сторінку
    page_url = random.choice(pages_friend_m)

    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    #з html коду витягуються всі елементи з класом ‘.content .sfst’, і їх текст зберігається в списку
    greetings_friend_m = [el.get_text(" ") for el in html.select('.content .sfst')]
    #зі списку випадковим чином вибирається одне привітання.
    greetings_friend_m = random.choice(greetings_friend_m)
    symbols1 = []
    #якщо символ є великою літерою, то до нього додається \n і він додається в список symbols1. В іншому випадку, символ просто додається в список
    for a in greetings_friend_m:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    #всі символи в списку symbols1 об’єднуються в одну строку, яка зберігається в змінній formatted_greeting
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting






































































