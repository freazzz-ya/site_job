import asyncio
import time


class Robot:
    parameters = 20

    def __init__(self, force=10, speed=15):
        self.force = force
        self.speed = speed

    async def punch(self):
        print("start punch")
        await asyncio.sleep(4)
        self.parameters += self.force * 0.1
        print("end punch")
        return f'parameters increased to {self.parameters}'

    async def jump(self):
        print("start jump")
        await asyncio.sleep(3)
        self.parameters += self.speed * 0.2
        print("end jump")
        return f'parameters increased to {self.parameters}'

    async def up_parameres(self):
        print('start')
        task1 = asyncio.create_task(self.punch())
        task2 = asyncio.create_task(self.jump())
        await task1, task2
        print(f'end {self.parameters}')


start = time.time()                                # Время начала работы
obj = Robot(3, 7)
asyncio.run(obj.up_parameres())
finish = time.time()                               # Время конца работы
print(f"Working time = {round(finish-start ,2)} seconds")
