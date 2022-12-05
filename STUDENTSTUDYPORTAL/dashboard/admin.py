from django.contrib import admin
from .models import *


# -------------- Notes section --------------------#

admin.site.register(Notes)

# -------------- Homework section --------------------#

admin.site.register(Homework)

# -------------- To Do section --------------------#

admin.site.register(Todo)


