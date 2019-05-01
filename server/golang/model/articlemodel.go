package model

import "github.com/jmoiron/sqlx"

type (
	ArticleModel struct {
		table string
		conn  sqlx.DB
	}
)

func NewArticleModel(table string, conn sqlx.DB) *ArticleModel {
	return &ArticleModel{
		table: table,
		conn:  conn,
	}
}
