package model

import "github.com/jmoiron/sqlx"

type (
	SqlModel struct {
		table string
		conn  sqlx.DB
	}
)

func NewConnectionModel(table string, conn sqlx.DB) *SqlModel {
	return &SqlModel{table: table, conn: conn}
}
