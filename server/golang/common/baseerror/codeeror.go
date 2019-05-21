package baseerror

import "fmt"

type CodeError struct {
	code    int    `json:"code"`
	message string `json:"message"`
}

var (
	InvalidParams = NewCodeError(10001, "参数有误")
)

// impl Error interface{}
func (ce *CodeError) Error() string {
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

func FromError(err error) (codeErr *CodeError, ok bool) {
	if se, ok := err.(*CodeError); ok {
		return se, true
	}
	return nil, false
}
