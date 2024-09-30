from io import BytesIO

def Extract(binaryData):
    header = binaryData[:16] # 가장 위에 줄 한 줄을 가져옴
    signature = None # 헤더 시그니처
    ext = None
    if b"\xff\xd8\xff\xe0" in header:
        signature = "image/jpeg" # 전송 파일 종류 설정
        ext = "jpg"
    elif b"\x47\x49\x46\x38\x37\x61" in header:
        signature = "image/gif"
        ext = "gif"
    elif b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a" in header:
        signature = "image/png"
        ext = "png"
    elif b"\x25\x50\x44\x46" in header:
        signature = "application/pdf"
        ext = "pdf"
    elif b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1" in header:
        signature = "application/x-hwp"
        ext = "hwp"
    elif b"\x50\x4B\x03\x04" in header:
        if b"\x77\x6F\x72\x64\x2F" in binaryData:
            signature = "application/msword"
            ext = "docx"
        elif b"\x70\x70\x74\x2F" in binaryData:
            signature = "application/vnd.ms-powerpoint"
            ext = "ppt"
        elif b"\x78\x6C\x2F" in binaryData:
            signature = "application/vnd.ms-excel"
            ext = "xlsx"
        else:
            signature = "application/zip"
            ext = "zip"
    else:
        signature = "application/octet-stream"
        ext = "txt"
    return BytesIO(binaryData), signature, ext # 파일 객체, 파일 종류에 대한 정보 반환