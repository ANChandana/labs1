# Lab-4

1. Build a Django contacts app from scratch.
2. Start your project.
3. Create your app. Name it as you like.
4. Create your templates folder.
    1. Create your app folder under templates and create index.html, contacts.html, help.html files there. You can use an HTML boilerplate for now.

**Answer for Step 1 to Step 4.1:**
The folder structure of my Lab 4 is as below which shows that i have created my project and created a app and named it as 'mycapp' which is short for mycontactsapp. I have also created templates folder in mycapp folder, and then created all the three of my html files in templates/mycapp folder. 
![image](https://user-images.githubusercontent.com/125329200/230728282-23530168-6888-4118-9f96-4d70edfe0b46.png)

5. In settings.py update
    1. TEMPLATES -> DIRS
        1. Add your directory
    2. INSTALLED_APPS
        1. Add your app name
**Answer for Step 5.1 to Step 5.2:**
I have made following changes in my settings.py file. 
![image](https://user-images.githubusercontent.com/125329200/230728436-23c56578-4e96-4a7f-9740-0479c736b4ad.png)
![image](https://user-images.githubusercontent.com/125329200/230728479-538e5ca8-af6b-4ed3-b65b-89b5d3c1f891.png)
![image](https://user-images.githubusercontent.com/125329200/230728508-4d8ba7f6-e0a1-4fb3-b8a2-15004d52a14e.png)


6. Update your models.py
**Answer for Step 6:**
The below is my models.py where i have updated the feilds that should be filled out in admin of Django. I gave str() in models.py so that it shows values instead of none. I have faced few errors to see contacts, so i browsed and came to know that we can add the function below in my Screenshot to fix it and it worked.
![image](https://user-images.githubusercontent.com/125329200/230728760-41a7b14f-c769-4a12-b20e-c6abf511e0a3.png)

7. Update your views.py to include html files
    1. Tip:

    ```python
    #import necessary models
    #include necessary html files

    def contacts(request):
    	contact_list = Contact.objects.order_by('first_name')
    	contact_dict = {'contacts':contact_list}
    	return render(request, 'appname/index.html', context=contact_dict)

    # complete the code
    ```
**Answer for Step 7:**
The below screenshot shows us a complete code in my views.py file, where includes requesting and rendering all the three html files.
![image](https://user-images.githubusercontent.com/125329200/230728872-4420556a-0328-4019-8928-8e8878e7ffa6.png)


8. Update urls.py
**Answer for Step 8:**
The below is my urls.py file, where i have added path for four links such as admin site, / (main page) , help/, contacts/.
![image](https://user-images.githubusercontent.com/125329200/230728960-4b5031a5-095f-429f-81d9-cb66358c38cf.png)

9. Do the migration. Necessary updates for the database.
**Answer for Step 9:**
I have made migrations sucessfully using below two commands:
python manage.py makemigrations mycapp
python manage.py migrate

10. Do the necessary updates to be able to use the admin interface
**Answer for Step 10:**
I have created superuser account by using the command 'python manage.py createsuperuser'. using those credentials, i was able to use the admin interface.

11. Add a couple of contacts using admin interface
**Update for Step 11:**
I have added four contacts using admin interface.

12. Update your index.html, help.html and contacts.html
    1. Get creative.
**Answer for Step 12.1:**
_index.html:_
![image](https://user-images.githubusercontent.com/125329200/230729450-56774aba-c26c-43f3-bb70-08b11fdaa4f8.png)

_help.html:_
![image](https://user-images.githubusercontent.com/125329200/230729484-9e502f62-b1e7-44bb-ab6e-ca6ca9fa578c.png)

_contacts.html:_
![image](https://user-images.githubusercontent.com/125329200/230729505-75c0b58a-f9be-4cdb-bd4b-475645633909.png)

13. Display those files
**Answer for Step 13.1 to 13.3:**
    1. localhost:8000/ (for index.html)
![image](https://user-images.githubusercontent.com/125329200/230729613-f8e3eda7-456f-477b-85ce-fecb1a309724.png)
    2. localhost:8000/help/
![image](https://user-images.githubusercontent.com/125329200/230729655-81950ff6-c36d-4a1d-b708-40d500c79177.png)
    3. localhost:8000/contacts/
![image](https://user-images.githubusercontent.com/125329200/230729690-6c2c7429-6a22-4956-94cd-60e413b7436e.png)
![image](https://user-images.githubusercontent.com/125329200/230729706-4ac130e0-c928-4325-9125-e353fe4ad032.png)

14. Add screenshots for each of the steps into your repository
Yes, added!
15. Update the **readme file** by answering the following questions and typing your answers in that file.
    1. Explain your steps and include screenshots if needed.
Yes, i have included screenshots for every step in the above.
i have started a project, created a my app. In that app, i have created templates/mycapp folder and added index, help, contacts html pages. I have updated settings.py, urls.py, models.py, views.py, admin.py files accordingly.
16. Submit your repository via github.
I have pushed my code back to git repository.
