import asyncio
import time

# Synchronous implementation of ordering food and splitting money
class ExampleFirst():
    # Method to simulate ordering food, blocking for 10 seconds
    def order_food(self):
        time.sleep(10)  # Simulate a long-running operation
        print('Food Ordered successfully !')

    # Method to simulate splitting money, blocking for 2 seconds
    def split_money(self):
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
        await asyncio.sleep(10)  # Non-blocking sleep for 10 seconds
        print('Food Ordered successfully !')

    # This method is a coroutine that simulates splitting money
    async def split_money(self):
        await asyncio.sleep(2)  # Non-blocking sleep for 2 seconds
        print('Split money done !')

    # Main method that manages the execution of coroutines concurrently
    async def main(self):
        # Create tasks for ordering food and splitting money
        t1 = asyncio.create_task(self.order_food())
        t2 = asyncio.create_task(self.split_money())
        
        # Wait for both tasks to complete
        await t1
        await t2

# Entry point for the script
if __name__ == "__main__":
    # Measure time for synchronous execution
    s = time.perf_counter()
    ef = ExampleFirst()
    ef.main()  # Run the synchronous main method
    e = time.perf_counter()
    print(f'Total time sync: {e-s} sec.')

    # Measure time for asynchronous execution
    s = time.perf_counter()
    es = ExampleSecond()
    asyncio.run(es.main())
    e = time.perf_counter()
    print(f'Total time async: {e-s} sec.')
