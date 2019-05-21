package model

import (
	"time"

	"github.com/jmoiron/sqlx"
)

type (
	CommentModel struct {
		*SqlModel
	}

	Comment struct {
		Id         int64     `db:"id" json:"id,omitempty"`
		Uid        int64     `db:"uid" json:"uid,omitempty"`
		Aid        int64     `db:"aid" json:"aid,omitempty"`
		Content    string    `db:"content" json:"content,omitempty"`
		CreateTime time.Time `db:"ctime" json:"createTime,omitempty"`
		UpdateTime time.Time `db:"mtime" json:"updateTime,omitempty"`
	}
)

const commentFields = `id,uid,aid,content,clap,terrible,ctime,mtime`

func NewCommentModel(table string, conn sqlx.DB) *CommentModel {
	return &CommentModel{SqlModel: NewSqlModel(conn, table)}
}

func (cm *CommentModel)Insert () {

}

func (cm *CommentModel)Update () {

}

func (cm *CommentModel)Delete () {

}

func (cm *CommentModel) FindById() {

}


func (cm *CommentModel)FindByArticleId () {

}



func (cm *CommentModel)UpdateFeedback() {

}

