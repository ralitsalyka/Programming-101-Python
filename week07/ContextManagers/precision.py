from contextlib import contextmanager


from decimal import *


@contextmanager
def change_precision(precision):
    try:
        old_prec = getcontext().prec
        getcontext().prec = precision
        yield
    except Exception:
        raise
    finally:
        getcontext().prec = old_prec


class ChangePrecision:

    def __init__(self, precision):
        self.valid_precision(precision)
        self.precision = precision

    def __enter__(self):
        self.precision = getcontext().prec
        getcontext().prec = self.precision
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        getcontext().prec = self.first_precision

    @staticmethod
    def valid_precision(precision):
        if not isinstance(precision, int):
            raise TypeError("Type Error!")
        elif precision < 0:
            raise ValueError("Value Error!")


'''
with change_precision(2):
    print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.4

print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.355452132
'''
