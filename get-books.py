import os
import requests
from dotenv import load_dotenv
import xmltodict
from datetime import datetime

header_text = """
---
title: "Books"
date: 2022-12-23T00:00:00-07:00
draft: false
---

# Books

---

See what I have been reading.
</br></br>
"""
output_path = "./content/books/_index.md"

# First run this in terminal
"""
curl --location 'https://www.goodreads.com/review/list?v=2&key=5EKW9AzpdwfOPldHu7Q&id=108920089&shelf=read&per_page=200&sort=date_read' \
--header 'Cookie: ccsid=613-0290512-1630872; locale=en' > goodreads.txt
"""
file_path = "/Users/mitchell/Documents/Code/mitch-www/goodreads.txt"


def main():
    # load_dotenv()
    # api_key = os.getenv('GOODREADS_KEY')
    # goodreads_id = os.getenv("GOODREADS_ID")

    # url = "https://www.goodreads.com/review/list"
    # params = {"v":  2, "key": api_key, "id": goodreads_id, "shelf": "read", "per_page": 200, "sort": "date_read" }
    # headers = {}

    # response = requests.get(url, params=params, headers=headers)
    # data = xmltodict.parse(response.text)
    with open(file_path, "r") as file:
        xml_content = file.read()
    data = xmltodict.parse(xml_content)

    books = data["GoodreadsResponse"]["reviews"]["review"]

    with open(output_path, "w") as file:
        file.truncate()  # Wipe file
        file.write(header_text)

        for book in books:
            html = f"""
<div>
<a
    href="{book["book"]["link"]}"
    target="blank"
    class="text-black no-underline">
    <div class="book-container rounded-lg p-0.5 shadow-lg transition hover:shadow-sm mb-5">
        <div class="flex flex-row justify-start content-start text-black no-underline p-4">
            <img
                class="book-thumbnail m-4"
                src="{book["book"]["image_url"]}"
                loading="lazy"
            />
            <div class="book-details w-full">
                <h3 class="mt-0.5 text-2xl font-medium text-gray-900 mt-2">
                <span
                class="hidden sm:inline text-base text-gray-600 float-right m-4 mt-1 ml-2"
                >{datetime.strptime(book.get("read_at", ""),"%a %b %d %H:%M:%S %z %Y").strftime("%B %d, %Y") if book.get("read_at", None) is not None else ""}</span
                >
                {book["book"]["title"]} - {book["book"]["authors"]["author"]["name"]}
                        <div class="text-sm font-light text-gray-800 pb-3">My Rating: {book["rating"]  + "/5" if book["rating"] != "0" else ""}</div>
                </h3>
                <span class="book-review text-sm font-light text-gray-800"><p class="mt-2">{book.get("body","") if book.get("body", None) is not None else ""}</p></span>
            </div>
        </div>
    </div>
</a></div>"""
            file.write(html)


if __name__ == "__main__":

    main()
