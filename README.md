# Inventory_src

A browser-based application to manage IT Inventory at Beloit College.

## Set up project on your local machine

This product requires you to have Python, Git, and MySQL installed.  The following commands are for a Windows machine and may differ for machines using a different OS. Known differences are shown.

1/ Create and run a virtual environment:
- If not already installed, install using the following command: 		
```bash
pip install virtualenv
```
- Use the following command to create a virtual environment, replacing ‘name’ with the desired name for your virtual environment:			
```bash
python -m venv ‘name’
```
- Use the following command to activate the virtual environment, replacing ‘name’ with the name you just used to create it.
```bash
source ‘name’/bin/activate
```
2/ Install django by using: 
```bash
pip install django
```
3/ Clone the product from git by using the following command: 			
```bash
git clone https://github.com/wadoodalam/Inventory_src.git
```
4/ Install mysql client by using: 
```bash
pip install mysqlclient
```
5/ Specify Server
- In a file explorer, go to inventory_src/inventory
- Open settings.py in a text editor
- In the “DATABASES” dict, change the following:
```bash
‘NAME’: your data base name
‘PASSWORD’: the password for your database
```
- Save the file and close it
- Navigate to inventory_src in the terminal
6/ Run the following commands to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```
7/ Depend on your use case, you can follow this [user manual](https://docs.google.com/document/d/10sXVrJy-zxhvN_HQGPUmI2P6xMk7Q_nM5BPucYE5sLE) to run the server and explore the provided features

## For future developers: Project Organization

- The Django-related settings are in Inventory_src/Inventory
- The backend implementation is in Inventory_src/Inventory_app
- The HTML files - frontend templates are in Inventory_src/Inventory_app/templates
- The CSS files are in Inventory_src/static/CSS

### Django Settings
- To manage dependency, database information and Django settings for this particular project, modify Inventory_src/Inventory/settings.py
- To update URL patterns and control the general flow of the website, modify Inventory_src/Inventory/urls.py

### Backend Implementation
- Database models and their relations are set up in Inventory_src/inventory_app/models.py
- After setting up your models, remember to register them in Inventory_src/inventory_app/admin.py
- The Django forms (used to take users' input before updating corresponding data table) are stored in Inventory_src/inventory_app/forms.py 
- The render functions (including search, filter and csv generating features) are stored in Inventory_src/inventory_app/views.py


### Frontend Implementation
- The HTML templates are stored in Inventory_src/Inventory_app/templates. After creating a template, remember to call them in Inventory_src/inventory_app/views.py from the appropriate function. Otherwise, the page will never be rendered
- The CSS files (styling sheets) are stored in Inventory_src/static/CSS. These files are linked to corresponding HTML templates through the STATIC_URL and STATIC_ROOT defined in Inventory_src/Inventory/settings.py

### Testing
- Unit tests can be added in Inventory_src/inventory_app/tests.py

If you have any concern about the project, please let us know by creating an issue. 
