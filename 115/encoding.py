import base64


#byte string Vs string
##string = b"abcdefghijk"
##print(string)
##print('type of b\'...\' string:', type(string))

#encode a string
#string.encode()
##string = "abcdefghijk".encode()
##print(string)
##print('type string.encode():', type(string))

#default is unicode
##string = "ƕƖƗƐƑƒƓƜƝƞƟ".encode()
##string = "ƕƖƗƐƑƒƓƜƝƞƟ".encode("utf-8")
##print(string)
##string = "ƕƖƗƐƑƒƓƜƝƞƟ".encode("utf-16")
##print(string)
##string = "ƕƖƗƐƑƒƓƜƝƞƟ".encode("ascii")


#decode a string
#string.decode()
#'str' object has no attribute 'decode'
##string = "ƕƖƗƐƑƒƓƜƝƞƟ".decode()

#bytestring can have only ascii chars
##string = b"ƕƖƗƐƑƒƓƜƝƞƟ".decode()

#decode a valid byte string
##string = b'\xc6\x95\xc6\x96\xc6\x97\xc6\x90\xc6\x91\xc6\x92\xc6\x93\xc6\x9c\xc6\x9d\xc6\x9e\xc6\x9f'.decode()
##print(string)

#a bytes-like object is required, not 'str'
##basedString = base64.b64encode("ƕƖƗƐƑƒƓƜƝƞƟ")

#encode to base64
##basedString = base64.b64encode("ƕƖƗƐƑƒƓƜƝƞƟ".encode())
##print(basedString)

#encode to base32
##basedString = base64.b32encode("ƕƖƗƐƑƒƓƜƝƞƟ".encode())
##print(basedString)

#encode to base16
##basedString = base64.b16encode("ƕƖƗƐƑƒƓƜƝƞƟ".encode())
##print(basedString)





