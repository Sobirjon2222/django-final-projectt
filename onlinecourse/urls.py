from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # ex: /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # ex: /enroll/5/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # <HINT> Create a route for submit view
    # Retrieved both lesson id and course id from exam form and passed in url params
    path('<int:course_id>/<int:lesson_id>/submit/', views.submit, name='submit'),

    # <HINT> Create a route for show_exam_result view
    # Passed the lesson id in url to retrieve the particular lesson in question
    # Useful especially when some or all questions go unanswered
    path('course/<int:course_id>/lesson/<int:lesson_id>/submission/<int:submission_id>/result/', \
        views.show_exam_result, name='exam_result'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
