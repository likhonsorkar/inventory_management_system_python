from datetime import datetime
class Store:
    def __init__(self, store_id, store_name, owner_name, owner_mobile, store_website, cash_now):
        self.store_id = store_id
        self.store_name = store_name
        self.owner_name = owner_name
        self.owner_mobile = owner_mobile
        self.store_website = store_website
        self.cash_now = cash_now

class ProductCategory:
    def __init__(self, cat_id, cat_name, cat_type):
        self.cat_id = cat_id
        self.cat_name = cat_name
        self.cat_type = cat_type
class Product:
    def __init__(self, product_id, product_name, cat_id, product_price, product_weight, weight_type, quantity, supplier_id):
        self.product_id = product_id
        self.product_name = product_name
        self.cat_id = cat_id
        self.product_price = product_price
        self.product_weight = product_weight
        self.weight_type = weight_type
        self.quantity = quantity
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, supplier_id, supplier_name, contact, address):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact = contact
        self.address = address

class StockTransaction:
    def __init__(self, stock_id, product_id, transaction_type, quantity, date):
        self.stock_id = stock_id
        self.product_id = product_id
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.date = date

class Customer:
    def __init__(self, customer_id, customer_name, customer_address, customer_mobile, reference, balance, date):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_mobile = customer_mobile
        self.reference = reference
        self.balance = balance
        self.date = date

class Order:
    def __init__(self, order_id, customer_id, date, total_amount, payment_status, order_status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.date = date
        self.total_amount = total_amount
        self.payment_status = payment_status
        self.order_status = order_status

class OrderDetail:
    def __init__(self, order_detail_id, order_id, product_id, quantity, price):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

class Due:
    def __init__(self, due_id, order_id, customer_id, due_amount, due_date):
        self.due_id = due_id
        self.order_id = order_id
        self.customer_id = customer_id
        self.due_amount = due_amount
        self.due_date = due_date

class Payments:
    def __init__(self, payment_id, customer_id, order_id, amount, date, method):
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.order_id = order_id
        self.amount = amount
        self. date = date
        self.method = method
        
class Cash:
    def __init__(self, cash_id, opening, balance, date):
        self.cash_id = cash_id
        self.opening = opening
        self.balance = balance
        self.date = date

class CashIn:
    def __init__(self, cashin_id, cash_id, type, reference, amount, time):
        self.cashin_id = cashin_id
        self.cash_id = cash_id
        self.type = type
        self.reference = reference
        self.amount = amount
        self.time = time

class CashOut:
    def __init__(self, cashout_id, cash_id, type, reference, amount, time):
        self.cashout_id = cashout_id
        self.cash_id = cash_id
        self.type = type
        self.reference = reference
        self.amount = amount
        self.time = time

