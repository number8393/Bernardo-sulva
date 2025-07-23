import yfinance as yf
import pandas as pd
from datetime import datetime

def analyze_market(symbol):
    try:
        df = yf.download(tickers=symbol, interval="1m", period="30m")
        if df.empty:
            return f"❌ Нет данных для {symbol}"

        df['Body'] = abs(df['Close'] - df['Open'])
        avg_body = df['Body'].mean()
        last = df.iloc[-1]

        signal = ""
        confidence = 0

        if last['Close'] > last['Open'] and last['Body'] > avg_body:
            signal = "📈 Покупка"
            confidence = 80
        elif last['Close'] < last['Open'] and last['Body'] > avg_body:
            signal = "📉 Продажа"
            confidence = 80
        else:
            signal = "⏸ Нет уверенности"
            confidence = 50

        return f"""
📊 {symbol}
Цена: {last['Close']:.5f}
Сигнал: {signal}
Уверенность: {confidence}%
Время: {datetime.now().strftime('%H:%M:%S')}
        """.strip()
    except Exception as e:
        return f"❌ Ошибка {symbol}: {e}"
