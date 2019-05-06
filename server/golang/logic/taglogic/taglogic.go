package taglogic

import "github.com/hotHeap/blog/server/golang/model"

type (
	TagLogic struct {
		*model.TagModel
	}

	Tag struct {
		Id   int    `json:"id"`
		Name string `json:"name"`
	}
)
