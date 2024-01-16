from setuptools import setup, find_packages



requires = [
    'matplotlib',
    'mplfinance',
    'pandas',
    'pandas_datareader.data'
    'numpy',
    'requests',
    'pickle',
    'yfinance',
    'bs4',
    'lxml',
    'scikit-learn',
]


setup(
    name='stock_analysis',
    version='1',
    packages=find_packages(),
    keywords='python stock candlestick matplotlib pandas ',
    url='',
    license='',
    author='Tom Hildebrand',
    author_email='t1manster@gmail.com',
    description='Stock analysis tool to analyze correlation between the top 100 stocks of the S&P500. The tool produces a heat map to easily visualize the correlations.',
    install_requires=requires
)
