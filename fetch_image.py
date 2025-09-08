import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()

    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch image using requests
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for HTTP errors

        # Try to extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        save_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(save_path, "wb") as file:
            file.write(response.content)

        print(f"✅ Image successfully saved as: {save_path}")

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection or the URL.")
    except requests.exceptions.Timeout:
        print("❌ The request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"❌ An unexpected error occurred: {e}")
    except Exception as e:
        print(f"⚠ Something went wrong: {e}")

if __name__ == "__main__":
    fetch_image()
 