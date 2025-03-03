from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('avatar/', include('avatar.urls')),
    path('users/', include('users.urls', namespace='users')),
    # Optional: Uncomment the following line to make the homepage point to your custom template
    # path('', TemplateView.as_view(template_name="home.html"), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
