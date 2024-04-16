import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils import keyboard
import requests
from bs4 import BeautifulSoup as BS
import re


def get_random_greeting_a_wen():
    #головна сторінка
    pages_a_w = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/zhenshchine/']
    #цикл для того щоб пройтись по всім сторінкам
    for i in range(1, 4):
        #додається у список 
        pages_a_w.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/zhenshchine/{i}.htm')
    #обираємо випакову сторінку
    page_url = random.choice(pages_a_w)

    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    #з html коду витягуються всі елементи з класом ‘.content .sfst’, і їх текст зберігається в списку
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
    formatted_greeting = formatted_greeting.split('(С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского на русский)')[0]
    formatted_greeting = formatted_greeting.split('(женщине - перевод)')[0]
    
    formatted_greeting = formatted_greeting.split('( С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод на русский)')[0]
    formatted_greeting = formatted_greeting.split('(перевод на русский язык)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского)')[0]
    formatted_greeting = formatted_greeting.strip()
    return formatted_greeting

def get_random_greeting_a_wen():
    pages_a_w = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/zhenshchine/']
    for i in range(1, 4):
        pages_a_w.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/zhenshchine/{i}.htm')
    page_url = random.choice(pages_a_w)

    r = requests.get(page_url, timeout=5)
    html = BS(r.content, 'html.parser')
    greetings_a_w = [el.get_text(" ") for el in html.select('.content .sfst')]
    greeting_a_w = random.choice(greetings_a_w)
    symbols1 = []
    for a in greeting_a_w:
        if a.isupper():
            symbols1.append('\n' + a)
        else:
            symbols1.append(a)
    formatted_greeting = ''.join(symbols1)
    formatted_greeting = formatted_greeting.split('(С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского на русский)')[0]
    formatted_greeting = formatted_greeting.split('(женщине - перевод)')[0]
    
    formatted_greeting = formatted_greeting.split('( С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод на русский)')[0]
    formatted_greeting = formatted_greeting.split('(перевод на русский язык)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского)')[0]
    formatted_greeting = formatted_greeting.strip()
    return formatted_greeting
#


def get_random_greeting_friend_wen():
    pages_friend_w = ['https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/podruge/']
    for i in range(1, 4):
        pages_friend_w.append(f'https://pozdravok.com/pozdravleniya/den-rozhdeniya/i/na-angliyskom/podruge/{i}.htm')
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
    formatted_greeting = formatted_greeting.split('(С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод)')[0]
    formatted_greeting = formatted_greeting.split('(перевод на русский)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского на русский)')[0]
    formatted_greeting = formatted_greeting.split('(перевод с английского)')[0]
    formatted_greeting = formatted_greeting.split('( С днем рождения — перевод)')[0]
    formatted_greeting = formatted_greeting.strip()
    return formatted_greeting
# 