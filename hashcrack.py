import hashlib, os, sys
from warn import *
kuni = '\x1b[33m'
class base85:
 def hasher(kont):
  import base64
  encb85 = base64.b85encode(kont)
  stripb85 = str(encb85).strip("'")
  strip1b85 = str(stripb85).strip("b'")
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b85))
 def cracker(kont1):
  import base64
  decb85 = base64.b85decode(kont1)
  stripb85 = str(decb85).strip("'")
  strip1b85 = str(stripb85).strip("b'")
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b85))
class base64:
 def hasher(kimi):
  import base64
  encb64 = base64.b64encode(kimi)
  stripb64 = str(encb64).strip("'")
  strip1b64 = str(stripb64.strip("b'"))
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b64))
 def cracker(kimi1):
  import base64
  decb64 = base64.b64decode(kimi1)
  stripb64 = str(decb64).strip("'")
  strip1b64 = str(stripb64.strip("b'"))
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b64))
class md5:
 def hasher(md):
  encmd5 = hashlib.md5(md.encode())
  print(f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+encmd5.hexdigest())
class base32:
 def hasher(kn):
  import base64
  encb32 = base64.b32encode(kn)
  stripb32 = str(encb32).strip("'")
  strip1b32 = str(stripb32).strip("b'")
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b32))
 def cracker(kn1):
  import base64
  decb32 = base64.b32decode(kn1)
  stripb32 = str(decb32).strip("'")
  strip1b32 = str(stripb32).strip("b'")
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b32))
class base16:
 def hasher(ko):
  import base64
  encb15 = base64.b16encode(ko)
  stripb15 = str(encb15).strip("'")
  strip1b15 = str(stripb15).strip("b'")
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b15))
 def cracker(ko1):
  import base64
  decb15 = base64.b16decode(ko1)
  stripb15 = str(decb15).strip("'")
  strip1b15 = str(stripb15).strip("b'")
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(strip1b15))
class binary:
 def hasher(st):
  yu = ' '.join(format(ord(x), 'b') for x in st)
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+str(yu))
 def cracker(st1):
  yuah = st1.split()
  ascci_str = ""
  for cekaja in yuah:
   yuk = int(cekaja, 2)
  asci_chr = chr(yuk)
  ascci_str = "".join([chr(int(binary, 2)) for binary in st1.split(" ")])
  print (f"{anj}----> [{kan}INFO{anj}] {kan}Hasil {anj}> {kon}"+ascci_str)

menu = ['\x1b[33mHasher','\x1b[33mCracker']
for i in range(len(menu)):
 print (f"{anj}[{ken}0"+str(i+1).ljust(1)+anj+"] "+menu[i])
pilih = str(input(f"{anj}[{kan}INPUT{anj}] {kan}Masukkan pilihan {anj}> {kun}"))
if (pilih == '1') or (pilih == '01'):
 menu1 = [kuni+'Base85','\x1b[33mBase64','\x1b[33mBase32',kuni+'Base16',kuni+'MD5 (hex)',kuni+'Binary']
 for i in range(len(menu1)):
  print (f"{anj}--> [{ken}0"+str(i+1).ljust(1)+anj+"] "+menu1[i])
 hyu = str(input(f"{anj}---> [{kan}INPUT{anj}] {kan}Masukkan pilihan {anj}> {kon}"))
 if (hyu == '1') or (hyu == '01'):
  kont = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan text{anj} > {kon}"),encoding='utf8')
  base85.hasher(kont)
 elif (hyu == '2') or (hyu == '02'):
  kimi = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan text{anj} > {kon}"),encoding='utf8')
  base64.hasher(kimi)
 elif (hyu == '3') or (hyu == '03'):
  kn = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan text{anj} > {kon}"),encoding='utf8')
  base32.hasher(kn)
 elif (hyu == '4') or (hyu == '04'):
  ko = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan text{anj} > {kon}"),encoding='utf8')
  base16.hasher(ko)
 elif (hyu == '5') or (hyu == '05'):
  md = str(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan text{anj} > {kon}"))
  md5.hasher(md)
 elif (hyu == '6') or (hyu == '06'):
  st = str(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan text{anj} > {kon}"))
  binary.hasher(st)
elif (pilih == '2') or (pilih == '02'):
 menu2 = [kuni+'Base85','\x1b[33mBase64','\x1b[33mBase32',kuni+'Base16',kuni+'Binary']
 for i in range(len(menu2)):
  print (f"{anj}--> [{ken}0"+str(i+1).ljust(1)+anj+"] "+menu2[i])
 hyu1 = str(input(f"{anj}---> [{kan}INPUT{anj}] {kan}Masukkan pilihan {anj}> {kon}"))
 if (hyu1 == '1') or (hyu1 == '01'):
  try:
   import binascii
   kont1 = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan code base85{anj} > {kon}"),encoding='utf8')
   base85.cracker(kont1)
  except binascii.Error as e:print (f"{anj}----> [{kun}ERROR{anj}] > {kun}{e}")
 elif (hyu1 == '2') or (hyu1 == '02'):
  try:
   import binascii
   kimi1 = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan code base64{anj} > {kon}"),encoding='utf8')
   base64.cracker(kimi1)
  except binascii.Error as e:print (f"{anj}----> [{kun}ERROR{anj}] > {kun}{e}")
 elif (hyu1 == '3') or (hyu1 == '03'):
  try:
   import binascii
   kn1 = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan code base32{anj} > {kon}"),encoding='utf8')
   base32.cracker(kn1)
  except binascii.Error as e:print (f"{anj}----> [{kun}ERROR{anj}] > {kun}{e}")
 elif (hyu1 == '4') or (hyu1 == '04'):
  try:
   import binascii
   ko1 = bytes(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan code base32{anj} > {kon}"),encoding='utf8')
   base16.cracker(ko1)
  except binascii.Error as e:print (f"{anj}----> [{kun}ERROR{anj}] > {kun}{e}")
 elif (hyu1 == '5') or (hyu1 == '05'):
  try:
   st1 = str(input(f"{anj}----> [{kan}INPUT{anj}] {kan}Masukkan code binary{anj} > {kon}"))
   binary.cracker(st1)
  except ValueError as e:print (f"{anj}----> [{kun}ERROR{anj}] > {kun}{e}")
