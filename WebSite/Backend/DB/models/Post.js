const Sequelize = require("sequelize");

module.exports = class Post extends Sequelize.Model{
    static init(sequelize){
        return super.init({ // 20(닉네임) + 14(년월일시분초) = 34
            postID : {
                type : Sequelize.STRING(34),
                allowNull : false,
                unique : true,
                primaryKey : true
            },
            title : {
                type : Sequelize.STRING(40),
                allowNull : false,
            },
            contents : {
                type : Sequelize.TEXT,
                allowNull : false,
            },
            createdtime : {
                type : Sequelize.DATE,
                allowNull : false
            }
        }, {
            sequelize,
            timestamps : false,
            underscored : false,
            modelName : "Post",
            tableName : "post",
            paranoid : false,
            collate : "utf8_general_ci",
            charset : "utf8"
        });
    }

    static associate(models) {
        this.belongsTo(models.Account, {
            foreignKey: 'accountNickname',
            targetKey: 'nickname'
        });
        
        this.belongsTo(models.Board, {
            foreignKey: 'boardname',
            targetKey: 'boardname'
        });
    }
}