package router

import (
	"net/http"

	"github.com/jmoiron/sqlx"
	"github.com/labstack/echo"
	"github.com/spf13/viper"

	"github.com/hotHeap/blog/server/golang/handler/articlehandler"
	"github.com/hotHeap/blog/server/golang/logic/articlelogic"
	"github.com/hotHeap/blog/server/golang/model"
)

const (
	prefix = "/article"
)

// initialization for article router
func article(g *echo.Group, db *sqlx.DB) {
	articleModel := model.NewArticleModel(*db, viper.GetString("schema.article"))
	tagModel := model.NewTagModel(*db, viper.GetString("schema.tag"))

	articleLogic := articlelogic.NewArticleLogic(articleModel, tagModel)
	routes := articleRouter(articleLogic)
	AddRoutes(g, routes)
}

func articleRouter(al *articlelogic.ArticleLogic) []Route {
	return addPrefix(prefix, []Route{
		{
			Method:  http.MethodGet,
			Path:    "/:id",
			Handler: articlehandler.NewArticleHandler(al).GetArticle,
		}, {
			Method:  http.MethodPost,
			Path:    "/list",
			Handler: articlehandler.NewArticleHandler(al).ArticleList,
		}, {
			Method:  http.MethodPost,
			Path:    "/add",
			Handler: articlehandler.NewArticleHandler(al).AddArticle,
		}, {
			Method:  http.MethodPost,
			Path:    "/delete",
			Handler: articlehandler.NewArticleHandler(al).DeleteArticle,
		}, {
			Method:  http.MethodPost,
			Path:    "/update",
			Handler: articlehandler.NewArticleHandler(al).UpdateArticle,
		},
	})
}
