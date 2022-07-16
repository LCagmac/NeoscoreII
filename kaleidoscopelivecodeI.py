while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('a'):  # if key 'q' is pressed
            neoscore.show(refresh_func_new)
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop
