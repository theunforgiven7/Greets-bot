import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils import keyboard
import requests
from bs4 import BeautifulSoup as BS


def get_random_greeting_a_w():
    #головна сторінка
    pages_a_w = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/zhntsi/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 25):
        #додається у список 
        pages_a_w.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/zhntsi/{i}.htm')
    #обираємо випакову сторінку
    page_url = random.choice(pages_a_w)
    
    r = requests.get(page_url, timeout=3)
    html = BS(r.content, 'html.parser')
    #з html коду витягуються всі елементи з класом ‘тртрртрт’, і їх текст зберігається в списку
    greetings_a_w = [el.get_text(" ") for el in html.select('.content .sfst')]
    #зі списку випадковим чином вибирається одне привітання.
    greeting_a_w = random.choice(greetings_a_w)
    symbols1 = []
    #якщо символ є великою літерою, то до нього додається \n і він додається в список symbols1. В іншому випадку, символ просто додається в список
    for a in greeting_a_w:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    #всі символи в списку symbols1 об’єднуються в одну строку, яка зберігається в змінній formatted_greeting
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting


#


def get_random_greeting_mother():
    pages_mom = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/mami/']
    for i in range(1, 25):
        pages_mom.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/mami/{i}.htm')
    page_url = random.choice(pages_mom)
    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    greetings_mom = [el.get_text(" ") for el in html.select('.content .sfst')]
    greeting_a_w = random.choice(greetings_mom)
    symbols2 = []
    for a in greeting_a_w:
        if a.isupper():
            symbols2.append('\n' + a)
        else:
            symbols2.append(a)
    formatted_greeting = ''.join(symbols2)
    return formatted_greeting
#


def get_random_greeting_dother():
    pages_a_w = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/dochts/']
    for i in range(1, 25):
        pages_a_w.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/dochts/{i}.htm')
    page_url = random.choice(pages_a_w)
    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    greetings_dother = [el.get_text(" ") for el in html.select('.content .sfst')]
    greeting_dother = random.choice(greetings_dother)
    symbols1 = []
    for a in greeting_dother:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting
#


def get_random_greeting_sister():
    pages_sister = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/sestri/']
    for i in range(1, 15):
        pages_sister.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/sestri/{i}.htm')
    page_url = random.choice(pages_sister)
    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    greetings_sister = [el.get_text(" ") for el in html.select('.content .sfst')]
    greeting_sister = random.choice(greetings_sister)
    symbols1 = []
    for a in greeting_sister:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting
#


def get_random_greeting_friend_w():
    pages_friend_w = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/podruzi/']
    for i in range(1, 15):
        pages_friend_w.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-ukrainskom/podruzi/{i}.htm')
    page_url = random.choice(pages_friend_w)
    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    greetings_friend_w = [el.get_text(" ") for el in html.select('.content .sfst')]
    greeting_friend_w = random.choice(greetings_friend_w)
    symbols1 = []
    for a in greeting_friend_w:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    formatted_greeting = ''.join(symbols1)
    return formatted_greeting
#