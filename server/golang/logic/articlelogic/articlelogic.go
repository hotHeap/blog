package articlelogic

import "github.com/hotHeap/blog/server/golang/model"

type (
	ArticleLogic struct {
		*model.ArticleModel
		*model.TagModel
	}

	Article struct {
		model.Article
	}
)

func NewArticleLogic(articleModel *model.ArticleModel, tagModel *model.TagModel) *ArticleLogic {
	return &ArticleLogic{
		ArticleModel: articleModel,
		TagModel:     tagModel,
	}
}
