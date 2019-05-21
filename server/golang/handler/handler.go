package handler

import (
	"errors"
	"net/http"

	"github.com/labstack/echo"

	"github.com/hotHeap/blog/server/golang/common/baseerror"
)

var (
	errServiceUnavailable = errors.New("服务器竟然开小差，一会儿再试试吧")
)

func FormatResponse(context echo.Context, data interface{}, err error) error {
	if err != nil {
		codeErr, ok := baseerror.FromError(err)
		if ok {
			return context.JSON(http.StatusServiceUnavailable, codeErr)
		} else {
			return context.JSON(http.StatusInternalServerError, errServiceUnavailable)
		}
	}
	return context.JSON(http.StatusOK, data)
}
