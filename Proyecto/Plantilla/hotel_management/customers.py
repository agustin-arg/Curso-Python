class Customer:
    def __init__(self,id , customer):
        pass

class CustomerManagement:
    ids: int = 0000
    
    def __init__(self):
        self.customers = {}

    def add_customer(cls, self, customer: str):
        if isinstance(customer, str):
            self.customers.update({str(cls.ids),customer})
        else:
            raise TypeError('El argumento debe de ser tipo str')

    def get_customer(self, customer_id: int):
       """Obtiene la información de un cliente por ID."""
       return self.customers[customer_id]