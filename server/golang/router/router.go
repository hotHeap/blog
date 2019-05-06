package router

import (
	"github.com/jmoiron/sqlx"
	"github.com/labstack/echo"
)

func LoadRouter(e *echo.Echo, db *sqlx.DB) {
	g := e.Group("/v1")

	// load all routes
	fns := make([]loadFn, 0)
	fns = append(fns, loadFn(article))

	// Initialize the router
	exec(g, db, fns)
}
