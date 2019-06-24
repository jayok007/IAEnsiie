import re
import treetaggerwrapper


def extract(people):
    name, text = people
    print('Extract infos for', name)
    return {
        'name': name,
        'text': text,
        'birth_date': extract_birthdate(text),
        'death_date': extract_death(text),
        'sexe': extract_sexe(text),
        'jobs': extract_job(text)
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


def extract_job(first_sentence):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
    first_sentence = first_sentence.split('est')[1]
    tags = treetaggerwrapper.make_tags(
        tagger.tag_text(first_sentence),
        allow_extra=True
    )

    #  Tags that seperate two jobs
    between_tags = ['KON', 'PUN', 'ADV']
    # End of jobs tags
    end_tags = ['VERB', 'SENT', 'VER:pper']
    # Tags that are useless
    remove_tags = ['DET:ART', 'NUM', 'PRP:det']

    jobs = []
    job = ''
    for i, tag in enumerate(tags):
        # If end
        if tag.pos in end_tags:
            if job != '':
                jobs.append(job)
            break
        # If we don't care (un, une for example)
        elif tag.pos in remove_tags:
            continue
        # If between job tag
        elif tag.pos in between_tags:
            if job != '':
                jobs.append(job)
                job = ''
        # If ok tag
        else:
            if job != '' and job[-1] != '\'':
                job += ' '
            job += tag.word

        # If end of string
        if i == (len(tags) - 1):
            if job != '':
                jobs.append(job)

    return jobs
