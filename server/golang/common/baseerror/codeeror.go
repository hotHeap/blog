package baseerror

import "fmt"

type CodeError struct {
	code    int    `json:"code"`
	message string `json:"message"`
}

func (ce *CodeError) Description() string {
	return fmt.Sprintf("Code is:%+v ,and Message:%+v", ce.code, ce.message)
}

func (ce *CodeError) Code() int {
	return ce.code
}

func (ce *CodeError) Message() string {
	return ce.message
}
func NewCodeError(code int, message string) *CodeError {
	return &CodeError{
		code:    code,
		message: message,
	}
}
