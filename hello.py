def test(x):
    if(x>0):
        x=x*x
    else:
        print("Error")
    return x

def res():
    for i in range(-5,5):
        x=i
        res1=test(x)
        print(res1)

res()