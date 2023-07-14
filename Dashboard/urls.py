from django.urls import path, include
from rest_framework import routers

from Dashboard import views
from Dashboard.api_views import PersonViewSet, DepartmentViewSet, CourseViewSet, StudentViewSet, LecturerViewSet
from Dashboard.views import HomeView, LoginView, ForgotPasswordView, ChangePasswordView, RegisterView, SettingsView, \
    CoursesView

app_name = "Dashboard"

router = routers.DefaultRouter()
router.register('department', DepartmentViewSet)
router.register('course', CourseViewSet)
router.register('person', PersonViewSet)
router.register('student', StudentViewSet)
router.register('lecturer', LecturerViewSet)

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('forgot_password', ForgotPasswordView.as_view(), name="forgot_password"),
    path('forgot_password/change_password<int:user_id>', ChangePasswordView.as_view(), name="change_password"),
    path('account/dashboard', HomeView.as_view(), name="home"),
    path('account/settings', SettingsView.as_view(), name="settings"),
    path('account/settings/<str:username>', SettingsView.as_view(), name="settings"),
    path('account/courses', CoursesView.as_view(), name="courses"),
    path('account/courses/toggle<str:course_code>', views.toggle_course, name="toggle_course"),
    path('api', include(router.urls)),
]
