package article

import (
	"net/http"

	"github.com/labstack/echo"

	"sunseekers/logic/article"
)

type HandlerArticle struct {
	*article.ArticleLogic
}

func NewArticleHandler(logic *article.ArticleLogic) *HandlerArticle {
	return &HandlerArticle{ArticleLogic: logic,}
}

func (ah *HandlerArticle) NewArticle(context echo.Context) error {
	req := new(article.NewArticleRequest)
	if err := context.Bind(req);err != nil{
		return context.JSON(http.StatusBadRequest,nil)
	}
	ah.ArticleLogic.NewArticle()
}
