from datetime import datetime

class Product:
    def __init__(self, product_id, name, category, supplier_id, quantity_in_stock, expiration_date):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.__supplier_id = supplier_id
        self.quantity_in_stock = quantity_in_stock
        self.expiration_date = expiration_date

    # Метод для отримання інформації про продукт
    def get_info(self):
        return f"Product: {self.name}, Category: {self.category}, In stock: {self.quantity_in_stock}"

    # Метод для зміни кількості на складі
    def update_stock(self, new_quantity):
        self.quantity_in_stock = new_quantity

    # Статичний метод для перевірки терміну придатності
    @staticmethod
    def is_expired(expiration_date):
        expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()  # Конвертуємо строку у дату
        return expiration_date < datetime.now().date()


# Дочірній клас з множинним наслідуванням
class Antibiotic(Product):
    def __init__(self, product_id, name, category, supplier_id, quantity_in_stock, expiration_date, requires_prescription):
        super().__init__(product_id, name, category, supplier_id, quantity_in_stock, expiration_date)
        self.requires_prescription = requires_prescription  # Чи потрібен рецепт

    # Перевизначення методу для показу інформації про продукт
    def get_info(self):
        info = super().get_info()
        prescription_info = "Requires prescription" if self.requires_prescription else "No prescription needed"
        return f"{info}, {prescription_info}"


# Другий батьківський клас для постачальників
class Supplier:
    def __init__(self, supplier_id, name, email, address):
        self.supplier_id = supplier_id
        self.name = name
        self.email = email
        self.address = address

    def get_supplier_info(self):
        return f"Supplier: {self.name}, Address: {self.address}"


# Множинне наслідування для вітамінів, з інформацією про постачальника
class Vitamin(Product, Supplier):
    def __init__(self, product_id, name, category, supplier_id, quantity_in_stock, expiration_date, vitamin_type, supplier_name, supplier_email, supplier_address):
        Product.__init__(self, product_id, name, category, supplier_id, quantity_in_stock, expiration_date)
        Supplier.__init__(self, supplier_id, supplier_name, supplier_email, supplier_address)
        self.vitamin_type = vitamin_type  # Тип вітаміну, наприклад, A, B, C

    # Перевизначення методу для показу інформації про продукт і постачальника
    def get_info(self):
        product_info = super().get_info()
        supplier_info = self.get_supplier_info()
        return f"{product_info}, Vitamin Type: {self.vitamin_type}. {supplier_info}"


# Демонстрація
if __name__ == "__main__":
    # Створення екземпляру класу Product
    product = Product(1, "Ibuprofen", "Pain Reliever", 101, 100, "2025-01-01")
    print(product.get_info())
    product.update_stock(95)
    print(f"Updated stock: {product.quantity_in_stock}")

    # Створення екземпляру дочірнього класу Antibiotic
    antibiotic = Antibiotic(2, "Amoxicillin", "Antibiotic", 102, 50, "2023-12-31", True)
    print(antibiotic.get_info())

    # Створення екземпляру з множинним наслідуванням
    vitamin = Vitamin(3, "Vitamin C", "Vitamin", 103, 200, "2026-05-15", "C", "HealthSuppliers", "contact@health.com", "123 Vitamin Street")
    print(vitamin.get_info())

    # Використання статичного методу
    print(Product.is_expired("2023-10-01"))  # False, якщо продукт не протермінований
