
# E-Learning-Management-System
E-Learning Management System is the online learning platform that can be used by learners
as well as course creators to learn better way in the world of internet.This system have several roles as
Instructures, Students and the Admin.It  provides required tools an access to instructor to create sevral courses(subject specific).
These courses categorized by subjects and have number of modules and different contetnts(Notes, pdf,Images and topic related videos).
Students can enroll in as many as courses and can discuss with others learners enrolled in a course. It will help an 
organization(colleges, schools) to teach and learn better way out the world!!!.

### Django Models:
 1. Subject
 2. Course
 3. Module
 4. Content
 5. Item Base
 
 
 ### Features:
 * Add Courses, Modules for each course and different contents for each Module and manage all these with content management system.
 * Courses are categorized by subjects
 * User(student) can enroll for several courses of different subjects
 * Modules can be rearranged directly from UI(done using ajax and jquery)
 * Custom middleware created to send Email who have registered but not enrolled in any course for more than 15 days.
 * Chat with other learners enrolled in particular course(implemented using Django Channels and ASGI )
 * Responsive web-app and user freindlu UI
 * Use nginx + uWSGI to work with producation Envirinment 
 * Created Api so other websites can fetch data with valid credentials.
 * Used Bootstrap 4.5.3
 
 ### Apps :
 1. Courses
 2. Students
 3. Chat
 
 # E-Learning Management System
 
