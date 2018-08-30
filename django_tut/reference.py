# Reference File

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#   Danjo Architecture                                      #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
#-> MVC Architecture
#-> URL Pattern + Views + Templates + Models
#
#   URL PATTERN ---------> VIEWS  ---------> TEMPLATES 
#                            |
#                          MODELS
#===========================================================#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Django App File Structure                                #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# app.py        - Configuration & Initialization
# models.py     - Data Layer
# admin.py      - Administative Interface 
# urls.py       - URL Routing
# views.py      - Control Layer
# tests.py      - Test the App
# migrations/   - Hold Migration File
#===========================================================#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Django Models & Fields                                   #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-> Models inherits from django.models.Model
#-> Field Type Reference -> 
#   https://docs.djangoproject.com/en/2.1/ref/models/fields/
#===========================================================#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Django Migartion                                         #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-> Generate scripts to chnage the database structure

#-> Migration needed when
#---> Adding a Model
#---> Adding a Field
#---> Changing a Field
#---> Removing a Field

#-> Migration commands
#---> makemigrations - shows the changes that has to be made
#---> showmigartions - shows migration status
#---> migrate        - makes the migration 
#===========================================================#


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Django Templates                                         #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-> {{ variable }} - to show a varible
#-> {% tag %} - to loop, if, control elements, ..etc
#-> {{ variable|filter }} - formater for strings on templates ( built-in filter->)
#-> {% url <name> [<arg>] %} - generates <name>'s url (refernce->url.py)

#-> Inheritance 
#--> {% block content %}
#--> {% endblock content %} 
#--> {% extends "<base_template>" %} - extends the <base_template>.
#--> {% load static %} - load static files.
#--> {% static <file_name> %} - load file <file_name>.
#===========================================================#


