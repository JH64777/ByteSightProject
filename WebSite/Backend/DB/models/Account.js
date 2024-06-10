const Sequelize = require("sequelize");

module.exports = class Account extends Sequelize.Model{
    static init(sequelize){
        return super.init({
            nickname : {
                type : Sequelize.STRING(20),
                allowNull : false,
                unique : true,
                primaryKey : true
            },
            id : {
                type : Sequelize.STRING(20),
                allowNull : false,
                unique : true
            },
            pwd : {
                type : Sequelize.STRING(60),
                allowNull : false
            },
            email : {
                type : Sequelize.STRING(30),
                allowNull : false
            }
        }, {
            sequelize,
            timestamps : false,
            underscored : false,
            modelName : "Account",
            tableName : "accounts",
            paranoid : false,
            collate : "utf8_general_ci",
            charset : "utf8"
        });
    }
}