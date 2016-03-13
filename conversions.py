char_map = { "a" : 10, "b" : 11, "c" : 12, "d" : 13, "e" : 14, "f" : 15 } 
for i in range(10):
    char_map[str(i)] = i

dec_to_hex_map = { 10 : "a", 11 : "b", 12 : "c", 13 : "d", 14 : "e", 15 : "f" }
for i in range(10):
    dec_to_hex_map[i] = str(i)

def hex_to_dec(string):
    string = string[::-1]
    i = 0   
    result = 0
    while i < len(string):
        result += (16**i) * char_map[string[i]] 
        i += 1
    return result

def dec_to_hex(n):
    result = ""
    while n:
        result = dec_to_hex_map[n % 16] + result
        n /= 16
    return result

def dec_to_binary(n):
    pass

def binary_to_dec(string):
    pass

def main():
    print hex_to_dec("bbaa")
    print dec_to_hex(48042)
    print binary_to_dec("101010010001")
    print dec_to_binary(9001)

main()
       
