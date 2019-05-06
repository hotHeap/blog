package articlelogic

type (
	UpdateArticleRequest struct {
		Id int64 `json:"id"`
	}
)

func (al *ArticleLogic) UpdateArticle(req *UpdateArticleRequest) error {
	// TODO
	return nil
}
