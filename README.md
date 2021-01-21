# E-Learning Management System :

This is my CS50 Final Project. I have buillt an E-learning management System where a user have several roles viz. instructors, learners and Admin. Admin.In this system, Instructors can create,edit or delete a course , several modules within a course and different content (notes, images and videos) for each module via content management system provided to him.A learner can enroll in several courses, can view there modules and content. Learner can chat with other learners within same course via course chat room(built using django channels).
         
 This project contains three apps working together, a courses app for course managemet, students app for learners managemet and chat app for chat server.Production environment is setup using NGINX and uwsgi. NGINX runs in front of uWSGI and Daphne as a reverse proxy server. NGINX facesthe Web and passes requests to the application server (uWSGI or Daphne) basedon their path prefix. Besides this, NGINX also serves static files and redirects nonsecure requests to secure ones. This setup reduces downtime, consumes less serverresources, and provides greater performance and security.
 
The technology stack used include django, django-channels, mysqlite for backend and HTML, CSS, Bootstrap 4.5, jquery and Ajax in frontend. Also redis server is used for communication store for chat application.The web app is mobile responsive and user interactive.

This project satisfies the complexity cs50 requirements for final project as it has 3 apps in it , also used django channels, redis and used jquery, ajax in fontend.

### Prerequisites :
1. Please Install all the packages in reuirements.txt file.
2. Also install redis 
If you are using Linux or macOS, download the latest Redis version from https://
redis.io/download.
3. For running project, in settings/pro.py make allowed hosts to * and use following command:
         ```python manage.py runserver --settings=education.settings.pro```

          
### Project directories and files
#### Education :
It is the main directory for project which includes urls.py, wsgi.py, asgi.py, routing.py and settings dir.
* wsgi.py includes wsgi configuration for education project.
* asgi.py includes asgi config which uses default asgi channels.
* routing.py has use URLRouter to map websocket connections to the URL patterns defined in the websocket_urlpatterns list of the chat application routing file. 
* urls.py include urls for different apps i.e. courses, students and chat also has path admin/ for django administration  and social_auth/ for social authentication.
* settings folder has local.py, base.py and pro.py. Base.py is base settings file, local.py and pro.py inherits these settings and pro.py is for production environment.

#### Courses :
It is app for managing courses there instructors, course modulles and content of different types.
##### courses/models.py
It includes several  models i.e. Subject, Course, Module and Content. These Models are connected with each other via Foreignkeys. Also there is Itembase named abstract model with common fields for content type which then inherited by Text, File, Image and Video.
##### courses/views.py
It has all class based views for course management. I used mixins by inheriting default class based views by user defined views. It encounts views or Managing course list, course creation-updation deletion, Course's module updation,content creation-updation-deletion, modules ordering and content ordering. Then it also embrace Course list view and course detail view.
##### courses/forms.py
* It encompass model formset for Course, Modules
##### courses/middleware.py
* A customm middleware is defined in it to allow subdomains for courses.
#####  courses/urls.py
* Its includes path for all views defined in views.py
##### courses/templates
It has base.html which is base template, footer.html which is a footer.
* templates/registration dir. has templates for login, logout.
* templates/courses dir. has content, course and manage directory.Templates related to managemnt views are in manage directory, content dir. has content templates and course dir. contain detial.html and list.html for course(Instructor's dashboard view)
##### course/templatetags
course.py and myfilter.py file are present in this directory in which a filter is defined to use in templates.

#### Students
This is app to manage learners.
##### students/views.py
Here, signup view is defined for student with email verification.
* Also it includes student course enroll view, course list view  and course detail view of enrolled courses.
##### students/forms.py
* It has CourseEnrollForm and SignupForm defined to use it in views.
##### students/templates
It has signup.html, course and student directory
* course directory includes templates for course list and detail view for enrolled courses(learner's dashboard)
##### students/management/commands/enroll_reminder.py
It has a Command class defined which inherits the BaseCommand. It is defined for sending an e-mail reminder to users registered more than N days that are not enrolled into any courses yet.

#### Chat
* It is app for implementing chat room in course.
* It contain consumers.py, routing.py, urls.py, views.py and templates.
* consumers.py has ChatConsumer defined which inherits AsyncWbesocketConsumer.
* views.py has course_chat_room view.
* routing.py has websockets_urlspatterns specified as re_path for chat room for each course(using course_id in url)
* templates/room.html defines frontend for course chat room.

#### config
* config directory have nginx.conf and uwsgi.ini files where nginx and uwsgi, nginx server configurations are specified respectively.

##### ssl directory has ssl certificate
##### static directory has static files generated  from ```python manage.py collectstatic```







