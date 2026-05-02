import yfinance as yf
import matplotlib.pyplot as plt

ticker = "7203.T"  # 丰田汽车

stock = yf.download(ticker, period="6mo")

print(stock.tail())

stock["Close"].plot(figsize=(12, 6))
plt.title("Toyota Stock Price (6 Months)")
plt.xlabel("Date")
plt.ylabel("Price (JPY)")
plt.grid(True)
plt.show()
