def decrypt():
    encrypted_message = input("Enter the message i.e to be decrypted: ").strip().casefold()
    letters = "abcdefghijklmnopqrstuvwxyz"
    k = int(input("Enter the key to decrypt: "))
    decrypted_message = ""
    for ch in encrypted_message:
        if ch in letters:
            new_pos = (letters.find(ch) - k) % 26
            decrypted_message += letters[new_pos]
        else:
            decrypted_message += ch
    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()
