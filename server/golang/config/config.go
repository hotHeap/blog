package config

import (
	"github.com/fsnotify/fsnotify"
	"github.com/labstack/gommon/log"
	"github.com/spf13/viper"
)

type Config struct {
	Name string
}

func (cfg *Config) Init() error {
	return nil
}

func (cfg *Config) initConfig() {

}

func (cfg *Config) intLog() {

}

func (cfg *Config) watchConfigChange() {
	viper.WatchConfig()
	viper.OnConfigChange(func(in fsnotify.Event) {
		log.Infof("Config file changed: %s", in.Name)
	})
}
