from fastapi import FastAPI
import random

app = FastAPI()

side_hustle = [
    "AI-Powered E-commerce Tools – Chatbots, automation tools",
    "Dropshipping Store – No inventory, online sales",
    "Crypto Trading Bots – Automated trading solutions",
    "Next.js SaaS Product – Small web app for businesses",
    "Freelance Web Dev (Next.js & Sanity) – Fiverr, Upwork",
    "Wholesale Cosmetics Store – B2B online selling",
    "AI Chatbot Development – Business automation",
    "Crypto Consultancy – Investment & trading guidance",
]

money_quotes = [
    "The only way to do great work is to love what you do.",
    "The best way to predict the future is to invent it.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "The only way to do great work is to love what you do.",
]

@app.get("/side-hustle")
def get_side_hustle(api_key: str):
    if api_key != "1234567890":
        return {'error': 'Invalid API key'}
    return {'side_hustle': random.choice(side_hustle)}

@app.get('/money-quotes')
def get_money_quotes(api_key: str):
    if api_key != "1234567890":
        return {'error': 'Invalid API key'}
    return {'money_quotes': random.choice(money_quotes)}
  