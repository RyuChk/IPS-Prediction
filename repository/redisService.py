from dotenv import load_dotenv
import redis
import os

class RedisService:
    def __init__(self):
        load_dotenv()
        self.host = str(os.getenv("REDIS_HOST"))
        self.port = int(os.getenv("REDIS_PORT"))
        self.username = str(os.getenv("REDIS_USERNAME"))
        self.password = str(os.getenv("REDIS_PASSWORD"))
        self.connect()

    def connect(self):
        print(f"initiate redis connection to -> ${self.host}")
        self.connection = redis.Redis(
            host=self.host, port=self.port,
            username=self.username,
            password=self.password,
            ssl=False,
        )
    
    def setKey(self, order, building):
        return "COORDINATE:"+str(building)+":"+str(order)
    
    def getCoordinate(self, order, building):
        self.key = self.setKey(order, building)
        if self.connection.exists(self.key):
            val = self.connection.get(self.key)
            return eval(val), False
        return None, True
    
    def findCoordinateCache(self, order, building):
        return self.getCoordinate(order, building)

    def saveCoordinateCache(self, data, order):
        self.key = self.setKey(order, data["building"])
        self.connection.set(self.key, str(data))