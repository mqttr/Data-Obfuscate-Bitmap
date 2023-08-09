import bmpconstants as CONSTANTS
import math
import sys



class bmpreader:

    def __init__(self, fileHandle):
        self.fileHandle = fileHandle
        self.hex = [ hex(ele)[2:].zfill(2) for ele in bytes(fileHandle.read()) ]
        fileHandle.seek(0)
        return
    
    def grab_data(self):
        print(self.hex[CONSTANTS.HEADER_OFFSET_OFFSET])
        return 

    def __str__(self):
        return self.hex

    

class bmpbuilder:

    def __init__(self, fileHandle):
        self.__fileHandle = fileHandle
        self.__fileHeader = CONSTANTS.DEFAULT_HEADER
        self.__dibHeader = CONSTANTS.DEFAULT_BITMAPINFOHEADER
        self.__data = []
        
        self.set_data(CONSTANTS.DEFAULT_IMAGE_24)

        return

    def complete_data(self):
        return [] + self.__fileHeader + self.__dibHeader + self.__data


    def write(self): # Saves bmpbuilder bmp to disk
        # Set resolution

        # Saving to disk 
        fileBytes = bytes()
        for eleHex in bmpbuilder.complete_data(self):
            fileBytes += bytes.fromhex(eleHex)
        self.__fileHandle.write(fileBytes)

        return self.__fileHandle

    def set_data(self, hexList):
        self.__data = hexList + ['00']*((3 - (len(hexList)%3) ) %3 ) # Completes all data pixels

        # Force Square image by added blank pixels at the end
        pixelCount = self.side_length()**2
        requiredHexCount = pixelCount*3
        self.__data += ['00']*(requiredHexCount-len(self.__data))

        # updating other markers to agree with new data
        self.generate_resolution()
        self.generate_padding()
        self.generate_size()

        return self.complete_data()

    def generate_padding(self):
        data = self.__data
        side = self.side_length()
        requiredPadding = (4-((3*side) %4 ) ) %4

        endLine = side*3

        for line in range(side):
            for requiredpad in range(requiredPadding):
                self.__data.insert(endLine+endLine*line+requiredPadding*line, '00')

        return self.__data

    def generate_size(self):        
        sizeArray = []
        data = self.complete_data()
        
        sizeString = hex(len(data))[2:].zfill(8).lower()

        for i in range(0,len(sizeString),2):
            sizeArray.append( sizeString[i] + sizeString[i+1] )

        sizeArray.reverse()
        for i,hexElement in enumerate(sizeArray):
            self.__fileHeader[i + CONSTANTS.HEADER_OFFSET_SIZE] = hexElement

        return str(sizeArray)

    def generate_resolution(self):
        side = self.side_length()
        sideArray = []

        sizeString = hex(side)[2:].zfill(8).lower()

        for i in range(0,len(sizeString),2):
            sideArray.append( sizeString[i] + sizeString[i+1] )

        sideArray.reverse()
        for i,hexElement in enumerate(sideArray):
            self.__dibHeader[i + CONSTANTS.INFOHEADER_OFFSET_WIDTH] = hexElement

        for i,hexElement in enumerate(sideArray):
            self.__dibHeader[i + CONSTANTS.INFOHEADER_OFFSET_HEIGHT] = hexElement

        return sideArray

    def side_length(self):
        return math.ceil( math.sqrt(len(self.__data) //3 ) )

    def __str__(self):
        return str(self.complete_data())

if __name__ == "__main__":
    with open('bmp.bmp', 'rb') as file:
        oldBMP = bmpreader(file).grab_data()
    
    # with open('bmp.bmp', 'wb') as file:
    #     newBMP = bmpbuilder(file)
    #     data = [
    #         'ff','ff','ff','ff','ff','ff','ff','ff','ff',
    #         'ff','ff','ff','ff','ff','ff','ff','ff','ff',
    #         'ff','ff','ff','ff','ff','ff','ff','ff',
    #     ]
        
    #     newBMP.set_data(data)
    #     print(newBMP)
    #     newBMP.write()