class Config:
    def __init__(self, cookieconsent, ssid, cookie, portfolioid):
        self.portfolioid = portfolioid
        
        self.cookie = {
            "CookieConsent": cookieconsent,
            "EQSESSID": ssid
        }
        
        self.cookie_full = cookie