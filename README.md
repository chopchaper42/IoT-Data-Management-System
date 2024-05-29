# NSI Homework #3

**Database name**: temperature.db <br/>
**Path to the database**: ./temperature.db

## Data Class

The Data class serves as an interface for interacting with the temperature data stored in the database. It provides methods for adding new records, retrieving records, deleting records, and getting various statistics about the data.
Methods:

    add(temp): Adds a new temperature record to the database.
    last(): Retrieves the last temperature record from the database.
    last_n(n): Retrieves the last N temperature records from the database.
    del_n_oldest(n): Deletes the oldest N temperature records from the database.
    delete(timestamp): Deletes the temperature record with the specified timestamp from the database.
    get_all(): Retrieves all temperature records from the database.
    count(): Gets the total number of temperature records in the database.

## Temperature Class

The Temperature class represents individual temperature records in the database. It is implemented as a SQLAlchemy model and contains fields for the record ID, timestamp, and temperature value.
Attributes:

    id: Integer primary key for the record.
    timestamp: String representing the timestamp of the temperature measurement.
    value: Double representing the temperature value.

### Methods:

    to_dict(): Converts the temperature record to a dictionary for JSON serialization.

## Flask Routes

The Flask routes define the API endpoints and specify the actions to be taken for each endpoint. They interact with the Data class to perform CRUD operations on the temperature data.
API Paths:

    /api/add/<value> (POST, GET): Adds a new temperature record with the specified value.
    /api/last/ (GET): Retrieves the last temperature record.
    /api/last/<n> (GET): Retrieves the last N temperature records.
    /api/delete_oldest/<n> (POST): Deletes the oldest N temperature records.
    /api/get_all_temps (GET): Retrieves all temperature records.
    /api/delete/<timestamp> (POST): Deletes the temperature record with the specified timestamp.
    /api/number_of_records (GET): Gets the total number of temperature records.

