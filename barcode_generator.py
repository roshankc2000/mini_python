# bar_code maker
# by @itsroshankc in github

import barcode
from barcode import UPCA
from barcode.writer import ImageWriter

# take input to make desired barcode
message = input("Enter 12 digit serial number :")

# Now, let's create an object of EAN13 class and
# pass the number with the ImageWriter() as the writer
generated_barcode = UPCA(message, writer=ImageWriter())


# lets save the image with desired file name
naam = input("Save file as (name):")
generated_barcode.save(naam)


# help code
"""
Supported formats
The python-barcode library supports several barcode formats:

Code 39
It includes uppercase letters, numeric digits, and some special characters. It can be of variable length up to the size of the barcode.
Code 128
It includes uppercase letters, lowercase letters, numeric digits, and some special characters. It can be of variable length up to the size of the barcode.
PZN7
It is a variant of Code 39 which encodes 6 digits + 1 check digit. This type of barcode is mostly used for pharmaceutical products in Germany.
EAN-13
It includes 12 digits + 1 check digit and is used to encode GTIN-13 (global trade item number) used mainly outside of North America.
EAN-8
It includes 7 digits + 1 check digit and is used to encode GTIN-8 (global trade item number) used mainly outside of North America.
JAN
JAN (Japanese Article Numbering) is a variant of EAN-13 where the first two digits must be 45 or 49 (Japan).
ISBN-13
ISBN-13 (International Standard Book Number) is similar to EAN-13 with a special prefix.
ISBN-10
ISBN-10 (International Standard Book Number) is a subtype of ISBN-13 which was use up to 31/12/2005.
ISSN
ISSN (International Standard Serial Number) uses an 8 digit code to uniquely identify publications, magazines, and more.
UPC-A
UPC-A is a standard version of UPC (Universal Product Code) which consists of 12 digits.
EAN-14
It includes 14 digits and is used to encode GTIN-14 (global trade item number) used for traded goods.
GS1–128
It is a variant of Code 128 and is used for goods in commerce and industry. This type of barcode can include more than one data field.
"""
