from django.contrib import admin
from django.urls import path, include
from register import views as v
print("ESTO ES V " + str(v))
urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),  # <-- added
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
]
