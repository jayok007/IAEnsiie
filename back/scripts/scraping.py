# coding=utf-8
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import wikipedia

wikipedia.set_lang('fr')
URL = "https://fr.wikipedia.org/wiki/Le_Plus_Grand_Français_de_tous_les_temps"


def get_famous_peoples():
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "html.parser")
    div = soup.find("div", "colonnes")
    return [] if req is None else [li.text for li in div.find_all("li")]


def get_famous_people_text(name):
    print("Get summary for", name)
    return (name, wikipedia.summary(name))


def get_famous_peoples_text(peoples):
    n = len(peoples)
    print("Spawning", n, "threads for the threadpool")
    p = Pool(n)
    return p.map(get_famous_people_text, peoples)
