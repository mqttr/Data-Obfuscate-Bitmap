'''
Generic Examples:
FILEHEADER
    42 4d              BM
    00 00 00 00        File Size
    00 00              Reserved 01
    00 00              Reserved 02
    36 00 00 00        Offset to pixel array (36 hex)

BITMAPINFOHEADER:

        28 00 00 00    Size of header (40)

        32 00 00 00    width signed
        32 00 00 00    height signed

    CONSTANT:
        01 00          # of planes (1)
        18 00          Bits per Pixel (1, 4, 8, 16, 24, 32)
        00 00 00 00    Compression (0)
        00 00 00 00    image size (if compression == 0: = 0)
        23 2e 00 00    horizontal resolution (pixel per meter)
        23 2e 00 00    vertical resolution (pixel per meter)
        00 00 00 00    Number of colors in color palette, or 0 = 2^n
        00 00 00 00    Nymber of iportant coors used, = 0


'''

DEFAULT_HEADER = [
    '42','4d',                           # Signature
    '3a','00','00','00',                 # File Size
    # mqtt = 6D 71 74 74
    '6d','71',                           # Reserved 1
    '74','74',                           # Reserved 2
    '00','00','00','00'                  # Offset
]

DEFAULT_BITMAPINFOHEADER = [
    # CONSTANT
        '28', '00', '00', '00',          # Size of header (40)
    # INCONISTENT
        '01', '00', '00', '00',          # Width signed
        '01', '00', '00', '00',          # Height signed
    # CONSTANT:
        '01', '00',                      # of planes (1)
        '18', '00',                      # Bits per Pixel (1, 4, 8, 16, 24, 32)
        '00', '00', '00', '00',          # Compression (0)
        '00', '00', '00', '00',          # Image size (if compression == 0: = 0)
        '13', '0b', '00', '00',          # Horizontal resolution (pixel per meter)
        '13', '0b', '00', '00',          # Vertical resolution (pixel per meter)
        '00', '00', '00', '00',          # Number of colors in color palette, or 0 = 2^n
        '00', '00', '00', '00'           # Number of important colors used, = 0
]

DEFAULT_IMAGE_24 = [ 'ff','ff','ff' ]

DEFAULT_FULLBMP = [] + DEFAULT_HEADER + DEFAULT_BITMAPINFOHEADER + DEFAULT_IMAGE_24 + [ '00' ] # to get multiple of 4 bytes per line

# File Header Offsets

HEADER_OFFSET_EXTENSION                = 0
HEADER_OFFSET_SIZE                     = 2
HEADER_OFFSET_RESERVED1                = 6
HEADER_OFFSET_RESERVED2                = 8
HEADER_OFFSET_OFFSET                   = 10
HEADER_OFFSET_DIB_HEADER               = 14

# BITMAPINFOHEADER Offsets

INFOHEADER_OFFSET_SIZE                     = 0
INFOHEADER_OFFSET_WIDTH                    = 4
INFOHEADER_OFFSET_HEIGHT                   = 8
INFOHEADER_OFFSET_PLANES                   = 12
INFOHEADER_OFFSET_BITSPERPIXEL             = 14
INFOHEADER_OFFSET_COMPRESSION              = 16
INFOHEADER_OFFSET_RAW_SIZE                 = 20
INFOHEADER_OFFSET_HORIZONTAL_RESOLUTION    = 24
INFOHEADER_OFFSET_VERTICAL_RESOLUTION      = 28
INFOHEADER_OFFSET_COLOR_PALETTE            = 32
INFOHEADER_OFFSET_IMPORTANT_COLORS         = 36
