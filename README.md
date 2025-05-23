# graphql-activities-api

## Temporarily Disable Django Admin to Avoid MongoDB Model ID Conflicts During Migration
When using MongoDB with Django, you may encounter errors related to the default ID field type during migrations. To avoid these issues, temporarily comment out certain Django contrib apps and admin-related routes:

**graph/settings.py**
In the `INSTALLED_APPS` section, comment out the following:
```
# 'django.contrib.admin',
# 'django.contrib.auth',
# 'django.contrib.contenttypes',
# 'django.contrib.messages',
```

Example:
```
INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    "graphene_django",
    "activities",
    "corsheaders",
]
```


**graph/urls.py**
Comment out the admin import and URL pattern:

```
# from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
```

🔄 Important: Remember to uncomment these lines after completing the migration to restore full admin functionality.
