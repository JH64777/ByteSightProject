const Checker = function(btnid, inputid, flagString){ // 버튼 아이디, 입력창 아이디, 백엔드에서 구분할때 쓰는 분류 기호
    if(document.getElementById(btnid).value != ""){
        fetch("/signup/check", {
            method: "POST",
            headers: {"Content-Type": "application/json",},
            body: JSON.stringify({
                contents : document.getElementById(inputid).value,
                flag : flagString
            })   
        })
        .then((reply) => reply.json())
        .then((message) => {
            alert(message.msg);
        })
        .catch(error => console.log(error));
    }
    else
        alert("빈 칸 없이 입력해주세요!");
}

const checknick = document.getElementById("checknick");
checknick.addEventListener("click", Checker("checknick", "nickname", "Nick"));

const checkid = document.getElementById("checkid");
checkid.addEventListener("click", Checker("checkid", "id", "ID"));