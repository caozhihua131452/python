## flask-migrate

### 1.flask 实现命令迁移数据库。

下载依赖环境：

​	   ` pip install flask-migrate`

- 第一步：`from flask_migrate import Migrate, MigrateCommand   `

- 第二步： `migrate = Migrate(app, db)   `

- 第三步：`manage.add_command('db', MigrateCommand) `

### 2.执行迁移命令：

```python
	python manage.py db init           #  初始化    第一次的时候使用
    python manage.py db migrate        #  本地生成迁移文件
    python manage.py db upgrade        #  提交到数据库
```
### 3.下边是代码的具体实例

``` python
from flask_script import Manager
from utils import create_app
from flask_migrate import Migrate, MigrateCommand   

from user.models import db


app = create_app()
migrate = Migrate(app, db)         


if __name__ == '__main__':
    manage = Manager(app)
    """
    数据库迁移命令：
        python manage.py db init         初始化    第一次的时候使用
        python manage.py db migrate      本地迁移
        python manage.py db upgrade      提交到数据库
    """
    manage.add_command('db', MigrateCommand)  # 添加migrate这条命令    
    manage.run()
```

