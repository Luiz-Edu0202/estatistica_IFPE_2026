import plotly.express as px
from download import download_data

df = download_data('AAPL')

px.line(
    df,
    x = 'Date',
    y = 'Close',
    title='AAPL Stock Price'
    )