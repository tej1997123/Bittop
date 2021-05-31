import blocksmith
address_1 = str(input('Enter the btc address: ')) #'1PQc5NNSdvRwyw2RvrrQcBF4jHnmQFRkaL'
private_Key = str(input('Enter Private Key'))
sert=0
while True:    
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890') # paddress_1aphrase
  #  private_Key = paddress_1aphrase.generate_key()
    address = blocksmith.BitcoinWallet.generate_address(private_Key)
    sert+=1
    if address_1 == address:
        print("we found it ")
        print("private private_Key = ", private_Key)
        print("address = ",address)
        file = open("brutus.txt","a")

            #file.write("address: " + str(data[2]) + "\n" +

            file.write("private key: " + str(private_Key) + "\n" +

                     #  "WIF private key: " + str(toWIF(str(data[0]))) + "\n" +

                       "public key: " + str(address).upper() + "\n" +

                     #  "balance: " + str(data[3]) + "\n" +

                    #   "Donate to the author of this program:" + "\n" +

				     #  "Bitcoin: 1Np6TE5TDDresDn9LDQm3wNFnkE5zSo7eC" + "\n" +

                       "Digibyte: j")

            file.close()
        break
    else:
        print("trying private private_Key = ", private_Key)
        print("address = ",address)
        continue 
