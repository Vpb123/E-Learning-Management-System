from django.urls import path
from django.conf.urls import url
import students.views as views
from django.views.decorators.cache import cache_page
urlpatterns = [
    # path('register/', views.StudentRegistrationView.as_view(), name='student_registration'), 
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/',views.StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<pk>/',cache_page(60*15)(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('course/<pk>/<module_id>/', cache_page(60*15)(views.StudentCourseDetailView.as_view()), name='student_course_detail_module'),
    url(r'^signup/$', views.signup, name='student_registration'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]
