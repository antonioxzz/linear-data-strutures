"""

"""

import random
import time
from typing import List, Optional

class Customer:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.arrival_time: float = time.time()
        self.shopping_time: int = random.randint(1, 5)

class Queue:
    def __init__(self) -> None:
        self.customers: List[Customer] = []
    
    def add_customer(self, customer: Customer) -> None:
        self.customers.append(customer)
    
    def next_customer(self) -> Optional[Customer]:
        if len(self.customers) == 0:
            return None
        else:
            return self.customers.pop(0)
    
    def length(self) -> int:
        return len(self.customers)

queue: Queue = Queue()
current_time: float = time.time()
last_customer_time: float = 0

while True:
    # Generate random customer
    if current_time - last_customer_time > random.randint(1, 3):
        customer: Customer = Customer(len(queue.customers) + 1)
        queue.add_customer(customer)
        print(f"Customer {customer.id} arrived at {time.strftime('%H:%M:%S', time.localtime(customer.arrival_time))}")
        last_customer_time = current_time
    
    # Serve next customer
    if queue.length() > 0:
        current_customer: Customer = queue.next_customer()
        print(f"Serving customer {current_customer.id}...")
        time.sleep(current_customer.shopping_time)
        print(f"Customer {current_customer.id} has finished shopping.")
    
    current_time = time.time()
    time.sleep(1)
