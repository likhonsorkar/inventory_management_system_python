# 📦 Inventory Management System – ERD Documentation

This document outlines the structure of the **Entity Relationship Diagram (ERD)** used in the Retail Inventory Management System. It covers all key entities, their attributes, and relationships.

---

## 📁 Entities & Attributes

### 1. 🏬 Store
Represents a retail store.
- `store_id` (PK): Unique identifier for the store.
- `store_name`: Name of the store.
- `owner_name`: Name of the store owner.
- `owner_mobile`: Mobile number of the owner.
- `store_website`: Website URL of the store.
- `cash_now`: Current cash available in the store.

---

### 2. 🗂️ ProductCategory
Categorizes products as physical or digital.
- `cat_id` (PK): Unique category ID.
- `cat_name`: Name of the category.
- `cat_type`: Type of category (`Physical` / `Digital`).

---

### 3. 📦 Product
Details of products available in the store.
- `product_id` (PK): Unique product ID.
- `product_name`: Name of the product.
- `cat_id` (FK): Foreign key referencing `ProductCategory`.
- `product_price`: Price of the product.
- `product_weight` (optional): Weight of the product.
- `weight_type`: Unit for weight (`KG`, `G`, `Liter`, `Carton`).
- `quantity`: Available quantity.
- `supplier_id` (FK): Foreign key referencing `Supplier`.

---

### 4. 🚚 Supplier
Suppliers who provide the products.
- `supplier_id` (PK): Unique supplier ID.
- `supplier_name`: Name of the supplier.
- `contact`: Contact information.
- `address`: Supplier's address.

---

### 5. 📈 StockTransaction
Tracks stock changes (inbound and outbound).
- `stock_id` (PK): Unique stock transaction ID.
- `product_id` (FK): Foreign key referencing `Product`.
- `transaction_type`: `IN` (added) or `OUT` (removed).
- `quantity`: Quantity of stock transacted.
- `date`: Date of the transaction.

---

### 6. 👤 Customer
Represents a customer of the store.
- `customer_id` (PK): Unique customer ID.
- `customer_name`: Name of the customer.
- `customer_address`: Address of the customer.
- `customer_mobile`: Mobile number of the customer.
- `reference`: Referrer or account type.
- `balance`: Current account balance or credit.
- `date`: Date of entry or registration.

---

### 7. 🧾 Order
Represents a customer's order.
- `order_id` (PK): Unique order ID.
- `customer_id` (FK): Foreign key referencing `Customer`.
- `date`: Date of the order.
- `total_amount`: Total value of the order.
- `payment_status`: Payment status of the order.
- `order_status`: Delivery or fulfillment status.

---

### 8. 📃 OrderDetail
Line items of a specific order.
- `order_detail_id` (PK): Unique ID for each line item.
- `order_id` (FK): Foreign key referencing `Order`.
- `product_id` (FK): Foreign key referencing `Product`.
- `quantity`: Quantity of the product ordered.
- `price`: Unit price at the time of order.

---

### 9. 💳 Due
Tracks dues for unpaid or partially paid orders.
- `due_id` (PK): Unique due ID.
- `order_id` (FK): Foreign key referencing `Order`.
- `customer_id` (FK): Foreign key referencing `Customer`.
- `due_amount`: Outstanding amount.
- `due_date`: Due date for payment.

---

### 10. 💰 Payments
Tracks payments made by customers.
- `payment_id` (PK): Unique payment ID.
- `customer_id` (FK): Foreign key referencing `Customer`.
- `order_id` (FK): Foreign key referencing `Order`.
- `amount`: Amount paid.
- `date`: Date of payment.
- `method`: Payment method (e.g., Cash, Card, Online).

---

### 11. 💵 Cash
Tracks daily cash records.
- `cash_id` (PK): Unique ID for each cash record.
- `date`: Date of the record.
- `opening`: Opening balance of the day.
- `balance`: Closing balance.

---

### 12. ➕ CashIn
Tracks incoming cash entries.
- `cashin_id` (PK): Unique ID for each cash-in record.
- `cash_id` (FK): Foreign key referencing `Cash`.
- `type`: Source of cash (`GetDue`, `Invest`, etc.).
- `reference`: Related reference info.
- `amount`: Amount received.
- `time`: Time of the transaction.

---

### 13. ➖ CashOut
Tracks outgoing cash entries.
- `cashout_id` (PK): Unique ID for each cash-out record.
- `cash_id` (FK): Foreign key referencing `Cash`.
- `type`: Reason for expense (`Cost`, `Howlad`, etc.).
- `reference`: Related reference info.
- `amount`: Amount spent.
- `time`: Time of the transaction.

---

## 📌 Notes

- All primary keys (PK) are unique identifiers for their respective tables.
- Foreign keys (FK) establish relationships between entities and enforce referential integrity.
- Use proper indexing for performance, especially on FK fields.
- The structure is modular and can be extended for multi-store setups, user roles, or inventory alerts.
