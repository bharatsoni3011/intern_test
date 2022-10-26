# APIs implemented:
* add user (post)
* get user by id (get)
* update user details (put)
* delete user details (delete)
* get all users details (get)
* delete all users details (delete)

# API Structure:

## API Request(1) -> Controller(2) -> Service(3) -> Database Accessor(4) -> Service(5) -> Controller(6) -> API Response(7)

### Working
(1): here the user will hit an API end point (requesting for some data to be fetched, updated or deleted) using Swagger UI (a user friendly interface for users to interact with API)

(2): Controller layer is used to establish a relationship between API endpoints and their functionalities. It is used to receive and handle all the requests, process the operation, and return the result (JSON or HTML) to the user

(3): This layer is used to encapsulate the functionality (get,add,delete or update details) of APIs and provide requested information to be fetched from database to the DB Accessor layer.

(4): DB Accessor is used to fetch, update, delete and add data to the database (in this case MongoDB). This layer directly interacts with the database and do desired operation and return the return to the Service layer(5) to process.

(5): Now this layer converts the raw data (dictionary in this case) into processed data (Objects) and build a response based on the result fetched data.

(6): This step is to return the response to the user or throw an error based on the data recieved from Service layer.

(7): This response will be displayed to the user on the Swagger UI in JSON or HTML format.


## Example to get the details of a user by id: 

(1): Using Swagger UI enter the id of user for which you want to fetch details.

(2): '/user/{id}/get' this end point will be used to fetch the desired data.

(3): Service layer will act as a mediater to transfer request from controller to DB Accessor

(4): data will fetched from the database and will be returned in the for of a dictionary.

(5): now this layer will convert the dictionary to Objects with the corresponding data fields.

(6): depending on the response from the Service layer this controller layer will either return an Object or throw and error

(7): now the response or the error will be shown on the Swagger UI in either JSON or HTML format.
