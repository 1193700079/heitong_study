def f(a,b=3,*args,**kwargs): #function object
    aa = 1
    bbb = 2
    pass

print(f.__code__)

print(dir(f.__code__))

code = f.__code__

print(code.co_code) # 查看字节码

import dis
print(dis.dis(f))


print(code.co_name)
print(code.co_filename)
print(code.co_lnotab)


print(code.co_flags) #15
print(code.co_stacksize) #1


def fun(a,b=3,/,*args,**kwargs):
    print("a+b",a+b)
    pass
code = fun.__code__
print(code.co_argcount) #2
print(code.co_posonlyargcount) #2 
print(code.co_kwonlyargcount) #0


fun(1)
fun(1, 1)
# fun(a=1)  error



def f2(a):
    b = a
    c = 1
    s = "aaba"
    return b


code = f2.__code__

print(code.co_nlocals) #2
print(code.co_varnames) #('a', 'b')
print(code.co_cellvars) #()
print(code.co_freevars) #()
print(code.co_consts) #(None,)


