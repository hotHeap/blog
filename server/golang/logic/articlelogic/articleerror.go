package articlelogic

import "github.com/hotHeap/blog/server/golang/common/baseerror"

var (
	ErrInvalidParams = baseerror.NewCodeError(10001,"参数有误")
)
