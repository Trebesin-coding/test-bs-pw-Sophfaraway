from bs4 import BeautifulSoup
import requests
import json


def main():

    url = "https://js-trebesin.github.io/bsoup-exam/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    # comment

    ingredients = soup.find_all(class_ = "stuff")
    print(ingredients)

    list = []

    for i in ingredients :
        list.append(i.text)
    print(list)

    for k in range(5):
        print(list[k])

    # for k in range(5):
    with open("recept.json","w") as f:
        json.dump(list[0], f, indent=4, ensure_ascii=False)
        json.dump(list[1], f, indent=4, ensure_ascii=False)
        json.dump(list[2], f, indent=4, ensure_ascii=False)
        json.dump(list[3], f, indent=4, ensure_ascii=False)
    








if __name__ == "__main__":
    main()