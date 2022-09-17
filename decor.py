from datetime import datetime
from functools import wraps


# simple decorator
def logger(old_func):

    @wraps(old_func)
    def new_func(*args, **kwargs):
        func_call = datetime.now()
        res = old_func(*args, **kwargs)
        with open('logs/info.log', 'a+') as file:
            info = file.writelines(f'''[datetime: {func_call}, \nname func: {old_func.__name__}, \narguments: {args} and {kwargs}, \nreturn: {res}]''')
        return res
    return new_func



def logger_with_path(path):
    def _logger_with_path(old_func):

        @wraps(old_func)
        def new_func(*args, **kwargs):
            nonlocal path
            func_call = datetime.now()
            result = old_func(*args, **kwargs)
            with open(path, 'a+') as file:
                info = file.writelines(f'''[datetime: {func_call}, \nname func: {old_func.__name__}, \narguments: {args} and {kwargs}, \nreturn: {result}]\n''')
            return result
        return new_func
    return _logger_with_path