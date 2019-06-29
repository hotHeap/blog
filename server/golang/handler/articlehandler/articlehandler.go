package articlehandler

import (
	"net/http"

	"github.com/labstack/echo"

	"github.com/hotHeap/blog/server/golang/handler"
	"github.com/hotHeap/blog/server/golang/logic/articlelogic"
)

type ArticleHandler struct {
	*articlelogic.ArticleLogic
}

func NewArticleHandler(logic *articlelogic.ArticleLogic) *ArticleHandler {
	return &ArticleHandler{ArticleLogic: logic}
}

func (ah *ArticleHandler) ArticleList(context echo.Context) error {
	req := new(articlelogic.ArticleListRequest)
	if err := context.Bind(req); err != nil {
		return context.JSON(http.StatusBadRequest, err)
	}
	data, err := ah.ArticleLogic.ArticleList(req)
	return handler.FormatResponse(context, data, err)
}

func (ah *ArticleHandler) GetArticle(context echo.Context) error {
	req := new(articlelogic.GetArticleByIdRequest)
	if err := context.Bind(req); err != nil {
		return context.JSON(http.StatusBadRequest, err)
	}
	data, err := ah.ArticleLogic.GetArticle(req)
	return handler.FormatResponse(context, data, err)
}

func (ah *ArticleHandler) AddArticle(context echo.Context) error {
	req := new(articlelogic.NewArticleRequest)
	if err := context.Bind(req); err != nil {
		return context.JSON(http.StatusBadRequest, err)
	}
	err := ah.ArticleLogic.AddArticle(req)
	return handler.FormatResponse(context, nil, err)
}

func (ah *ArticleHandler) DeleteArticle(context echo.Context) error {
	req := new(articlelogic.DeleteArticleRequest)
	if err := context.Bind(req); err != nil {
		return context.JSON(http.StatusBadRequest, err)
	}
	err := ah.ArticleLogic.AddArticle(req)
	return handler.FormatResponse(context, nil, err)
}

func (ah *ArticleHandler) UpdateArticle(context echo.Context) error {
	req := new(articlelogic.UpdateArticleRequest)
	if err := context.Bind(req); err != nil {
		return context.JSON(http.StatusBadRequest, err)
	}
	err := ah.ArticleLogic.AddArticle(req)
	return handler.FormatResponse(context, nil, err)
}
