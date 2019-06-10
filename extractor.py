import re


def extracte_date(text):
    return (extract_birthdate(text), extract_death(text))


def extract_birthdate(text):
    birthdate_regex = [
        r"née? (?P<birth>à une date inconnue)",
        r"née? \D*le (?P<birth>\d+(er)? \w+ \d+)",
        r"née? (?P<birth>vers \d+)"
    ]
    for regex in birthdate_regex:
        birth = re.search(regex, text)
        if birth is not None:
            return birth.group("birth")


def extract_death(text):
    death = re.search(r"morte? \D*le (\d+(er)? \w+ \d+)", text)
    if death is not None:
        return death.group(1)
