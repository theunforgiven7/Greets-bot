import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils import keyboard
import requests
from bs4 import BeautifulSoup as BS
import re


def get_random_greeting_a_m():
    #головна сторінка
    pages_a_m = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/muzhchine/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 4):
        #додається у список 
        pages_a_m.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/muzhchine/{i}.htm')
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
    formatted_greeting = formatted_greeting.split('(С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод на русский)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского на русский)')[0]
    formatted_greeting = formatted_greeting.split('(С днем рождения мужчине)')[0]
    formatted_greeting = formatted_greeting.split('(перевод в стихах на русский)')[0]
    formatted_greeting = formatted_greeting.split('(С днем рождения любимому мужчине)')[0]
    
    formatted_greeting = formatted_greeting.strip()
    return formatted_greeting
#


def get_random_greeting_friend_m():
    pages_friend_m = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/drugu/']
    for i in range(1, 4):
        pages_friend_m.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/drugu/{i}.htm')
    page_url = random.choice(pages_friend_m)
    
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
    formatted_greeting = formatted_greeting.split('(С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского на русский)')[0]
    formatted_greeting = formatted_greeting.split('(С днем рождения другу)')[0]
    formatted_greeting = formatted_greeting.strip()
    return formatted_greeting