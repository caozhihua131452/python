# content-type

django内置的一个组件。 使用与一张表同时关联多张表。

```python
'django.contrib.contenttypes',
```

可以用于多张表 同一属性的关联， 直接关联表名，和表字段的id。 



### 1.多张表关联



![content-tpye](.\images\content-type.png)



### 2.数据库设计如下

``` python
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Course(models.Model):
    title = models.CharField(max_length=32)

    # 不生成数据库列，GenericRelation仅用于反向查找  前提是用content_type
    price_policy_list = GenericRelation('PricePolicy')


class DegreeCourse(models.Model):
    title = models.CharField(max_length=32)

    # 不生成数据库列，GenericRelation仅用于反向查找  前提是用content_type
    price_policy_list = GenericRelation('PricePolicy')


class PricePolicy(models.Model):
    price = models.IntegerField()
    period = models.IntegerField()

    # Table_name = models.CharField(verbose_name='关联表名称')
    # object_id = models.CharField(verbose_name='关联表中数据行的id')

    content_type = models.ForeignKey(ContentType, verbose_name='关联表名称', on_delete=False)
    object_id = models.IntegerField(verbose_name='关联表中数据行的id')

    # 插入入数据专用  快速实现content_type操作， 和字段列无任何关系
    content_object = GenericForeignKey('content_type', 'object_id')

"""
ContentType  自动创建一张表， 把数据库中的所有表名称放到这张表里。 

"""
# 正常插入操作
# obj = DegreeCourse.objects.filter(title='python全栈').first()
# cobj = ContentType.objects.filter(model='course').first()
# PricePolicy.objects.create(price='6.6', period='30', content_type_id=cobj.id, object_id=obj.id)

# 如果用了 content_object = GenericForeignKey('content_type', 'object_id')
# obj = DegreeCourse.objects.filter(title='python全栈').first()
# PricePolicy.objects.create(price='6.6', period='30', content_object=obj)
```



### 3. 视图函数和路由函数如下。

``` python
from django.shortcuts import render, HttpResponse
    
def add_course(request):
    # 如果用了 content_object = GenericForeignKey('content_type', 'object_id')

    # 增加课程， 并且自关联的增加了外键的两列
    # 增加 PricePolicy 表的所有数据， 并关联了 DegreeCourse表的数据
    obj = models.DegreeCourse.objects.filter(title='python全栈').first()
    models.PricePolicy.objects.create(price=19.9, period=60, content_object=obj)

    # 增加 PricePolicy 表的所有数据， 并关联了 DegreeCourse表的数据
    obj = models.DegreeCourse.objects.filter(title='python全栈').first()
    models.PricePolicy.objects.create(price=29.9, period=90, content_object=obj)
    return HttpResponse('ok')


def get_course(request):

    # 查找与课程相关的数据。
    degree = models.DegreeCourse.objects.filter(id=2).first()
    price_policys = degree.price_policy_list.all()
    print(price_policys) #<QuerySet [<PricePolicy: PricePolicy object (4)>, <PricePolicy: PricePolicy object (5)>]>
    return HttpResponse('ok')


# 路由
path('course/', views.course),

```



1