import time


def debuger(func):
    from django.db import connection

    def inner(*args, **kwargs):
        result = func(*args, *kwargs)
        print('----'*50)
        for query in connection.queries:
            print(query['sql'], query['time'])
        print('----'*50)
        return result
    return inner