import re
import treetaggerwrapper
from nltk import sent_tokenize


def extract(people):
    name, text = people
    print('Extract infos for', name)
    return {
        'name': name,
        'text': text,
        'birth_date': extract_birthdate(text),
        'death_date': extract_death(text),
        'sexe': extract_sexe(text),
        'jobs': extract_job(name, text)
    }


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


def extract_sexe(text):
    first_sentence = text.split('.')[0]
    if 'née' in first_sentence:
        return 'F'
    elif 'né' in first_sentence:
        return 'M'
    else:
        if 'une' in first_sentence or 'elle' in first_sentence:
            return 'F'
        else:
            return 'M'


def _is_name_present(names, value):
    for word in value.split():
        if word in names and len(word) > 3:
            return True
    return False


def extract_job(name, text):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
    first_sentence = sent_tokenize(text)[0]
    if 'est' in first_sentence:
        first_sentence = first_sentence.split('est')[1]
    # Remove text between parentheses
    first_sentence = re.sub(r" ?\([^)]+\)", "", first_sentence)
    tags = treetaggerwrapper.make_tags(
        tagger.tag_text(first_sentence),
        allow_extra=True
    )    
    names = name.split(' ')
    #  Tags that seperate two jobs
    between_tags = ['KON', 'PUN', 'ADV']
    # End of jobs tags
    end_tags = ['VERB', 'SENT', 'VER:pper', 'PRO:REL']
    # Tags that are useless
    remove_tags = ['DET:ART', 'NUM', 'PRP:det']

    jobs = []
    job = ''
    for i, tag in enumerate(tags):
        # If end
        if tag.pos in end_tags:
            if job != '' and not _is_name_present(names, job):
                jobs.append(job)
            break
        # If we don't care (un, une for example)
        elif tag.pos in remove_tags:
            continue
        # If between job tag
        elif tag.pos in between_tags:
            if job != '':
                if job != '' and not _is_name_present(names, job):
                    jobs.append(job)
                job = ''
        # If ok tag
        else:
            if job != '' and job[-1] != '\'':
                job += ' '
            job += tag.word

        # If end of string
        if i == (len(tags) - 1):
            if job != '' and not _is_name_present(names, job):
                jobs.append(job)

    return jobs
