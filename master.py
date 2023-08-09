import bmp

def main():
    option = input("1. Encode into .bmp\n2. Decode from .bmp\n").strip()
    if option == '1': encode()
    elif option == '2': decode()
    else: print("Command unknown try again loser.")

def encode():
    # inputFile = input("What file would you like to obfuscate into .bmp? Include extension: ")
    # outputFile  = input("What do you want the output bitmap file to be called? Omit the extension: ") + ".bmp"
    inputFile = "test.txt"
    outputFile = "bmp.bmp"

    with open(inputFile, 'rb') as inFile:
        fileHex = [ hex(ele)[2:].zfill(2) for ele in bytes(inFile.read()) ]
        strippedHex = list(filter(lambda a: a != '0d', fileHex))
    print(strippedHex)

    with open( outputFile, 'wb') as bmpFile:
        newBMP = bmp.bmpbuilder(bmpFile)
        newBMP.set_data(strippedHex)
        newBMP.write()

def decode(name):
    with open(name, 'rb') as bmpfile:
        pass


if __name__ == "__main__":
    encode()