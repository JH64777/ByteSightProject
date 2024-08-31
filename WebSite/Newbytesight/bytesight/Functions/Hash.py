import hashlib
from django.utils import timezone
import uuid

def Hashing(data): # 해시 함수
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    
    return sha256.hexdigest()

def MakeName(): # 랜덤한 문자열 반환 시간 + uid를 해싱한 값
    uid = uuid.uuid4()
    randomString = str(timezone.now()) + uid.hex
    print(uid.hex)
    newName = Hashing(randomString)

    return newName