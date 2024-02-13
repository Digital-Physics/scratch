def logic(x, y):
    return y and x

test_y = [] # Falsy
text_x = "this is a Str argument; not a Bool"

print("Falsy y: ", logic(text_x, test_y))

test_y = ["something"] # Truthy
text_x = "this is a Str argument; not a Bool"

print("Truthy y: ", logic(text_x, test_y))

test_y = {1, 2, 3}
test_x = {2, 3, 4}

print("A non-empty set is Truthy, but an 'Intersection' seems to be a more intuitive interpretation of what an 'and' should do here: ", logic(test_x, test_y))

def logic2(x, y):
    return y & x

print("Let's use this '&' for sets, not 'and': ", logic2(test_x, test_y))