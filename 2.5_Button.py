# from gpiozero import Button

# button = Button(2)

# button.wait_for_press()
# print("Button was pressed!")


# while True:
#     if button.is_pressed:
#         print("Button is pressed")
#     else:
#         print("Button is not pressed")



# from gpiozero import Button
# from signal import pause

# def say_hello():
#     print("Hello!") 

# button = Button(2)
# button.when_pressed = say_hello
# pause()


from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

button = Button(2)

button.when_pressed = say_hello
button.when_released = say_goodbye
pause()