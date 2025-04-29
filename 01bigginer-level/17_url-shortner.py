import requests

def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def main():
    long_url = input("Enter the URL to shorten: ").strip()
    if not long_url:
        print("No URL entered.")
        return
    short_url = shorten_url(long_url)
    if short_url:
        print(f"Shortened URL: {short_url}")
    else:
        print("Failed to shorten the URL.")

if __name__ == "__main__":
    main()
