const Sequelize = require('sequelize');
const config = require('../config/config').development;
const Account = require("./Account");
const Board = require("./Board");
const Post = require("./Post");
const db = {};

const sequelize = new Sequelize(config.database, config.username, config.password, config);

Account.init(sequelize);
Board.init(sequelize);
Post.init(sequelize);

Account.associate({ Post });
Board.associate({ Post });
Post.associate({ Board, Account });

db.sequelize = sequelize;

module.exports= db;