import random

class Customer:
    def __init__(self , customer_type):
        self.customer_type = customer_type
        self.willingness_to_pay = self.set_willingness()
    
    def set_willingness(self):
          """
        Defines how much a customer is willing to pay
        based on their segment.
        """
          if self.customer_type == "price_sensitive":
               return random.uniform(300,450)
          elif self.customer_type == "normal":
               return random.uniform(400,600)
          elif self.customer_type == "premimum":
               return random.uniform(550,800)
          else:
               return random.uniform(400,600)
    
    def will_buy(self , price):
        #determine whether the customerwill buy at given price
        return price <=self.willingness_to_pay
    

if __name__ == "__main__":
     customer = Customer("price_sensitive")
     print("Willingness to pay:", customer.willingness_to_pay)
     print("Will buy at $400:", customer.will_buy(500))



