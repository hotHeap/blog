package model

import "github.com/jmoiron/sqlx"

type (
	TagModel struct {
		*SqlModel
	}
)

func NewTagModel(conn sqlx.DB, table string) *TagModel {
	return &TagModel{SqlModel: NewSqlModel(conn, table)}
}
