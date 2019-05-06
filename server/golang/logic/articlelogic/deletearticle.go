package articlelogic

type (
	DeleteArticleRequest struct {
		Id int64 `json:"id"`
	}
)

func (al *ArticleLogic) DeleteArticle() error {
	// TODO
	return nil
}
