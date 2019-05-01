package main

import (
	"net/http"

	"github.com/spf13/pflag"

	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
)

var (
	cfg     = pflag.StringP("config", "c", "", "blog api server configuration path")
	version = pflag.BoolP("version", "v", false, "blog api server's version")
)

func main() {
	pflag.Parse()

	// Echo instance
	e := echo.New()

	// Middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// Routes
	e.GET("/", hello)

	// Start server
	e.Logger.Fatal(e.Start(":1323"))
}

// Handler
func hello(c echo.Context) error {
	return c.String(http.StatusOK, "Hello, World!")
}
