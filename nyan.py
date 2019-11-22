import tarfile
import io
import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

r=sys.argv[1]
X_X = 'errornyan'

won=r.count('\\')
r2=r
while won != 0:
	r1=r.find('\\')
	won = won -1
	r2=r[r1+1:]
	r=r2

sainc1 = r2.encode("UTF-8")
rem = hashlib.sha256(sainc1).hexdigest()
if rem == '1dfaac277f79e7b02f4327730848181d3d28fbd5b63ff772a0fc20d1e9ea0813':
    print('OK')
else :
    print('NG')

f=open(r,"rb")


crytext1 = b'\x80\x45\x3E\x79\xD2\x12\x45\x31\x0E\x7E\xBF\x2F\x56\x86\x72\xF1\x52\x00\x4A\xE6\x7A\x4F\x65\x99\xA0\x1E\x0F\x97\xFC\xA0\xF7\x95'
crytext2 = b'\xB3\xB6\x8A\x31\x66\xA1\x3F\xC1\xA7\xB2\xB9\xFF\x49\x99\x5F\x2A\xEE\x2B\x5B\xF3\xD4\xD2\xC1\x24\x56\xFD\x2D\xF2\xCA\x80\x1F\xBA'
keydata = f.read(16)
ivdata = f.read(16)
ivdata1 = f.read(16)
f.seek(10000000)
keydata2 = f.read(16)

obj2 = AES.new(keydata, AES.MODE_CBC, ivdata)
unobj2=unpad(obj2.decrypt(crytext1), 16)
evedata= hashlib.sha256(unobj2).hexdigest()
text1 = unobj2.decode("UTF-8")


obj3 = AES.new(keydata, AES.MODE_CBC, ivdata1)
unobj3=unpad(obj3.decrypt(crytext2), 16)
eve1data= hashlib.sha256(unobj3).hexdigest()
text2 = unobj3.decode("UTF-8")

if evedata == 'a4ffcd6b799be6f2ea8fdf6a6cb500313952d10aa6b9baa01af76aa9af56aac8' and eve1data == '3a8a670f70b4ba3ac96144d61f2d83a39d315cd9cefdfe57c692523d61665c73':
    print('OK')
else :
    print('NG')

crytext3 = b'\x18\x8B\x95\xC9\x67\xBD\xE1\xE6\xBB\xD3\x12\x30\x20\x90\x20\x14'
crytext4 = b'\x20\x93\x32\xEE\x05\x5D\x74\x0D\xEB\x26\x32\xBB\x33\x59\x39\x3C'

obj1 = AES.new(keydata2, AES.MODE_ECB)
obj0 = AES.new(keydata2, AES.MODE_ECB)
unobj1 = unpad(obj1.decrypt(crytext3), 16)
unobj0 = unpad(obj0.decrypt(crytext4), 16)
nekomimi = int(unobj1.decode("UTF-8"))
gido = int(unobj0.decode("UTF-8"))

f.seek(0)
f.seek(nekomimi)
data = f.read()
f.close()


z=io.BytesIO(data)
zzok=tarfile.open(fileobj=z, mode='r:gz')
yaong = zzok.extractfile(text1)
zzokzzok=yaong.read()
zzokzzokyaong = io.BytesIO(zzokzzok)
ddol3=tarfile.open(fileobj=zzokzzokyaong, mode='r')
ddol3jusik=ddol3.extractfile(text2)
ddol3jusik.seek(gido)
sonic = ddol3jusik.read(8)
sainc = sonic + b'\x00\x00\x00\x00\x00\x00\x00\x00'

supersoinc = hashlib.sha256(sainc).hexdigest()
if supersoinc == 'e8472a7ea907b029e1b4ba6a4b40dfe9060d84d2482b657d81189423d054c907':
    X_X = 'nyan'
    print('OK')
else :
    X_X = 'ngnyan'
    print('NG')
    
cuteson=open(X_X,"wb")
cuteson.write(sainc)
cuteson.close()

#쪽쪽야옹!