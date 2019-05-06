package articlelogic

type (
	NewArticleRequest struct {
		Title   string `json:"title"`
		Content string `json:"content"`
		Tag     int64  `json:"tag"`
	}
)

func (al *ArticleLogic) AddArticle(req *NewArticleRequest) error {
	return nil
}
