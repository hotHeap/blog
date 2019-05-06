package userlogic

import "github.com/hotHeap/blog/server/golang/model"

type (
	UserLogic struct {
		*model.UserModel
	}
)

func NewUserLogic(userModel *model.UserModel) *UserLogic {
	return &UserLogic{UserModel: userModel}
}
