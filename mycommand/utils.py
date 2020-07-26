import time
import requests


def count_words_at_url(url):
    """Just an example function that's called async."""
    time.sleep(8)
    resp = requests.get(url)
    text_length = len(resp.text.split())
    print(text_length)
    return text_length
