const path = require('path')
const webpack = require('webpack')
const vueConfig = require('./vue-loader.config')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const isProd = process.env.NODE_ENV === 'production'

module.exports = {
  devtool: isProd ?
    false :
    '#cheap-module-source-map',
  output: {
    path: path.resolve(__dirname, '../dist/front'),
    publicPath: '/dist/front/',
    filename: 'js/[name].[chunkhash].js',
    chunkFilename: 'js/[name].[chunkhash].js'
  },
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      // 'echarts': 'echarts/dist/echarts.common.min.js',
      // 'vue': 'vue/dist/vue.runtime.min.js',
      // 'vue': 'vue/dist/vue.js',
      '@': path.resolve('src'),
      'R': path.resolve('src/components')
    }
  },
  module: {
    noParse: /es6-promise\.js$/, // avoid webpack shimming process
    rules: [{
        test: /\.vue$/,
        loader: 'vue-loader',
        options: vueConfig
      },
      {
        test :/\.md$/,
        loader: 'text-loader'
      },
      {
        test: /\.scss$/,
        use: [
            "style-loader", // creates style nodes from JS strings
            "css-loader", // translates CSS into CommonJS
            "sass-loader" // compiles Sass to CSS
        ]
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(gif|jpg|png|woff|svg|eot|ttf)\??.*$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(less|css|scss)$/,
        use: isProd ?
          ExtractTextPlugin.extract({
            use: ['css-loader?minimize','less-loader','scss-loader'],
            fallback: 'vue-style-loader'
          }) :
          ['vue-style-loader', 'css-loader', 'less-loader','sass-loader']
      }
    ]
  },
  performance: {
    maxEntrypointSize: 300000,
    hints: isProd ? 'warning' : false
  },
  plugins: isProd ?
    [
      new webpack.optimize.UglifyJsPlugin({
        compress: {
          warnings: false,
          drop_debugger: true,
          drop_console: true
        },
        sourceMap: false // true
      }),
      new ExtractTextPlugin({
        filename: 'css/common.[chunkhash].css',
        // allChunks:true //所有组件的css都打包到一个css文件中
      }),
      new ExtractTextPlugin({
        filename: 'css/common.[chunkhash].less'
      }),
      new CopyWebpackPlugin([
      {
        from: path.resolve(__dirname, '../static/404.html'),
        to: path.resolve(__dirname, '../dist'),
        ignore: ['.*']
      }
    ])
    ] :
    [
      new FriendlyErrorsPlugin()
    ]
}
