const path = require('path');

module.exports = {
  mode: 'development',
  entry: './personalwebsite/js/header.jsx',
  output: {
    path: path.join(__dirname, '/personalwebsite/static/js/'),
    filename: 'bundle_header.js',
  },
  module: {
    rules: [
      {
        // Test for js or jsx files
        test: /\.jsx?$/,
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env', '@babel/preset-react'],
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
