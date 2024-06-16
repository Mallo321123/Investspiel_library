import read
import configparser
import json
import requests
import calc

class buy:
    def __init__(self, config):
        self.trade_config = configparser.ConfigParser()
        self.trade_config.read('trade.conf')
        self.stock_config = configparser.ConfigParser()
        self.stock_config.read('stock.conf')
        self.generall_config = configparser.ConfigParser()
        self.generall_config.read('generall.conf')
        
        self.portfolioid = config.portfolioid
        self.cookie = config.cookie_full
        
    def price(self, money, name):
        if money > read.ballance():
            return("not enouth money")
        
        url = self.generall_config["post"]["url"]
        header = {
            "Cookie": str(self.cookie)
        }
        exchange = self.trade_config[name]["type"]
            
        rq = {
            'PortfolioId': int(self.portfolioid),
            'Exchange': exchange,
            'Ticker': self.trade_config[name]["ticker"],
            'BuyWithAmount': money,
            'DoEnqueue': False

        }
        rq = json.dumps(rq)
        
        data = {
            'rq': str(rq)
        }
        try:
            response = requests.post(url, headers=header, data=data)
        except ConnectionError:
            print("error buying currency")
        
        if response.status_code != 200:
            print("error buying currency")
                      
    def count(self, count, name):
        money = calc.price(name, count)
        if money > read.ballance():
            return("not enouth money")
        
        url = self.generall_config["post"]["url"]
        header = {
            "Cookie": str(self.cookie)
        }
        exchange = self.trade_config[name]["type"]            
            
        rq = {
            'PortfolioId': int(self.portfolioid),
            'Exchange': exchange,
            'Ticker': self.trade_config[name]["ticker"],
            'BuyWithAmount': money,
            'DoEnqueue': False

        }
        rq = json.dumps(rq)
        
        value = {
            'rq': str(rq)
        }
        try:
            response = requests.post(url, headers=header, data=value)
        except ConnectionError:
            print("error buying currency")
        
        if response.status_code != 200:
            print("error buying currency")
            
    def all(self, name):
        amount = read.quant(name)
        url = self.generall_config["post"]["url"]
        header = {
            "Cookie": str(self.cookie)
        }
        exchange = self.trade_config[name]["type"]
            
        rq = {
            'PortfolioId': int(self.portfolioid),
            'Exchange': exchange,
            'Ticker': self.trade_config[name]["ticker"],
            'SellQuantity': amount,
            'DoEnqueue': False

        }
        rq = json.dumps(rq)
        
        value = {
            'rq': str(rq)
        }
        try:
            response = requests.post(url, headers=header, data=value)
        except ConnectionError:
            print("error sell currency")
        
        if response.status_code != 200:
            print("error selling currency")