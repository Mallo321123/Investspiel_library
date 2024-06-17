import requests
import configparser

class Read:
    def __init__(self, config):
        self.trade_config = configparser.ConfigParser()
        self.trade_config.read('config/trade.conf')
        self.stock_config = configparser.ConfigParser()
        self.stock_config.read('config/stock.conf')
        self.generall_config = configparser.ConfigParser()
        self.generall_config.read('config/generall.conf')
        
        self.portfolioid = config.portfolioid
        self.cookie = config.cookie
    
    def chart(self, name, time_range):
        url = self.stock_config[name][time_range]
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
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
    
    def tax(self,name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        
        tax = response.Json("BrokeragePct") / 100
        
        return(tax)
    
    def owned(self, name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        
        return(response.json("CurrentStockQuantity"))