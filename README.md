# mitchadam.github.io

My personal website: https://mitchadam.com

## Building

To run the website locally just run the command `npm run start`

## Get Books

- `python3 -m pip install python-dotenv requests xmltodict`
- `python3 get-books.py` - this broke so first manually run `curl --location 'https://www.goodreads.com/review/list?v=2&key=5EKW9AzpdwfOPldHu7Q&id=108920089&shelf=read&per_page=200&sort=date_read' \
--header 'Cookie: ccsid=613-0290512-1630872; locale=en' > goodreads.txt` and then run the script to populate the html file
