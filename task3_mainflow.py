import requests
from bs4 import BeautifulSoup

#url of web that we are web scrapping
url = "https://soax.com/scraping/ecommerce?utm_campaign=531514149&utm_medium={extensionid}&utm_content=1357899403547385&utm_term=competera%20web%20scraping%20tool&utm_source=bing.com&msclkid=c6aa040650891d577bc163029745afc8"

resp = requests.get(url)

print(resp) #checking output value

#extacting data if request code is 200
if resp.status_code == 200:
    html_cont = BeautifulSoup(resp.text,"html.parser")

    page_text = html_cont.get_text()

    page_link = [a["href"] for a in html_cont.find_all("a",href = True)]

    page_img = [img["src"] for img in html_cont.find_all("img",src = True)]

    #printing the details
    print("text:")
    print(page_text)

    print("links:")
    for link in page_link:
        print(link)

    print("images:")
    for image in page_img:
        print(image)

else:
    print(f"failed to retrive the data from web page since request code id {resp.status_codes}")