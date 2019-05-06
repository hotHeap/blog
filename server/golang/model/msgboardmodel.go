package model

import "github.com/jmoiron/sqlx"

type (
	MsgBoardModel struct {
		*SqlModel
	}
)

func NewMsgBoardModel(conn sqlx.DB, table string) *MsgBoardModel {
	return &MsgBoardModel{SqlModel: NewSqlModel(conn, table)}
}
