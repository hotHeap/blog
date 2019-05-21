package model

import "github.com/jmoiron/sqlx"

type (
	UserModel struct {
		*SqlModel
	}

	User struct {
		Uid int64 `db:"uid" json:"uid,omitempty"`
		Account string `db:"account" json:"account,omitempty"`

	}
)

func NewUserModel(conn sqlx.DB, table string) *UserModel {
	return &UserModel{SqlModel: NewSqlModel(conn, table)}
}

func (um *UserModel) Insert(u *User) (int64, error) {
	//TODO
	querySql := `insert into ` + um.table + ` () VALUES ()`
	result, err := um.SqlModel.conn.Exec(querySql)
	if err != nil {
		return 0, err
	}
	id, err := result.LastInsertId()
	if err != nil {
		return 0, nil
	}
	return id, nil
}
