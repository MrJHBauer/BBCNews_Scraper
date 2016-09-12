import requests


def main():
    url = "http://www.bbc.co.uk/news/popular/read"
    response = requests.get(url)

    print(response.text)

if __name__ == "__main__":
    main()
