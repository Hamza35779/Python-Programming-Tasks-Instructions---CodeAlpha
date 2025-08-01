import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

def move_jpg_files():
    source = input("Enter the source folder path: ").strip().strip('\'"')
    destination = input("Enter the destination folder path: ").strip().strip('\'"')

    if not os.path.isdir(source):
        print(f"Error: Source folder '{source}' does not exist or is not a directory.")
        return

    try:
        os.makedirs(destination, exist_ok=True)
    except OSError as e:
        print(f"Error creating destination directory '{destination}': {e}")
        return

    moved_files = 0
    for filename in os.listdir(source):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            source_file = os.path.join(source, filename)
            try:
                shutil.move(source_file, os.path.join(destination, filename))
                moved_files += 1
            except (IOError, shutil.Error) as e:
                print(f"Could not move file '{filename}': {e}")
    print(f"Moved {moved_files} JPG/JPEG files from {source} to {destination}.")

def extract_emails():
    input_file = input("Enter the path of the .txt file to extract emails from: ").strip().strip('\'"')
    output_file = input("Enter the path of the output file to save emails: ").strip().strip('\'"')
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        emails = re.findall(email_pattern, content)
        unique_emails = sorted(list(set(emails)))
        with open(output_file, 'w', encoding='utf-8') as f:
            for email in unique_emails:
                f.write(email + '\n')
        print(f"Extracted {len(unique_emails)} unique email addresses to {output_file}.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except IOError as e:
        print(f"Error reading from or writing to a file: {e}")

def scrape_title():
    url = input("Enter the URL of the webpage to scrape the title from: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')

        if title_tag and title_tag.string:
            title = title_tag.string.strip()
            print(f"Title of the page: {title}")
            save_option = input("Save title to a file? (y/n): ").lower()
            if save_option.startswith('y'):
                filename = input("Enter filename to save the title: ").strip().strip('\'"')
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(title)
                    print(f"Title saved to {filename}")
                except IOError as e:
                    print(f"Error saving title to file: {e}")
        else:
            print("Title tag not found in the webpage.")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the webpage: {e}")

def main():
    tasks = {
        '1': ("Move all .jpg files from a folder to a new folder", move_jpg_files),
        '2': ("Extract all email addresses from a .txt file and save them to another file", extract_emails),
        '3': ("Scrape the title of a webpage and save it", scrape_title),
    }
    while True:
        print("\nTask Automation Options:")
        for key, (description, _) in tasks.items():
            print(f"{key}. {description}")
        print(f"{len(tasks) + 1}. Exit")

        choice = input(f"Enter your choice (1-{len(tasks) + 1}): ")

        if choice in tasks:
            tasks[choice][1]()
        elif choice == str(len(tasks) + 1):
            print("Exiting.")
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(tasks) + 1}.")

if __name__ == "__main__":
    main()
