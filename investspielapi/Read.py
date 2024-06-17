import requests

class Read:
    def __init__(self, config):
        self.trade_config = config.trade_config
        self.stock_config = config.stock_config
        self.generall_config = config.generall_config
        
        self.portfolioid = config.portfolioid
        self.cookie = config.cookie
        self.cookie_full = config.cookie_full
    
    def chart(self, name, time_range):
        url = self.stock_config[name][time_range]
        response = requests.get(url)
        response.raise_for_status()
        return(response.json())
    
    def price(self, name):
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]

        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
            
        Json = response.json()
        
        return(Json["StockRateInGameCurrency"])
    
    def ballance(self):
        name = self.generall_config["get"]["example"]
        url = self.generall_config["get"]["url1"] + self.portfolioid + self.generall_config["get"]["url2"] + self.trade_config[name]["type"] + self.generall_config["get"]["url3"] + self.trade_config[name]["ticker"]
        
        response = requests.get(url, cookies=self.cookie)       # Requests Payload
        
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
            
        Json = response.json()
        
        return(Json["Bankroll"])
    
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
            
        Json = response.json()
        
        return(Json["CurrentStockQuantity"])