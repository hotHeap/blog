package model

import "github.com/jmoiron/sqlx"

type (
	CommentModel struct {
		ModelConnection
	}
)

func NewCommentModel(table string,conn sqlx.DB) *CommentModel {
	return &CommentModel{
		table:table,

	}
}
