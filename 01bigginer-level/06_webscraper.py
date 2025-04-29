import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        print(f"Title of the page: {soup.title.string}\n")

        print("All links on the page:")
        for link in soup.find_all('a', href=True):
            print(link['href'])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ").strip()
    if url:
        scrape_website(url)
    else:
        print("No URL entered.")
