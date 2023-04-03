# Lab-4

1. Build a Django contacts app from scratch.
2. Start your project.
3. Create your app. Name it as you like.
4. Create your templates folder.
    1. Create your app folder under templates and create index.html, contacts.html, help.html files there. You can use an HTML boilerplate for now.
5. In settings.py update
    1. TEMPLATES -> DIRS
        1. Add your directory
    2. INSTALLED_APPS
        1. Add your app name
6. Update your models.py
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

8. Update urls.py
9. Do the migration. Necessary updates for the database.
10. Do the necessary updates to be able to use the admin interface
11. Add a couple of contacts using admin interface
12. Update your index.html, help.html and contacts.html
    1. Get creative.
13. Display those files
    1. localhost:8000/ (for index.html)
    2. localhost:8000/help/
    3. localhost:8000/contacts/
14. Add screenshots for each of the steps into your repository
15. Update the **readme file** by answering the following questions and typing your answers in that file.
    1. Explain your steps and include screenshots if needed.
16. Submit your repository via github.
