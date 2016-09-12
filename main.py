import requests
from bs4 import BeautifulSoup


def main():
    url = "http://www.bbc.co.uk/news/popular/read"  # URL of the page where 10 most popular news stories are available.
    response = requests.get(url)  # send a GET request using the specified URL and save the resulting response.

    soup = BeautifulSoup(response.content, "html.parser")  # Create a BeautifulSoup object using the requested HTML doc.
    # print(soup.prettify())  # Print the HTML document in a more readable format.

    most_popular = soup.find_all("a", {"class": "most-popular-page-list-item__link"})  # Get the <a> tags with stories.
    # print(most_popular)  # Print the anchor tags and containing child elements.

    stories = {}  # Create a dict to store the title and links for popular news stories. Order won't be maintained.

    for anchor in most_popular:
        link = anchor.get("href")
        title = anchor.contents[3].text
        stories[title] = link  # Save the title and link of the story and key, value pair within the dict.

    for title, link in stories.items():
        print("Title: {} \nURL: http://www.bbc.co.uk{}".format(title, link))  # Print the title and link to console.

if __name__ == "__main__":
    main()
