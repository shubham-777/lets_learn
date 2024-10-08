import asyncio
import time

# ref: https://docs.python.org/3/library/asyncio-task.html

class ExampleFirst():
    def order_food(self):
        time.sleep(10)
        print('Food Ordered successfully !')

    def split_money(self):
        time.sleep(2)
        print('Split money done !')

    def main(self):
        self.order_food()
        self.split_money()
    
class ExampleSecond():
    # due to async keyword this become a coroutine
    async def order_food(self):
        # wait until this coroutine execution is finished
        await asyncio.sleep(10)
        print('Food Ordered successfully !')

    async def split_money(self):
        await asyncio.sleep(2)
        print('Split money done !')

    async def main(self):
        t1 =  asyncio.create_task(self.order_food())
        t2 =  asyncio.create_task(self.split_money())
        await t1
        await t2

if __name__ == "__main__":
    s = time.perf_counter()
    ef = ExampleFirst()
    ef.main()
    e = time.perf_counter()
    print(f'Total time sync: {e-s} sec.')

    s = time.perf_counter()
    es = ExampleSecond()
    asyncio.run(es.main())
    e = time.perf_counter()
    print(f'Total time async: {e-s} sec.')
