alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(start_text, shift_num, direction):
    plain_text = ""
    if direction == "decode":
        shift_num *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_num
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the {direction}d result: {plain_text}")

should_continue = True
while should_continue
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    from art import logo
    print (logo)
    shift = shift % 26
    ceaser(text, shift, direction )
    result = input("Type 'yes' if you want to continue. Otherwise type 'no'. \n").lower()
    if result == "no":
        should_continue = False
        print("GoodBye")

