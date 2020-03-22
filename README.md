## Morbus Clade

A proof of concept for scaling up Sars-Covid-2 testing in Germany. 
Developed as part of the [WirVsWirus](https://wirvsvirushackathon.org/) Hackathon. 
A running demo can be found [here](https://sars-cov2-testing.herokuapp.com/).

### Installation
The website is developed with the django framework.

1. Clone the repository.

2. Install the required dependencies with

    ``pip install -r requirements.txt``

3. Execute the database migrations:

    ``python manage.py migrate``

4. load some initial data into the database
    ``python manage.py loaddata health_system``

5. _optional_: load some dummy fake data for tested persons:
    ``python manage.py loaddata base_data``


### Run

Exceute `python manage.py runserver` to start the webserver.
