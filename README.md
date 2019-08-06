# Data Wrapper

*    Author: Guillem Alomar      
*    Current release: August 6th, 2019                     
*    Code version: 0.1                      
*    Availability: Public

## Index

* [Requirements](#requirements)
* [Documentation](#documentation)
    * [Explanation](#explanation)
* [Using the application](#using-the-application)
    * [Using your database](#using-your-database)
    * [Testing](#testing)

## Requirements

Programming language
- Python +3.7

PIP packages
- pytest 5.0.1
- pymongo 3.8.0
- mysql-connector-python 8.0.14
- mysql-connector-python-rf 2.2.2

## Documentation

### Explanation

This project consists of a python library to make use of a database in a transparent and simple way.

## Using the application

Download the pip package to your current environment:

```
-> % pip install data_wrapper
```

### Using your Database

This application has the option of using your MongoDB or MySQL database.

In order to do so, you will need to create a _creds.py_ file in your main folder (you can use the _creds_dummy.py_ file as a guide) and add your database credentials. Also don't forget to specify the database that you want to use by adding the input parameter when running the application:

```
-> % python GeneticAlgorithm.py -db [mongodb|mysql]
```

### Testing

Some tests have been added to the 'tests' folder. To run them, simply type from the main project folder:
```
-> nosetests tests
```
