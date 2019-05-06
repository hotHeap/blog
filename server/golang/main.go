package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/jmoiron/sqlx"
	"github.com/labstack/echo/middleware"
	"github.com/spf13/pflag"
	"github.com/spf13/viper"

	_ "github.com/go-sql-driver/mysql"
	"github.com/labstack/echo"

	"github.com/hotHeap/blog/server/golang/config"
	"github.com/hotHeap/blog/server/golang/router"
)

var (
	version       = pflag.BoolP("version", "v", false, "blog api server's version")
	configuration = pflag.StringP("config", "c", "", "blog api server configuration path")
)

func main() {
	pflag.Parse()

	// init configuration
	if err := config.Init(*configuration); err != nil {
		log.Fatal("config error:", err)
	}

	db, err := initDB()
	if err != nil {
		log.Fatal("database error:", err)
	}
	defer db.Close()

	// Echo instance
	e := echo.New()
	e.GET("/ping", pong)

	// middleware
	useMiddleware(e)

	// Routes
	router.LoadRouter(e, db)

	// Start server
	e.Logger.Fatal(e.Start(":8080"))
}

// Handler
func pong(c echo.Context) error {
	return c.String(http.StatusOK, "pong!")
}

func initDB() (*sqlx.DB, error) {
	config := fmt.Sprintf("%s:%s@tcp(%s)/%s?",
		viper.GetString("db.username"),
		viper.GetString("db.password"),
		viper.GetString("db.address"),
		viper.GetString("db.name"),
	)
	return sqlx.Connect(viper.GetString("db.drivename"), config+"parseTime=true&loc=Asia%2FShanghai")
}

func useMiddleware(e *echo.Echo) {
	e.Use(middleware.CORS())
	e.Use(middleware.Secure())
	e.Use(middleware.Gzip())
}
