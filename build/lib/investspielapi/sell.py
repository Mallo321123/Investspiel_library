import read
import configparser
import json
import requests
import calc

class sell:
    def __init__(self, config):
        self.trade_config = configparser.ConfigParser()
        self.trade_config.read('trade.conf')
        self.stock_config = configparser.ConfigParser()
        self.stock_config.read('stock.conf')
        self.generall_config = configparser.ConfigParser()
        self.generall_config.read('generall.conf')
        
        self.portfolioid = config.portfolioid
        self.cookie = config.cookie_full
        
    
    def count(self, amount, name):
        if amount > read.quant(name):
            return("not enouth in stock")
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
            
    def price(self, money, name):
        amount = calc.calc_count(name, money)
        if amount > read.quant(name):
            return("not enouth in stock")
        
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
            
    def sellall(self, name):
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