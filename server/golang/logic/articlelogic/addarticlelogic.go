package articlelogic

import (
	"github.com/hotHeap/blog/server/golang/common/baseerror"
	"github.com/hotHeap/blog/server/golang/model"
)

type (
	NewArticleRequest struct {
		Title   string `json:"title"`
		Content string `json:"content"`
		Status  int8   `json:"status"`
		Tag     int64  `json:"tag"`
	}
)

func (al *ArticleLogic) AddArticle(req *NewArticleRequest) error {
	// TODO:参数处理
	article := new(model.Article)
	article.UId = 1
	article.Title = req.Title
	article.Content = req.Content
	article.Status = req.Status
	_, err := al.ArticleModel.Insert(article)
	if err != nil {
		return baseerror.NewCodeError(10001, "新增文章失败")
	}
	return nil
}
