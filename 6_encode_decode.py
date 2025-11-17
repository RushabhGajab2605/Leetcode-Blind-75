def encode(strs):
    encode_str = ""
    for word in strs:
         encode_str = encode_str + str(len(word)) + "#" + word

    return encode_str

def decode(s):
    decode_arr = []
    i = 0
    while(i < len(s)):
        j = i
        while (s[j] != "#"):
            j = j + 1
        element_len = int(s[i:j])
        decode_arr.append(s[j+1:j+element_len+1])
        i = j+element_len+1

    return decode_arr

encode_op = encode(["neet","code","love","you"])
print(encode_op)
print(decode(encode_op))



