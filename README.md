# Flask Restaurant

This app was built as a backend for data related to a restaurant menu. It was built with Flask and uses MongoDB to persist data.

## Technologies Used

* Flask
* MongoDB
* MongoEngine

## Installation

* Fork and clone this repository
* Though not required, it is recommended to create a virtual environment for the project
* run `$ pip install -r requirements.txt`
* run `$ flask run`
* navigate to localhost:5000, or use an api testing tool such as Postman

## Models

This app takes advantage of MongoDB's schemaless pattern. There is only one model (Entree), which has three fields - name (a string), recommended wine pairings (a list of strings) and allergens (a list of strings)

## Endpoints

* ` GET /entrees` - requests to this endpoint return all of the entree documents in the database
* ` POST /entrees` - requests to this endpoint persist an entree (in the body of the request) to the database
* ` GET /entrees/<id>` - requests to this endpoint find and return an entree in the database using the id param
* ` PUT /entrees/<id>` - requests to this endpoint find and update an entree in the database using the id param and an updated entree in the request body
* ` DELETE /entrees/<id>` - requests to this endpoint delete the selected entree in the database