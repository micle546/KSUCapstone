###############################################################################################################

    # This script uses the openlibrary.org developer api to retrieve and return book data 
    # Author: Antonio Shelton-McGaha
    # Authored on: 11/3/2022
    # Capstone Group Members: Abdullah Almutlaq, Antonio S-M, Mitchell Stemm, Christabel Akhigbe, Mike Eubank

###############################################################################################################

import requests
import json

###############################################################################################################
    # ADD THE LINE BELOW TO THE TOP OF YOUR FILE TO USE THE 'get_book_data()' FUNCTION # 

    ############## from book_data import get_book_data ##############

    # get_book_data() takes a 10 or 13 digit ISBN as an argument and returns a dictionary of data for that book #
###############################################################################################################

def get_book_data(isbn):
    
    # Validating length of ISBN | Returns an error message if length of ISBN is not 10 or 13
    if len(isbn) != 13 and len(isbn) != 10:
        error = {"error": "Invalid ISBN. Length error."}
        return error
    
    # API endpoint
    url = f"https://openlibrary.org/isbn/{isbn}.json"

                     # PARSING #

    ############## get overall data ##############
    # Returns an error message if script fails to make request from API using endpoint
    try:
        data = requests.get(url)
        data = data.json()
    except:
        error = {"error": "An error occurred when fetching data from API. Invalid ISBN - Book not found"}
        return error
    ##############################################

    ################## get cover #################
    try:
        cover_id = data["covers"][0]
        cover = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
    except:
        cover = 'no cover available'
    ##############################################

    ################## get title #################
    try:
        title = data["title"]
    except:
        title = 'no title available'
    ##############################################

    ############## get publish date ##############
    try:
        publish_date = data["publish_date"]
    except:
        publish_date = 'no publish date available'
    ##############################################

    ################ get language ################
    try:
        language = data["languages"][0]["key"]
    except:
        language = 'no language available'
    ##############################################

    ############### get author name ##############
    try:
        authors = []
        if len(data["authors"]) > 1:
            for i in range (0, len(data["authors"])):
                author = data["authors"][i]["key"]
                author_url = f"https://openlibrary.org{author}.json"
                author_data = requests.get(author_url)
                author_data = author_data.json()
                try:
                    authors.append({"key": author_data["name"]})
                except:
                    authors.append({"key": author_data["personal_name"]})
        else:
            author = data["authors"][0]["key"]
            author_url = f"https://openlibrary.org{author}.json"
            author_data = requests.get(author_url)
            author_data = author_data.json()
            try:
                authors = [{"key": author_data["personal_name"]}]
            except:
                authors = [{"key": author_data["name"]}]
    except:
        authors = [{"key": 'no author available'}]
    ##############################################

    # Returning dictionary that contains all useful book data
    return {"title":title, "cover":cover, "isbn":isbn, "item_type":1, "authors":authors, "language":language, "publish_date":publish_date}
