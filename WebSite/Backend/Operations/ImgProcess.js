const multer = require("multer"); // 사진, 영상 등을 올리기 위해 사용한 모듈
const path = require("path");

const storage = multer.diskStorage({ // 업로드 되는 파일에 대한 설정
    destination: function (req, file, cb) {
        let uploadPath;
        let error = null;
        console.log(file.fieldname);
        if (file.fieldname === "AI_Img") {
          uploadPath = path.join(__dirname, "../Img/AI_Img"); // 인공지능 관련 이미지 저장 경로
        } else if (file.fieldname === "post") {
          uploadPath = path.join(__dirname, "../Img/postImg"); // 게시글에 들어가는 이미지 저장 경로
        } else {
            console.log("알수 없는 접근입니다.");
            error = Error;
        }
        cb(error, uploadPath);
      },
    
      filename: function (req, file, cb) {
        if(req.sessionNickname == undefined)
        {
            cb(null, Date.now() + 'Unknown' + path.extname(file.originalname)); // 파일 이름 설정
            console.log("로그인 안됨");
        }
        else
        {
            cb(null, Date.now() + req.session.id + path.extname(file.originalname)); // 파일 이름 설정
            console.log("로그인 됨");
        }
            
      },
});

const upload = multer({ storage: storage });

module.exports = upload;