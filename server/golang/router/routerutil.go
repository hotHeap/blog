package router

import (
	"net/http"

	"github.com/jmoiron/sqlx"
	"github.com/labstack/echo"
)

type (
	Route struct {
		Method  string
		Path    string
		Handler echo.HandlerFunc
	}
)

type (
	loadFn func(*echo.Group, *sqlx.DB)
	loadFns []loadFn
)

func exec(g *echo.Group, db *sqlx.DB, fns loadFns) {
	for _, f := range fns {
		f(g, db)
	}
}

func AddRoutes(g *echo.Group, routes []Route) {
	for _, r := range routes {
		matchMethod(g, r)
	}
}

func matchMethod(g *echo.Group, r Route) {
	switch r.Method {
	case http.MethodGet:
		g.GET(r.Path, r.Handler)
	case http.MethodPost:
		g.POST(r.Path, r.Handler)
	case http.MethodPut:
		g.PUT(r.Path, r.Handler)
	case http.MethodDelete:
		g.DELETE(r.Path, r.Handler)
	case http.MethodHead:
		g.HEAD(r.Path, r.Handler)
	case http.MethodPatch:
		g.PATCH(r.Path, r.Handler)
	case http.MethodConnect:
		g.CONNECT(r.Path, r.Handler)
	case http.MethodOptions:
		g.OPTIONS(r.Path, r.Handler)
	case http.MethodTrace:
		g.TRACE(r.Path, r.Handler)
	default:
	}
}

func addPrefix(prefix string, routes []Route) []Route {
	for i, _ := range routes {
		routes[i].Path = prefix + routes[i].Path
	}
	return routes
}
