import configparser

class Config:
    def __init__(self, cookieconsent, ssid, cookie, portfolioid):
        self.portfolioid = portfolioid
        
        self.cookie = {
            "CookieConsent": cookieconsent,
            "EQSESSID": ssid
        }
        
        self.cookie_full = cookie
        self.stock_config = configparser.ConfigParser()
        self.stock_config.read('config/stock.conf')
        self.generall_config = configparser.ConfigParser()
        self.generall_config.read('config/generall.conf')
        self.trade_config = configparser.ConfigParser()
        self.trade_config.read('config/trade.conf')