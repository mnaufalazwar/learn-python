#import modul / file lain
import function
import dir1.function1 as func1

#jika ingin import fungsi tertentu
from function import total
from function import say_hello

#built in module
import platform

hello = function.say_hello("naufal")
print(hello)

print(total(1,2,3))

print(platform.system())

print(func1.say_hello1("azwar"))