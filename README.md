# Product Tracker

## Description
This is a very simple REST API written in Python using Django. It is a simple product tracker that allows you to create, update, and supervise products. 

## Setup

### Install Dependencies
For the project to work properly, you need to install packets and dependencies. You can do that by running the following command:
Pip:
```shell
pip install -r requirements.txt
```
Conda:
```shell
conda create --name <env> --file requirements-conda.txt
```

### Set Up Database
Project is also using a little bit more advanced databse than sqlite, which is postgresql. You can run it by running the following command:
```shell
docker-compose up -d
```
To use the postgresql database, you need to create a database with the name: "producttracker".
If you don't want to use the postgresql database, you can revert to sqlite by commenting out the lines 85-94 and uncommenting the lines 78-83 in the productTracker/settings.py file.

### Run server
To start the project and run the server, you can run the following commands:
```shell
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```
## Endpoints
The projects consists of three endpoints:


### GET /warehouses
This endpoint allows you to see all the warehouses.
You can use the following options:
- Query Parameter page: This is the page number you want to see. If not provided there will be no pagination.

### GET /products
This endpoint allows you to see all the products.
You can use the following options:
- Query Parameter page: This is the page number you want to see. If not provided there will be no pagination.
- Query Parameter f: This is the option to filter by warehouse (id). If not provided there will be no filtering.

### POST & PUT /product
This endpoint allows you to create or update a specific product.
ID of the product is assigned automatically during creation.
To create a product, you have to provide the following data:
- name: The name of the product.
- stock: The stock of the product.
- warehouse: The warehouse where the product is stored.
Example:
```json
    {
        "name": "Dishwasher",
        "stock": 300,
        "warehouse": 4
    }
```
To update a product, you have to provide the same set of data (with the values you want to set)




