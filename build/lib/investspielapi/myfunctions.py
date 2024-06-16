import requests
import datetime
import matplotlib.pyplot as plt
import configparser
import os
from dotenv import load_dotenv
import json
import sqlite3

def stock(name, time_range):
    stock_config.read('stock.conf')
    url = stock_config[name][time_range]
    response = requests.get(url)
    if response.status_code == 200:
        Json = response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
    return(Json)
   
def price(name):
    url = generall_config["get"]["url1"] + generall_config["post"]["portfolioid"] + generall_config["get"]["url2"] + trade_config[name]["type"] + generall_config["get"]["url3"] + trade_config[name]["ticker"]
    cookie = {
        "CookieConsent": os.getenv('cookieconsent'),
        "EQSESSID": os.getenv('ssid')
    }
           
    response = requests.get(url, cookies=cookie)       # Requests Payload
       
    if response.status_code == 200:
        Json = response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
           
    price = Json["StockRateInGameCurrency"]
       
    return(price)
   
def ballance():
    name = generall_config["get"]["example"]
    url = generall_config["get"]["url1"] + generall_config["post"]["portfolioid"] + generall_config["get"]["url2"] + trade_config[name]["type"] + generall_config["get"]["url3"] + trade_config[name]["ticker"]
    cookie = {
        "CookieConsent": os.getenv('cookieconsent'),
        "EQSESSID": os.getenv('ssid')
    }
       
    response = requests.get(url, cookies=cookie)       # Requests Payload
       
    if response.status_code == 200:
        Json = response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
           
    value = Json["Bankroll"]
       
    return(value)
   
def tax(name):
    url = generall_config["get"]["url1"] + generall_config["post"]["portfolioid"] + generall_config["get"]["url2"] + trade_config[name]["type"] + generall_config["get"]["url3"] + trade_config[name]["ticker"]
    cookie = {
        "CookieConsent": os.getenv('cookieconsent'),
        "EQSESSID": os.getenv('ssid')
    }
    
    response = requests.get(url, cookies=cookie)       # Requests Payload
       
    if response.status_code == 200:
        Json = response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")           
        
    tax = Json["BrokeragePct"]
       
    tax = tax / 100
       
    return(tax)
   
def quant(name):
    url = generall_config["get"]["url1"] + generall_config["post"]["portfolioid"] + generall_config["get"]["url2"] + trade_config[name]["type"] + generall_config["get"]["url3"] + trade_config[name]["ticker"]
    cookie = {
        "CookieConsent": os.getenv('cookieconsent'),
        "EQSESSID": os.getenv('ssid')
    }
       
    response = requests.get(url, cookies=cookie)       # Requests Payload
       
    if response.status_code == 200:
        Json = response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
           
    quant = Json["CurrentStockQuantity"]
       
    return(quant)