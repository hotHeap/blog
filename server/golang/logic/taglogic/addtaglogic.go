package taglogic

type (
	AddTagRequest struct {
		Name string `json:"name"`
	}
)

func (tl *TagLogic) AddTag(req *AddTagRequest) error {
	return nil
}
