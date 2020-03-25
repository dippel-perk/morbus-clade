from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, create_test, update_test_result, citizen_detail_pk, evaluation

urlpatterns = [
    path('', home, name='health-home'),
    path('evaluation', evaluation, name='health-evaluation'),
    path('detail/<int:pk>', citizen_detail_pk, name='citizen-detail-pk'),
    path('login', LoginView.as_view(template_name='health/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='health/logout.html'), name='logout'),

    path('test/create', create_test, name="create-test"),
    path('test/update', update_test_result, name="update-test")
]
