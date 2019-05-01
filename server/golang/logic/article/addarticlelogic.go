package article

type (
	NewArticleRequest struct {
		Title   string `json:"title"`
		Content string `json:"content"`
		Tag     int64  `json:"tag"`
	}
)

func (cl *ArticleLogic)NewArticle()  {
	
}
