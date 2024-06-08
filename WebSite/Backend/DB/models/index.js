const Sequelize = require('sequelize');
const config = require('../config/config').development;
const Account = require("./Account");
const db = {};

const sequelize = new Sequelize(config.database, config.username, config.password, config);

Account.init(sequelize);

db.sequelize = sequelize;

module.exports= db;