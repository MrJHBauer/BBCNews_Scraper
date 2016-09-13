# BBC News Scraper

This is simple web scraper for BBC News most read content. It scrapes http://www.bbc.co.uk/news/popular/read for the 9 most popular articles taking with it the title and url. In addition this it accesses each articles page to return the introduction of the article.

## Installation

Simply download the [main.py](https://github.com/MrJHBauer/BBCNews_Scraper/blob/master/main.py) from this repository. [Python 3](https://www.python.org/) is required in addition to [requests](http://docs.python-requests.org/en/master/) and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/). This has been tested on Python 3.5.2 on Ubuntu 16.04

## Usage

Simply call `python3 main.py` inside the terminal and it shall return the 9 most read articles from the BBC News website.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
