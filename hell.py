# i=input()
# print(f"hello {i}")
def square(x):
    return x*x
def mian():
    for i in range(10):
        print("{} squared is {}".format(i,square(i)))
if  __name__=="__main()__":
    mian()
print(square(10))
