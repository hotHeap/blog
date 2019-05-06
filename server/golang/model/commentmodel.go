package model

import "github.com/jmoiron/sqlx"

type (
	CommentModel struct {
		*SqlModel
	}
)

func NewCommentModel(table string, conn sqlx.DB) *CommentModel {
	return &CommentModel{SqlModel: NewSqlModel(conn, table)}
}
