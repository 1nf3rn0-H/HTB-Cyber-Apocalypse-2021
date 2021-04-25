def decrypt(message_bytes, key):
  decrypted = b''
  i = 0
  for byte in message_bytes:
    # Go back to the beginning of the key if we've reached it's length.
    # This handles the "repeating" bit of the key.
    if (i == len(str(key))):
      i = 0

    # Convert the key char to a number so it can be XOR'd
    xor = byte ^ key
    
    # Convert the xor'd value back to bytes... bytes(...) requires an
    # array as an argument, hence the [...]
    decrypted += bytes([xor])
    i += 1
  return decrypted


buf = ""

#we will search this after deciphering
res = "CHTB{"

with open("output.txt", "r") as fil:
	data = fil.read()
    
    #convert the data to the list
	data = data.split("\n")
    
	for i in data:
        #convert it into bytes
		mes = bytearray.fromhex(i)
        
        #iterate through all possible single byte hex values
		for j in range(256):
			key = '{}'.format(hex(j).replace("0x","")).encode()
			ans = decrypt(mes,j)
            
            #not all decrypted text can be displayed as ASCII text
			try:
				if res in ans.decode():
					print(ans)
					break
			except UnicodeDecodeError:
                #you can just use pass here instead
				buf += str(ans) + "\n"
			
#you can ignore the below code if you are not interested in decrypted text
with open('ana.txt',"a") as fil:
	fil.write(buf)
	fil.close()
