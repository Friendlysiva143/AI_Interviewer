from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.index, name="index"),
    path("home/", views.home, name="home"),

    # SSO auth
    path("auth/login/", views.user_login, name="user_login"),
    path("auth/callback/", views.callback_view, name="callback_view"),
    path("auth/logout/", views.user_logout, name="user_logout"),
    path("auth/register/", views.register_view, name="register"),
    path("auth/profile/", views.user_homepage, name="user_homepage"),
    path("complete-profile/", views.complete_profile, name="complete_profile"),
path('unauthorized-access/', views.unauthorized_access, name='unauthorized_access'),
    # admin
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('activate/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),

    # interview
    path('start/', views.start_interview, name='start_interview'),
    path('answer/', views.answer_question, name='answer_question'),
    path('results/all/', views.all_results, name='all_results'),
    path('results/<int:candidate_id>/', views.interview_results, name='interview_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)