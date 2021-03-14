import requests
from bs4 import BeautifulSoup
import webbrowser
import time

COMMENT = "Don't look at my comment and expect to find any intrinsic value."
URL = "https://robinhood.com/stocks/"

cypher = "".join([word[0] for word in COMMENT.title().split()])
tickers = []
noise = []
while len(cypher) > 0:
    temp_cy = cypher
    while len(temp_cy) > 0:
        if temp_cy in noise + tickers:
            pass
        else:
            url = URL + temp_cy
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            error = soup.find_all(text="404")
            if len(error) == 0:
                tickers.append(temp_cy)
                print(temp_cy)
                webbrowser.open(url)
                time.sleep(4)
            else:
                noise.append(temp_cy)
        temp_cy = temp_cy[0:-1]
    cypher = cypher[1:]
