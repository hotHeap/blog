package model

import "github.com/jmoiron/sqlx"

type (
	SqlModel struct {
		conn  sqlx.DB
		table string
	}
)

func NewSqlModel(conn sqlx.DB, table string) *SqlModel {
	return &SqlModel{table: table, conn: conn}
}
