# Python imports
import os
import builtins
import threading

# Lib imports

# Application imports
from core.utils import Logger
from core.utils import MessageHandler       # Get simple message processor


class BuiltinsException(Exception):
    ...


# NOTE: Threads WILL NOT die with parent's destruction.
def threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=False).start()
    return wrapper

# NOTE: Threads WILL die with parent's destruction.
def daemon_threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper

# NOTE: Just reminding myself we can add to builtins two different ways...
# __builtins__.update({"event_system": Builtins()})
builtins.app_name        = ':::APP TITLE:::'
builtins.threaded        = threaded_wrapper
builtins.daemon_threaded = daemon_threaded_wrapper
builtins.ROOT_FILE_PTH   = os.path.dirname(os.path.realpath(__file__))
builtins.logger          = Logger().get_logger()
builtins.json_message    = MessageHandler()
