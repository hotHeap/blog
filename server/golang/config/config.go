package config

import (
	"strings"

	"github.com/fsnotify/fsnotify"
	"github.com/labstack/gommon/log"
	"github.com/spf13/viper"
)

type Config struct {
	Name string
}

func Init(cfg string) error {
	config := Config{
		Name: cfg,
	}

	// 用于热加载
	//config.watchConfigChange()

	return config.initConfig()
}

func (cfg *Config) initConfig() error {
	if cfg.Name != "" {
		viper.SetConfigFile(cfg.Name)
	} else {
		viper.AddConfigPath("conf") // 当前工程目录的 `conf` 文件夹
		viper.SetConfigName("config")
	}

	viper.SetConfigType("yaml")     // 设置配置文件格式为YAML
	viper.AutomaticEnv()            // 读取匹配的环境变量
	viper.SetEnvPrefix("APISERVER") // 读取环境变量的前缀为APISERVER
	replacer := strings.NewReplacer(".", "_")
	viper.SetEnvKeyReplacer(replacer)
	if err := viper.ReadInConfig(); err != nil { // viper解析配置文件
		return err
	}

	return nil
}

func (cfg *Config) watchConfigChange() {
	viper.WatchConfig()
	viper.OnConfigChange(func(in fsnotify.Event) {
		log.Infof("Config file changed: %s", in.Name)
	})
}

// TODO
func (cfg *Config) intLog() {

}
