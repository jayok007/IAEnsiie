import requests
from bs4 import BeautifulSoup

base_url = "https://fr.wikipedia.org"

def get_famous_peoples():
    peoples = []
    req = requests.get(base_url + "/wiki/Le_Plus_Grand_Français_de_tous_les_temps")

    if req is not None:
        soup = BeautifulSoup(req.text, "html.parser")

        div = soup.find("div", "colonnes")

        for li in div.find_all("li"):
            url = base_url + li.find("a")["href"]
            person = (li.text, url)
            peoples.append(person)

    return peoples

def get_famous_peoples_text(peoples):
    texts = []

    for (name, url) in peoples:
        req = requests.get(url)
        if req is not None:
            soup = BeautifulSoup(req.text, "html.parser")
            div = soup.find("div", {"id": "bodyContent"})
            texts.append((name, div.text))

    return texts


if __name__ == "__main__":
    peoples = get_famous_peoples()
    texts = get_famous_peoples_text(peoples)
