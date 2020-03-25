from django.contrib import admin
from .models import Threaddb,threadcontentdb,thread_deleterequestdb,manager_userdb,threadcontent_deleterequestdb

admin.site.register(Threaddb)
admin.site.register(threadcontentdb)
admin.site.register(thread_deleterequestdb)
admin.site.register(manager_userdb)
admin.site.register(threadcontent_deleterequestdb)

# Register your models here.
