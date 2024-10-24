from io import BytesIO

def AppendTail(cover, secret): # 뒤에 값을 붙이는 방식의 스테고이미지 생성기
    newData = cover + secret # 커버 이미지에 대한 바이너리 데이터 뒤에 숨겨지는 파일의 바이너리 값을 넣는다.
    signature = "image/jpeg" # MIME Type 설정
    
    return BytesIO(newData), signature # 생성된 스테가노그래피 이미지 데이터와 확장자(MIME Type)
