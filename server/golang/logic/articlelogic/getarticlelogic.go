package articlelogic

type (
	GetArticleByIdRequest struct {
		Id int64 `json:"id"`
	}
	GetArticleByIdResponse struct {
		Article
	}

	ArticleListRequest struct {
		NowPage  int `json:"nowPage"`
		PageSize int `json:"pageSize"`
	}
	ArticleListResponse struct {
		Total    int        `json:"total"`
		Count    int        `json:"count"`
		NowPage  int        `json:"nowPage"` //当前页
		Articles []*Article `json:"articles"`
	}
)

func (al *ArticleLogic) ArticleList(req *ArticleListRequest) (*ArticleListResponse, error) {
	var resp ArticleListResponse
	resp.Total = 1
	resp.Count = 1
	resp.NowPage = 1

	var a Article
	a.Status = 1
	a.Title = "测试文章"
	a.Content = "dsafae4wsvasdfaszdvqszx adsv dawcafasvqavcaesfsadfva"
	a.Clap = 1000
	resp.Articles = append(resp.Articles, &a)
	return &resp, nil
}

func (al *ArticleLogic) GetArticle(req *GetArticleByIdRequest) (*GetArticleByIdResponse, error) {
	var resp GetArticleByIdResponse
	resp.Status = 1
	resp.Title = "测试文章"
	resp.Content = "dsafae4wsvasdfaszdvqszx adsv dawcafasvqavcaesfsadfva"
	resp.Clap = 1000
	return &resp, ErrInvalidParams
}
