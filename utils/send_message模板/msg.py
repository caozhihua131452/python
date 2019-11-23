from .base import Base


class Message(Base):

    def __init__(self):
        self.username = 'caoge'
        self.pwd = 'caoge'

    def send(self, msg):
        print(msg, '发送信息')