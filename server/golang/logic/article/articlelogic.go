package article

import "sunseekers/model"

type (
	ArticleLogic struct {
		ArticleModel *model.ArticleModel
	}

	Article struct {
		Uid     int64  `json:"uid"`
		Title   string `json:"title"`
		Content string `json:"content"`
		Comment string `json:"comment"`
		Like    int    `json:"like"`
	}


)
