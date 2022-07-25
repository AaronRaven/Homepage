''''
Originaliai internete buvo geras tutorialas
kaip kurti programas su fbprophet
bet mano pc jo nesugebejo irasyti
tai maza programele
kuri parodo, kiek procentu pakilo
populiarios krypto ir akciju kainos

Siaip ne taip
nuojauta sako, kad streamlit ir fb prophet
turi
puikia ateity!
Yfinance irgi super :D
'''
# ---- THE LIBRARIES----
import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stuff :( ", page_icon=":dollar:", layout="wide")
# ---- NAVIGATION BAR----
selected = option_menu(
    menu_title="Epic Navigation bar",  # required
    options=["Home", "Our Python Calculator", "The Crypto tool"],  # required
    icons=["house", "calculator", "currency-bitcoin"],  # optional
    menu_icon="controller",  # optional
    default_index=1,  # optional
    orientation="horizontal",
)

if selected == "Home":
    st.title("main.app")
if selected == "Our Python Calculator":
    st.title("https://codeacademy.lt/")
if selected == "The Crypto tool":
    st.title("'Tis the tool!")
    # ---- HEADER----

tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-EUR')

# ---- BASSICALLY THE BODY----
# ---- DROPDOWN MENU----
dropdown = st.multiselect("Choose the investment dream!", tickers)

start = st.date_input('From', value=pd.to_datetime('2022-01-01'))
end = st.date_input('Untill', value=pd.to_datetime('today'))
def theprofit(df):
    rel = df.pct_change()
    cumret = (1 + rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret




if len(dropdown) > 0:
    df = theprofit(yf.download(dropdown, start, end)['Adj Close'])
    st.header ('Returns of {}'.format(dropdown))
    st.line_chart(df)
