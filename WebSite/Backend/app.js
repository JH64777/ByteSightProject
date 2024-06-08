const express = require("express");
const app = express();
const scenario = require("./RoutingPages/Scenario");
const steganlysis = require("./RoutingPages/steganalysis");
const study = require("./RoutingPages/study");
const resources = require("./RoutingPages/resource");
const login = require("./RoutingPages/login");
const account = require("./RoutingPages/account");
const path = require('path');
const { sequelize } = require('./DB/models');
const port = 8080;

sequelize.sync({ force: true })
    .then(() => {
        console.log("데이터 베이스 연결 성공")
    })
    .catch((err) => {
        console.log(err);
    });

app.use(express.static(path.join(__dirname, '../Frontend')));
app.use(express.urlencoded({extended : true}));
app.use(express.json());
app.use("/scenario", scenario);
app.use("/analysis", steganlysis);
app.use("/resources", resources);
app.use("/study", study);
app.use("/login", login);
app.use("/signup", account);

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../Frontend/Views/Home.html'));
});

app.get("*", (req, res) => {
    res.status(404).sendFile(path.join(__dirname, '../Frontend/Views/404Error.html'));
});

app.listen(port, () => {
    console.log(`server is listening at localhost:${port}`);
});