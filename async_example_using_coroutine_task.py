"""
Author      : Shubham Ahinave
Created at  : 10/10/24
"""
import asyncio
import multiprocessing
import os
import threading
import time
from datetime import datetime


# Synchronous implementation of ordering food and splitting money
class ExampleFirst():
    # Method to simulate ordering food, blocking for 10 seconds
    def order_food(self):
        print(f"E1, order_food Process Id:{os.getpid()}")
        time.sleep(10)  # Simulate a long-running operation
        print('Food Ordered successfully !')
    
    # Method to simulate splitting money, blocking for 2 seconds
    def split_money(self):
        print(f"E1, split_money Process Id:{os.getpid()}")
        time.sleep(2)  # Simulate a shorter operation
        print('Split money done !')
    
    # Main method to execute the ordering and splitting sequentially
    def main(self):
        self.order_food()  # Order food first
        self.split_money()  # Then split the money

# Asynchronous implementation using asyncio
class ExampleSecond():
    # This method is a coroutine that simulates ordering food
    async def order_food(self):
        print(f"E2, order_food Process Id:{os.getpid()}")
        for i in range(10):
            await asyncio.sleep(1)  # Non-blocking sleep for 10 seconds
            print(f"order_food: {datetime.now()}")
        print('Food Ordered successfully !')

    # This method is a coroutine that simulates splitting money
    async def split_money(self):
        print(f"E2, split_money Process Id:{os.getpid()}")
        for i in range(2):
            await asyncio.sleep(1)  # Non-blocking sleep for 2 seconds
            print(f"split_money: {datetime.now()}")
        print('Split money done !')

    # Main method that manages the execution of coroutines concurrently
    async def main(self):
        # Create tasks for ordering food and splitting money
        t1 = asyncio.create_task(self.order_food())
        t2 = asyncio.create_task(self.split_money())

        # Wait for both tasks to complete
        await t1
        await t2


# Asynchronous implementation using asyncio
class ExampleMultiThread():
    # This method is a coroutine that simulates ordering food
    def order_food(self):
        print(f"ET, order_food Process Id:{os.getpid()}")
        for i in range(10):
            time.sleep(1)  # Non-blocking sleep for 10 seconds
            print(f"order_food: {datetime.now()}")
        print('Food Ordered successfully !')
    
    # This method is a coroutine that simulates splitting money
    def split_money(self):
        print(f"ET, split_money Process Id:{os.getpid()}")
        for i in range(2):
            time.sleep(1)  # Non-blocking sleep for 2 seconds
            print(f"split_money: {datetime.now()}")
        print('Split money done !')
    
    # Main method that manages the execution of coroutines concurrently
    def main(self):
        # Create tasks for ordering food and splitting money
        t1 = threading.Thread(target=self.order_food)
        t2 = threading.Thread(target=self.split_money)
        
        # Wait for both tasks to complete
        t1.start()
        t2.start()
        t1.join()
        t2.join()


# Asynchronous implementation using asyncio
class ExampleMultiProc():
    # This method is a coroutine that simulates ordering food
    def order_food(self):
        print(f"EP, order_food Process Id:{os.getpid()}")
        for i in range(10):
            time.sleep(1)  # Non-blocking sleep for 10 seconds
            print(f"order_food: {datetime.now()}")
        print('Food Ordered successfully !')
    
    # This method is a coroutine that simulates splitting money
    def split_money(self):
        print(f"EP, split_money Process Id:{os.getpid()}")
        for i in range(2):
            time.sleep(1)  # Non-blocking sleep for 2 seconds
            print(f"split_money: {datetime.now()}")
        print('Split money done !')
    
    # Main method that manages the execution of coroutines concurrently
    def main(self):
        # Create tasks for ordering food and splitting money
        t1 = multiprocessing.Process(target=self.order_food)
        t2 = multiprocessing.Process(target=self.split_money)
        
        # Wait for both tasks to complete
        t1.start()
        t2.start()
        t1.join()
        t2.join()


# Entry point for the script
if __name__ == "__main__":
    print(f"Parent: {os.getpid()}")
    
    print("#" * 15, 'Sync Code', '#'*15)
    # Measure time for synchronous execution
    s = time.perf_counter()
    ef = ExampleFirst()
    ef.main()  # Run the synchronous main method
    e = time.perf_counter()
    print(f'Total time sync: {e - s} sec.')
    
    
    print("#" * 15, 'async Code', '#'*15)
    # Measure time for asynchronous execution
    s = time.perf_counter()
    es = ExampleSecond()
    asyncio.run(es.main())
    e = time.perf_counter()
    print(f'Total time async: {e - s} sec.')
    
    
    print("#" * 15, 'Multi Threading Code', '#'*15)
    # Measure time for asynchronous execution
    s = time.perf_counter()
    es = ExampleMultiThread()
    es.main()
    e = time.perf_counter()
    print(f'Total time multi_thread: {e - s} sec.')
    
    
    print("#" * 15, 'Multi Processing Code', '#'*15)
    # Measure time for asynchronous execution
    s = time.perf_counter()
    es = ExampleMultiProc()
    es.main()
    e = time.perf_counter()
    print(f'Total time multi_process: {e - s} sec.')
