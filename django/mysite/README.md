练习多种类型的数据存储和查看
==
# Usage
`python3 manage.py runserver 0.0.0.0:8000`
浏览器中输入"localhost:8000/admin"
输入用户名(admin)和密码(miximixi666)
* 或者直接访问我的服务器查看效果: <http://lihao2333.com:8000/admin>
# 创建模型

```python
#models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Case(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    publish = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    email = models.EmailField()
    ip = models.GenericIPAddressField()
    vip = models.BooleanField()
    score = models.FloatField()
    age = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        ordering = ("-publish",)
    def __str__(self):
        return self.title
```
* ForiegnKey经常用作选择User, 要注意从哪里import, 要注意必须选择删除方式(CASCDE)
* DecimalField 必须有decimal_places 和max_digitals
* IPAddressField已经废除, 选用GenericIPAddressField
* 图片和文件存储还没有攻克

# 数据显示

```python
#admin.py
from django.contrib import admin
from .models import Case

# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'author', 'email', 'ip' )
admin.site.register(Case, CaseAdmin)
```
