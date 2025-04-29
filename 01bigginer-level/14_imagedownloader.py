import requests
import os

def download_image(url, filename=None):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        if not filename:
            filename = url.split("/")[-1]
            if not filename:
                filename = "downloaded_image"
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Image downloaded and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {e}")

if __name__ == "__main__":
    url = input("Enter the image URL to download: ").strip()
    if url:
        filename = input("Enter filename to save as (leave blank for default): ").strip()
        filename = filename if filename else None
        download_image(url, filename)
    else:
        print("No URL provided.")
