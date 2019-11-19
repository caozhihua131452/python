# csrf_token

基于中间件process_view方法实现的。 检查视图是否被@csrf_exempt（免除scrf认证）

去请求体或cookie中获取token，根据token做校验。

### 1. 免除scrf

```python
from django.views.decorators.csrf import csrf_exempt

# 免除csrf验证
@csrf_exempt   
def course(request):
    pass


# settings.py 配置上了， 就是全局使用csrf
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### 2. 只有一个函数用

``` python
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# 全局注释了， 只有这个函数使用csrf
@csrf_protect
def course(request):
    pass
```



### 3. CBV使用csrf—token

在dispatch上加@method_decorator(csrf_protect) 才有用

``` python
from django.utils.decorators import method_decorator


# 方法一
class CourseView(View):
     
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super(CourseView, self).dispatch(request, *args, **kwags)
    
    def post(self, request, *args, **kwargs):
        pass

    
# 方法二：

@method_decorator(csrf_protect, name='dispatch')
class CourseView(View):
     
    def post(self, request, *args, **kwargs):
        pass


```

