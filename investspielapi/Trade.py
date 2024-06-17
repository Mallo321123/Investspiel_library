import json
import requests
import investspielapi.Read as Read

class Trade:
    def __init__(self, config):
        self.trade_config = config.trade_config
        self.stock_config = config.stock_config
        self.generall_config = config.generall_config

        self.portfolioid = config.portfolioid
        self.cookie = config.cookie_full
        
    def _buy_or_sell(self, name, parameters):
        url = self.generall_config["post"]["url"]
        headers = {
            "Cookie": str(self.cookie)
        }
        exchange = self.trade_config[name]["type"]

        parameters.update({
            'PortfolioId': int(self.portfolioid),
            'Exchange': exchange,
            'Ticker': self.trade_config[name]["ticker"],
            'DoEnqueue': False
        })
            
        value = {
            'rq': json.dumps(parameters)
        }
        response = requests.post(url, headers=headers, data=value)
        response.raise_for_status()
        return response
  
  
    def sell_count(self, amount, name):
        if amount > self.owned(name):
            raise RuntimeError("not enouth in stock")
        return self._buy_or_sell(name, {
            'SellQuantity': amount,
        })

    def sell_price(self, money, name):
        amount = self.calc_count(name, money)
        if amount > self.owned(name):
            raise RuntimeError("not enouth in stock")
        return self._buy_or_sell(name, {
            'SellQuantity': amount,
        })

    def sell_all(self, name):
        amount = self.owned(name)
        return self._buy_or_sell(name, {
            'SellQuantity': amount,
        })


    def buy_price(self, money, name):
        if money > self.ballance():
            return("not enouth money")
        return self._buy_or_sell(name, {
            'BuyWithAmount': money,
        })
                      
    def buy_count(self, count, name):
        money = self.calc_price(name, count)
        if money > self.ballance():
            return("not enouth money")
        return self.buy_price(money, name)
            
    def buy_all(self, name):
        money = Read.ballance()
        return self._buy_or_sell(name, {
            'BuyWithAmount': money,
        })
        
        
    def calc_price(self, name, count):
        price = self.price(name)
        value = price * count
        return(value)

    def calc_count(self, name, money):
        price = self.price(name)
        value = money / price
        return(value)
    
    
    def price(self, name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        
        return(response.json("StockRateInGameCurrency"))
    
    def ballance(self):
        name = self.generall_config["get"]["example"]
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]
        
        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        
        return(response.json["Bankroll"])
    
    def owned(self, name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        
        return(response.json("CurrentStockQuantity"))