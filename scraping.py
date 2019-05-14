import requests
from bs4 import BeautifulSoup

base_url = "https://fr.wikipedia.org"

def get_famous_people():
    people = []
    req = requests.get(base_url + "/wiki/Le_Plus_Grand_Français_de_tous_les_temps")

    if req is not None:
        soup = BeautifulSoup(req.text, "html.parser")

        div = soup.find("div", "colonnes")

        for li in div.find_all("li"):
            url = base_url + li.find("a")["href"]
            person = (li.text, url)
            people.append(person)

    return people

if __name__ == "__main__":
    for person in get_famous_people():
        print(person)
