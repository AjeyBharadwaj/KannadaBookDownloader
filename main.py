import requests
import sys
import urllib.request
import os.path
import socket
import pdb
 
url = "https://kanaja.karnataka.gov.in/ebook/book-list/"
book_directory="books"

socket.setdefaulttimeout(15)

# create request
#x = requests.get(url)
#text = x.text
#text = text.split('\n')

with open("data.txt", 'r', encoding='utf-8') as f:
    text = f.readlines()

i = 0
for line in text:
    if "listing-item" in line:
        links = line.split("</a>")
        for link in links:
            while True:
                try:
                    if "href" not in link:
                        break
                    i += 1
                    print(f"{i} Original link : ", link)
                    booklink = link.split("href")[1].split('/">')[0].replace('="', '')
                    bookname = link.split('">')[-1]
                    print(f"{i} Link : {booklink}")
                    print(f"{i} BookName : {bookname}")

                    if os.path.isfile(f"{book_directory}/{bookname}.pdf"):
                        break

                    x = requests.get(booklink, timeout=5)
                    booktext = x.text
                    booktext = booktext.split('\n')
                    #with open("data1.txt", 'r', encoding='utf-8') as f:
                    #    booktext = f.readlines()
                    for line in booktext:
                        if 'btn btn-primary' in line or 'download' in line:
                            pdfurl = line.split("download")[0].split("href")[1].replace('"', '').replace('=', '').strip()
                            print(f"Pdfurl : {pdfurl}")
                            urllib.request.urlretrieve(pdfurl, f"{book_directory}/{bookname}.pdf")
                    break
                except Exception as ex:
                    print(f"Exception : {ex}")
                    continue