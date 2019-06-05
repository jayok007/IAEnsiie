# coding=utf-8
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
from os import cpu_count
import re
import wikipedia
base_url = "https://fr.wikipedia.org"
wikipedia.set_lang('fr')

def get_famous_peoples():
    peoples = []
    req = requests.get(base_url + "/wiki/Le_Plus_Grand_Français_de_tous_les_temps")

    if req is not None:
        soup = BeautifulSoup(req.text, "html.parser")

        div = soup.find("div", "colonnes")

        for li in div.find_all("li"):
            url = base_url + li.find("a")["href"]
            person = (li.text, url)
            print("Hit url for", li.text)
            peoples.append(person)
    return peoples

def get_famous_people_text(people):
    name, url = people
    return (name, wikipedia.summary(name))

def get_famous_peoples_text(peoples):
    p = Pool(cpu_count())
    return p.map(get_famous_people_text, peoples)

if __name__ == "__main__":
    peoples = get_famous_peoples()
    texts = get_famous_peoples_text(peoples)
    # sequential list(map(get_famous_people_text, peoples))
