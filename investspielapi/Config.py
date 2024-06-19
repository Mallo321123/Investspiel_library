import configparser
import pkg_resources

class Config:
    def __init__(self, ssid, cookie, portfolioid):
        self.portfolioid = portfolioid
        self.cookie_full = cookie
        self.cookie = {

            "EQSESSID": str(ssid)
        }

        config_path = pkg_resources.resource_filename('investspielapi', 'config/stock.conf')
        self.stock_config = configparser.ConfigParser()
        self.stock_config.read(config_path)
            
        config_path = pkg_resources.resource_filename('investspielapi', 'config/generall.conf')
        self.generall_config = configparser.ConfigParser()
        self.generall_config.read(config_path)
            
        config_path = pkg_resources.resource_filename('investspielapi', 'config/trade.conf')
        self.trade_config = configparser.ConfigParser()
        self.trade_config.read(config_path)