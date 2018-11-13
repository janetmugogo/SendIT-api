
[![Coverage Status](https://coveralls.io/repos/github/janetmugogo/SendIT-api/badge.svg)](https://coveralls.io/github/janetmugogo/SendIT-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/18e7c5a2fee1e92ba154/maintainability)](https://codeclimate.com/github/janetmugogo/SendIT-api/maintainability)
[![Build Status](https://travis-ci.com/janetmugogo/SendIT-api.svg?branch=test_travis)](https://travis-ci.com/janetmugogo/SendIT-api)

# SendIT-api
SendIT is a courier management API, which will help users in getting information about their orders, and also requesting on viewing their orders and perform operations like updating destination of a parcel and canceling.

## API Endpoints
| Method | Endpoint | Description |
| --- | --- | --- |
|GET | /api/v1/parcel  | Get all parcel delivery orders |
|GET | /api/v1/parcel<parcelid>  | Get a specific parcel delivery order by id |
|POST | /api/v1/users | create a user(register) |
|GET | /api/v1/user<userid>  | Get a all parcel delivery orders by specific user  |
|PUT | /api/v1/parcels/<parcelid>/cancel | cancel the specifc parcel delivery order |
|POST | /api/v1/parcels | create a parcel delivery order |
|PUT | /api/v1/parcels/<parcelid>/changedestination | change destination of a parcel by id |

## Running and testing the API endpoints
 - python  -version 3.6 +
 - postgress database
 - postman to run and test the endpoints
 
## Installation/How to run the application locally
 - create a folder in your local workspace<br>
- open terminal while in that folder<br>
- git init(initialize)<br>
- git clone https://github.com/janetmugogo/SendIT-api.git

## Create a virtual environment
 create a virtual environment via the terminal and write:
  - virtualenv -p python3
 Activate the virtual environment for you to install other python requirements
  - source bin/activate
 Next, install requirements by typing:
  -pip install -r requirements.txt
  
 ## Testing
 Unit Testing
  - to test endpoints, there are tools that are required, for instance:
      -POSTMAN
 ##To test this application
 on the terminal, write this
  - nosetests --with-coverage --cover-package=app && coverage report
 


