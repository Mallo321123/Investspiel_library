import read

class calc:
    def price(name, count):
        price = read.price(name)
        value = price * count
        return(value)

    def count(name, money):
        price = read.price(name)
        value = money / price
        return(value)