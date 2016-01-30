/**
 * @fileOverview Webpack configuration file
 * @name webpack.config.js<younglee-s-blog>
 * @author Young Lee <youngleemails@gmail.com>
 * @license MIT
 */
'use strict';

var path = require("path");
var webpack = require('webpack');
var node_modules = path.resolve(__dirname, 'node_modules');
var pathToReact = path.resolve(node_modules, 'react/dist/react.min.js');

var definePlugin = new webpack.DefinePlugin({
    __DEV__: JSON.stringify(JSON.parse(process.env.BUILD_DEV || 'true')),
    __PRERELEASE__: JSON.stringify(JSON.parse(process.env.BUILD_PRERELEASE || 'false'))
});

// webpack config
module.exports = {
	entry: { 
		app: [ 'webpack/hot/dev-server', path.resolve(__dirname, 'app/react-slide.js') ] 
	},
	resolve: {
		alias: { 'react': pathToReact }
	},
    output: {
	    path: path.resolve(__dirname, 'build'),
	    filename: 'bundle.js'
    },
    module: {
        loaders: [
            { 
                test: /\.jsx$/,
                loader: 'babel'
            }, { 
                loader: 'babel-loader',
	            query: { presets: [ 'es2015', 'react' ] }
            }, {
	            test: /\.css$/,
                loader: 'style!css'
            }, {
                test: /\.less$/,
	            loader: 'style!css!less'
            }, {
	            test: /\.(png|jpg)$/,
	            loader: 'url?limit=25000'
            }, { 
		        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, 
		        loader: "url-loader?limit=10000&minetype=application/font-woff" 
	        }, { 
		        test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, 
		        loader: "file-loader"
	        }
        ],
	    noParse: [ pathToReact ]
    },
    resolve: {
        // use require without file extensions
	    extensions: [ '', '.js', '.json', '.jsx' ]
    },
    plugins: [
	    definePlugin
    ]
};

