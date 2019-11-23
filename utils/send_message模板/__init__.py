import importlib
from .settings import MSG_LIST


def send_msg(msg):
    for path in MSG_LIST:
        m, c = path.rsplit('.', maxsplit=1)
        md = importlib.import_module(m)
        obj = getattr(md, c)()
        obj.send(msg)

