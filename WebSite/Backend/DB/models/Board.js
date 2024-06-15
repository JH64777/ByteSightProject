const Sequelize = require("sequelize");

module.exports = class Board extends Sequelize.Model{
    static init(sequelize){
        return super.init({
            boardname : {
                type : Sequelize.STRING(40),
                allowNull : false,
                unique : true,
                primaryKey : true
            }
        }, {
            sequelize,
            timestamps : false,
            underscored : false,
            modelName : "Board",
            tableName : "board",
            paranoid : false,
            collate : "utf8_general_ci",
            charset : "utf8"
        });
    }
    
    static associate(models) {
        this.hasMany(models.Post, {
            foreignKey: 'boardname',
            sourceKey: 'boardname'
        });
    }
}