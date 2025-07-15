# fix with *

@overload
def process_data(foo):
    ...

@overload
def process_data(bar):
    ...

def process_data(foo=None, bar=None):
    if foo: 
        ...
    elif bar: 
        ...