#!/usr/bin/env python3
# coding=utf-8

from multiprocessing import Pool
from os import cpu_count
from google.cloud import firestore
from firebase_admin import credentials
from FirestoreClient import FirestoreClient
from scraping import get_famous_peoples, get_famous_peoples_text
from extractor import extract

if __name__ == "__main__":
    peoples_text = get_famous_peoples_text(get_famous_peoples())
    n = cpu_count()
    print("Spawning", n, "threads for the threadpool")
    p = Pool(n)
    peoples = p.map(extract, peoples_text)

    credentials.ApplicationDefault()
    firestore_client = FirestoreClient(firestore.Client())
    firestore_client.set_peoples(peoples)
