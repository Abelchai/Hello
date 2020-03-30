print('****Welcome!****')
print("type 'help' for details")
started = False
while True:
    command=str(input('>'))
    if command == 'help':
        print('''
start--start the car
stop--stop the car
quit--quit the game''')
    elif command == 'start':
        if started:
            print('Your car has already started!!')
        else:
            started = True
            print("Your car has been started!")
    elif command == 'stop':
        if not started:
            print('Your car has already stopped!!')
        else:
            started = False
            print("Your car has stopped!")
    elif command == 'quit':
        print("Exiting...")
        break
    else:
        print("Sorry,I don't understand...")
