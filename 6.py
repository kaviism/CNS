# To write a python program for play fair decryption.

matrix = [['M', 'O', 'N', 'A', 'R'],
         ['C', 'B', 'Y', 'F', 'X'],
         ['D', 'E', 'G', 'H', 'I'],
         ['K', 'L', 'P', 'Q', 'S'],
         ['T', 'U', 'V', 'W', 'Z']]

def playfair_encode(message):
    message = message.upper()
    message = message.replace('J', 'I')
    message = message.replace(' ', '')
    if len(message) % 2 != 0:
        message += 'X'
    ciphertext = ''
    for i in range(0, len(message), 2):
        a = message[i]
        b = message[i+1]
        a_row, a_col = 0, 0
        b_row, b_col = 0 , 0
        for row in range(len(matrix)):
            if a in matrix[row]:
                a_row = row
                a_col = matrix[row].index(a)
            if b in matrix[row]:
                b_row = row
                b_col = matrix[row].index(b)
        if a_row == b_row:
            ciphertext += matrix[a_row][(a_col+1)%6]
            ciphertext += matrix[b_row][(b_col+1)%6]
        elif a_col == b_col:
            ciphertext += matrix[(a_row+1)%5][a_col]
            ciphertext += matrix[(b_row+1)%5][b_col]
        else:
            ciphertext += matrix[a_row][b_col]
            ciphertext += matrix[b_row][a_col]
    return ciphertext

message = 'Must see you over Cadogan West. Coming at once.'
ciphertext = playfair_encode(message)
print(ciphertext)

