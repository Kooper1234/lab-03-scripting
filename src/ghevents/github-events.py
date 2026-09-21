#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """This function retrieves the events from the GitHub API."""
    return json.loads(requests.get(url).text)
    

def print_events(events, n=5):
    """This function prints n events to the console."""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name'] + ' :: ' + x['created_at']
        print(event)

def main():
    print(GHUSER)
    print(url)
    retrieve_events(url)
    events = retrieve_events(url)
    print_events(events)

if __name__ == "__main__":
    main()