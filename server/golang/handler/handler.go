package handler

import "sunseekers/common/baseerror"

type Handler struct {
	Data string `json:"data"`
	Err  *baseerror.CodeError
}

func NewHandler() {

}
