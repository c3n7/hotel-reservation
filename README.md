# Hotel Reservation System

## Requirements
You should have installed these:
- Python

### Project setup
1. In the project's root directory, create a virtual environment
    ```shell
    $ python -m venv venv
    ```
2. Activate the environment
    - If in a Linux environment
        ```shell
        $ source venv/bin/activate
        ```
    - If in a Windows environment
        ```shell
        > venv\Scripts\activate
        ```
3. Install the dependencies
    ```shell
    pip install -r requirements.txt
    ```
4. Migrate the models
    ```shell
    python manage.py migrate
    ```
5. Create a superuser account. If you log in using this in the website, you'll be able to add rooms that the hotel offers.
    ```shell
    python manage.py createsuperuser
    ```
    
### Running the project
1. Run the server
    ```shell
    python manage.py runserver
    ```
You should now be able to access the project on `localhost:8000`


---
### Disclaimer
This is a far-from-finished project done as part of a classroom assignment. It can do CRUD but can in no way be used as a full-featured hotel-reservation system.