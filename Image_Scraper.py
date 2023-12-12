import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, num_images_to_download):
    # Create a directory to save images
    os.makedirs("downloaded_images", exist_ok=True)

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract image URLs
    img_tags = soup.find_all('img')
    img_urls = [urljoin(url, img['src']) for img in img_tags]

    # Download specified number of images
    for i, img_url in enumerate(img_urls[:num_images_to_download]):
        response = requests.get(img_url)

        # Save the image to the 'downloaded_images' directory
        with open(f"downloaded_images/image_{i+1}.jpg", 'wb') as f:
            f.write(response.content)

if __name__ == "__main__":
    # Specify the URL of the webpage containing images
    target_url = "https://example.com"

    # Specify the number of images to download
    num_images_to_download = 10

    # Download images
    download_images(target_url, num_images_to_download)
