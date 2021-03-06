import requests
import asyncio
import threading
from urllib.parse import urljoin
from be import serve
from fe import conf


thread: threading.Thread = None


def run_backend():
    serve.be_run()


def pytest_configure(config):
    global thread
    print("frontend begin test")
    thread = threading.Thread(target=run_backend)
    thread.start()


def pytest_unconfigure(config):
    url = urljoin(conf.URL, "shutdown")
    requests.get(url)
    thread.join()
    print("frontend end test")
