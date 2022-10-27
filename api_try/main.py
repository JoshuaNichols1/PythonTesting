from flask import Flask, render_template
import requests
import json
from datetime import datetime
from serpapi import GoogleSearch
from key import key
from olclient.openlibrary import OpenLibrary
import olclient.common as common


app = Flask(__name__)


@app.route("/")
@app.route("/iss")
def iss():
    query = {"lat": "-27.49991160047569", "lon": "153.25767865434028"}
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=query)

    data = json.loads(response.text)

    data_response = data["response"]

    data_response_1 = data_response[0]

    duration_print = round(data_response_1["duration"] / 60, 2)

    risetime_date = datetime.fromtimestamp(data_response_1["risetime"]).strftime(
        "%d/%m/%y"
    )
    risetime_time = datetime.fromtimestamp(data_response_1["risetime"]).strftime(
        "%I:%M %p"
    )

    return render_template(
        "iss.html",
        dur_p=duration_print,
        ris_d=risetime_date,
        ris_t=risetime_time,
        lat=float(query["lat"]),
        lon=float(query["lon"]),
    )


@app.route("/people")
def people():
    import requests
    import json

    response = requests.get("http://api.open-notify.org/astros.json")

    data = json.loads(response.text)

    data_response = data["people"]

    dict_use = {}

    for i in data_response:
        dict_use.update({i["name"]: i["craft"]})

    data_sort = dict(sorted(dict_use.items(), key=lambda item: item[1]))

    iss_dict = {}

    other_dict = {}

    for i in data_sort:
        if data_sort[i] == "ISS":
            iss_dict.update({i: data_sort[i]})
        else:
            other_dict.update({i: data_sort[i]})

    api_key = key()
    question = ""
    params = {
        "q": "",
        "tbm": "isch",
        "ijn": "0",
        "api_key": f"{api_key}",
    }

    def image_search(dict):
        images_dict = {}
        for i in dict:
            params.update({"q": f"{i}"})
            search = GoogleSearch(params)
            results = search.get_dictionary()
            images_results = results["images_results"]
            images_results = images_results[0]
            images_dict.update({i: images_results["thumbnail"]})
        return images_dict

    iss_img_dict = image_search(iss_dict)
    other_img_dict = image_search(other_dict)

    return render_template(
        "people.html",
        iss_data=dict(sorted(iss_dict.items())),
        other_data=dict(sorted(other_dict.items())),
        iss_img_dict=iss_img_dict,
        other_img_dict=other_img_dict,
    )


@app.route("/books")
def books():
    titles_dict = {}
    book_ids = []
    images_dict = {}
    isbn_dict = {}
    response = requests.get(
        "https://www.googleapis.com/books/v1/volumes?q=Harry_Potter_and_the_chamber_of_secrets"
    )
    data = json.loads(response.text)
    numrecords = data["totalItems"]
    if numrecords > 100:
        for i in range(100 // 40):
            response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q=Harry_Potter_and_the_chamber_of_secrets&maxResults=40&startIndex={i*40}"
            )
            data = json.loads(response.text)
            data_response = data["items"]
            for record in data_response:
                book_id = record["id"]
                info = record["volumeInfo"]
                title = info["title"]
                link = f"https://books.google.com/books/content?id={book_id}&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                industryIdentifiers = info["industryIdentifiers"]
                isbn13_record = industryIdentifiers[0]
                isbn13 = isbn13_record["identifier"]
                titles_dict.update({book_id: title})
                isbn_dict.update({book_id: isbn13})
                images_dict.update({book_id: link})
                book_ids.append(book_id)
    else:
        for i in range(numrecords // 40):
            response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q=Harry_Potter_and_the_chamber_of_secrets&maxResults=40&startIndex={i*40}"
            )
            data = json.loads(response.text)
            data_response = data["items"]
            for record in data_response:
                book_id = record["id"]
                info = record["volumeInfo"]
                title = info["title"]
                link = f"https://books.google.com/books/content?id={book_id}&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                industryIdentifiers = info["industryIdentifiers"]
                isbn13_record = industryIdentifiers[0]
                isbn13 = isbn13_record["identifier"]
                titles_dict.update({book_id: title})
                isbn_dict.update({book_id: isbn13})
                images_dict.update({book_id: link})
                book_ids.append(book_id)
    return render_template(
        "books.html",
        titles_dict=titles_dict,
        images_dict=images_dict,
        book_ids=book_ids,
        isbn_dict=isbn_dict,
    )


@app.route("/openlibrary")
def openlibrary():
    # ol = OpenLibrary()
    # edition = ol.Edition.get("OL25952968M")
    # authors = edition.authors
    # work = edition.work
    # return str(authors)
    response = requests.get(
        "https://openlibrary.org/search.json?title=Harry+Potter+and+the+chamber+of+secrets&author=J.K+Rowling"
    )
    data = json.loads(response.text)
    data_response = data["docs"]
    return data
    # titles = []
    # for record in data_response:
    #     title = record["title"]
    #     titles.append(title)
    # return render_template("books.html", titles=titles)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
