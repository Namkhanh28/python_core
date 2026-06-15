import first_module as first_module
import display.say_goodbye
from display.say_goodbye import say_hi

print(first_module.NAME)
first_module.sayHello()
display.say_goodbye.sayBye(first_module.NAME)
display.say_goodbye.say_hi("Nam")