from encode_decode import encode_message,decode_message

MAIN_MENU = """
Options:
    1. Encode Text to morse code
    2. Decode Text from morse code
    3. Exit
Note: you can press CTRL+C or type "Exit" and hit [enter] to exit the programm.
"""

if __name__ == "__main__":
    selected_option = 0
    while True:
        print(MAIN_MENU)
        
        x = input()
        if x.lower()=="exit":
            break
        try:
            selected_option = int(x)
        except ValueError:
            continue

        if selected_option==1:
            try:
                msg = input("Enter text to convert in morse code: ")
                print(encode_message(msg))
            except KeyboardInterrupt:
                selected_option = 0
        elif selected_option==2:
            try:
                msg = input("Enter morse code to convert in text: ")
                print(decode_message(msg))
            except KeyboardInterrupt:
                selected_option = 0
