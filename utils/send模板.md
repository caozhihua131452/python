## 发射实现send模板

定义好模板， 实现了更改配置文件，增加删除，send方法， 

主文件则不需要更改。

``` python
# base.py
class Base(object):

    def send(self):
        raise NotImplementedError('.........')

        
# msg.py        
from .base import Base


class Message(Base):

    def __init__(self):
        self.username = 'caoge'
        self.pwd = 'caoge'

    def send(self, msg):
        print(msg, '发送信息')        
   
# email.py
from .base import Base


class Email(Base):

    def send(self, msg):
        print(msg,'发送邮件')

# settings.py
MSG_LIST = {
     'utils.message.email.Email',
     'utils.message.msg.Message',
}

# __init__.py
import importlib
from .settings import MSG_LIST


def send_msg(msg):
    for path in MSG_LIST:
        m, c = path.rsplit('.', maxsplit=1)
        md = importlib.import_module(m)
        obj = getattr(md, c)()
        obj.send(msg)

# index.py
from utils.message import send_msg

send_msg('msg')

```

