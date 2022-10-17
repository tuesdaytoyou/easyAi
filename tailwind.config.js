module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    theme: {
      fontFamily: {
        'sc': ['PingFang SC'],
      }
    },
    extend: {
      colors: {
        statehover: '#475258'
      }
    },
    backgroundColor: theme => ({
      ...theme('colors'),
      'clickbtn': '#4844A3',
    })
  },
  plugins: [],
}