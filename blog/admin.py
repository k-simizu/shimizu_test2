from django.contrib import admin

# Register your models here.
from .models import User,Article # 追加

admin.site.register(User) # 追加
admin.site.register(Article) # 追加
