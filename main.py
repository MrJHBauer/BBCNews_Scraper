import requests


def main():
    url = "http://www.bbc.co.uk/news/popular/read"  # URL of the page where 10 most popular news stories are available.
    response = requests.get(url)  # send a GET request using the specified URL and save the resulting response.

    print(response.text)  # Print the responses text.

if __name__ == "__main__":
    main()
