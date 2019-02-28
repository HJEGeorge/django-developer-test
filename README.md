# django-developer-test
A skeleton Django project to test the onboarding of new developers on Django-forms, models and the project.


**The Goal:** 

To produce a form to the following specification:
1. The form contains a 'Full Name' which validates that a full name is given, not just a first or a last name.
2. The form contains a checkbox, asking 'Do you live in the UK?', if this checkbox is checked, a new field should appear, which asks for your UK Post Code.
    A UK Postcode is a 6-8 character post code with an optional space. Some examples of suitable inputs are: 'NW5 1HP', 'SE146BP', for more see [here](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting).
    
3. A CV PDF Upload field. This field should be safe from code injections or large file uploads.
4. A last salary field, with suitable validation, and a '£', prepended to the input field.
5. The submit button should trigger a bootstrap model, which asks the user to confirm whether they are ready to submit, or whether they'd like to go back.

All the fields above should have suitable validation, displayed in the standard bootstrap 4 style, under each field which has been validated incorrectly. Fields should have suitable labels, and placeholder text when necessary.
    