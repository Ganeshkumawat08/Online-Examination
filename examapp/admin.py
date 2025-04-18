from django.contrib import admin
from .models import usermodel
from .forms import userform

from .models import coursemodel
from .models import subjectmodel
from .models import papermodel
from .models import resultcoursemodel
from .models import resultsubjectmodel


# Register your models here.

class signupuser(admin.ModelAdmin):
    form = userform

admin.site.register(usermodel,signupuser)


admin.site.register(coursemodel)
admin.site.register(subjectmodel)
admin.site.register(papermodel)
admin.site.register(resultcoursemodel)
admin.site.register(resultsubjectmodel)

