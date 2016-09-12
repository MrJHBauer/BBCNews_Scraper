import requests
from bs4 import BeautifulSoup


def main():
    url = "http://www.bbc.co.uk/news/popular/read"  # URL of the page where 10 most popular news stories are available.
    response = requests.get(url)  # send a GET request using the specified URL and save the resulting response.

    soup = BeautifulSoup(response.content, "html.parser")  # Create a BeautifulSoup object using the requested HTML doc.
    # print(soup.prettify())  # Print the HTML document in a more readable format.

    most_popular = soup.find_all("a", {"class": "most-popular-page-list-item__link"})  # Get the <a> tags with stories.
    print(most_popular)  # Print the anchor tags and containing child elements.

if __name__ == "__main__":
    main()
