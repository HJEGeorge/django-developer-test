# django-developer-test
A skeleton Django project to test the onboarding of new developers on Django-forms, models and the project.



## The Goal: 

To produce a form to the following specification:
1. The form contains a 'Full Name' which validates that a full name is given, not just a first or a last name.
2. The form contains a checkbox, asking 'Do you live in the UK?', if this checkbox is checked, a new field should appear, which asks for your UK Post Code.
    A UK Postcode is a 6-8 character post code with an optional space. Some examples of suitable inputs are: 'NW5 1HP', 'SE146BP', for more see [here](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting).
    
3. A CV PDF Upload field. This field should be safe from code injections or large file uploads.
4. A last salary field, with suitable validation, and a '£', prepended to the input field.
5. The submit button should trigger a bootstrap modal, which asks the user to confirm whether they are ready to submit, or whether they'd like to go back.
6. Once valid data is submitted, the data should be stored in an appropriate manner in the database.

All the fields above should have suitable validation, displayed in the standard bootstrap 4 style, under each field which has been validated incorrectly. Fields should have suitable labels, and placeholder text when necessary.

### Example
Below is an example of the above spec:
![Example Image](https://i.imgur.com/cjekxta.png)
### Time
This task should take 1-5 hours depending on your knowledge of python and Django (1hr for an experienced Django dev, 5 hours for a beginner/hobbyist).

### Libraries
The django-crispy-forms library comes preinstalled, but you are free to use any libraries you wish (or none) in the completion of this project. 
However, remember that this test is emulating an enterprise project, and so you may want to consider security, reliability and code longevity when assessing packages.

### Submission
The recommended method of submission is to take a private fork of this repository, create your solution, add HJEGeorge as a collaborator, and then email 
the link and an estimate of how long it took to [development@stepex.co](mailto:development@stepex.co). Alternatively you can manage the source code however you'd like, but in this case please ensure that all files are emailed, including any details of how to install (if different from this repo).

## Installation
Download Python 3.6.7, if you're using ubuntu this would be `sudo apt-get install python3.6`.
It is recommended you work in a virtualenv (`python3 pip install virtualenv`).

To install the requirements use `pip install -r requirements.txt` while in the root folder of this project.

To initiate Django run `python manage.py migrate` and `python manage.py collectstatic`, then `python manage.py runserver` and open up `127.0.0.1:8000` on your browser of choice.

You should see a basic page with a simple form. You are now ready to begin.

## Build Details:

Django 2.1.7
Python 3.6.7

