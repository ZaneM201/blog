# Important notes for Django Projects

1. Open terminal and create a folder to store the project (e.g. SDGKU/my-projects/Django-projects/blog)
2. Move to the respective folder (make sure you are in the right location)
3. Create virtual enviroment (Windows: python -m venv venv | Mac: python3 -m venv venv)
4. Activate venv (Windows: venv\Scripts\activate | Mac: source venv/bin/activate)
5. Install django (pip install django)
    - Install django allauth (pip install django-allauth)
    - Install crispy forms/bootstrap (pip install django-crispy-forms crispy-bootstrap5)
6. Save packages into requirements.txt file (pip freeze > requirements.txt)
7. Creat the project (django-admin startproject config .)
8. Finish the structure
    - Create the static templates, img, css, and js folders
    - Create the .gitignore, README.md (optional) files
9. Link everything to settings.py


# Important not for DTL - Jinja
{% %} - Basic structure for all tags
{% block NAME_OF_THE_BLOCK %}{% endblock %} - Portion of code
{% load static %} - Load static files
{% extends 'filename' %} - Inheritance through htmls
{% include 'filename' %} - Insert html code into the desired one
{% static 'PATH_FOR_THE_FILE' %} - Load any static file (css, js, img)
{% url 'NAME_OF_THE_URL' %} - Travel through htmls