const express = require("express");
const app = express();
const scenario = require("./RoutingPages/Scenario");
const steganlysis = require("./RoutingPages/steganalysis");
const path = require('path');
const port = 8080;

app.use(express.static(path.join(__dirname, '../Frontend')));
app.use("/scenario", scenario);
app.use("/analysis", steganlysis);

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../Frontend/Views/Home.html'));
});

app.get("*", (req, res) => {
    res.status(404).sendFile(path.join(__dirname, '../Frontend/Views/404Error.html'));
});

app.listen(port, () => {
    console.log(`server is listening at localhost:${port}`);
});