package model

import (
	"time"

	"github.com/jmoiron/sqlx"
)

type (
	ArticleModel struct {
		*SqlModel
	}

	Article struct {
		Id         int64     `json:"id" db:"id"`
		UId        int64     `json:"uid" db:"uid"`
		Title      string    `json:"title" :"Title"`
		Content    string    `json:"content" db:"content"`
		Status     int8      `json:"status" db:"status"`
		Clap       int       `json:"clap" db:"clap"`
		Terrible   int       `json:"terrible" db:"terrible"`
		Visits     int       `json:"visits" db:"visits"`
		Replies    int       `json:"replies" db:"replies"`
		Shared     int       `json:"shared" db:"shared"`
		CreateTime time.Time `json:"ctime" db:"ctime"`
		UpdateTime time.Time `json:"mtime" db:"mtime"`
	}
)

func NewArticleModel(conn sqlx.DB, table string) *ArticleModel {
	return &ArticleModel{SqlModel: NewSqlModel(conn, table)}
}

func (am *ArticleModel) Insert(article *Article) (int64, error) {
	querySql := `insert into ` + am.table + ` (uid,title,content,status) VALUES ($1,$2,$3,$4)`
	result, err := am.SqlModel.conn.Exec(querySql, article.UId, article.Title, article.Content, article.Status)
	if err != nil {
		return 0, err
	}
	id, err := result.LastInsertId()
	if err != nil {
		return 0, nil
	}
	return id, nil
}
