module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    theme: {
      fontFamily: {
       'sc': ['PingFang SC'],
      }
    },
    backgroundColor: theme => ({
      ...theme('colors'),
      'clickbtn': '#4844A3',
    })
  },
  plugins: [],
}