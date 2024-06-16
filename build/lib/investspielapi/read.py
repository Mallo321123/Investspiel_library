import requests
import configparser

class read:
    def __init__(self, config):
        self.trade_config = configparser.ConfigParser()
        self.trade_config.read('trade.conf')
        self.stock_config = configparser.ConfigParser()
        self.stock_config.read('stock.conf')
        self.generall_config = configparser.ConfigParser()
        self.generall_config.read('generall.conf')
        
        self.portfolioid = config.portfolioid
        self.cookie = config.cookie
    
    def chart(self, name, time_range):
        self.stock_config.read('stock.conf')
        url = self.stock_config[name][time_range]
        response = requests.get(url)
        if response.status_code == 200:
            Json = response.json()
        else:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        return(Json)
    
    def price(self, name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code == 200:
            Json = response.json()
        else:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
            
        price = Json["StockRateInGameCurrency"]
        
        return(price)
    
    def ballance(self):
        name = self.generall_config["get"]["example"]
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]
        
        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code == 200:
            Json = response.json()
        else:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
            
        value = Json["Bankroll"]
        
        return(value)
    
    def tax(self,name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code == 200:
            Json = response.json()
        else:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
            
        tax = Json["BrokeragePct"]
        
        tax = tax / 100
        
        return(tax)
    
    def owned(self, name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code == 200:
            Json = response.json()
        else:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
            
        quant = Json["CurrentStockQuantity"]
        
        return(quant)