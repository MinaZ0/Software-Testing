def caesarCipher(s, k):
    result = []
    k = k % 26
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)