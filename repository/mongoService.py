from dotenv import load_dotenv
from pymongo import MongoClient
from typing import List, Dict, Any
from pymongo.errors import ServerSelectionTimeoutError
from pymongo.cursor import Cursor
import os

class TrainStatModel:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class MongoDBClient:
    def __init__(self, collectionName:str) -> None:
        load_dotenv()
        self.ConnectionString = str(os.getenv("DB_CONNECTION_STRING"))
        self.Name = str(os.getenv("DB_NAME"))
        self.Collection = collectionName
        self.init()

    def init(self):
        print(f"initiate mongodb connection to -> ${self.Collection}")
        client = MongoClient(self.ConnectionString, serverSelectionTimeoutMS=5000)
        db = client[self.Name]
        self.Client = db[self.Collection]

    def insert_one(self, document: TrainStatModel) -> None:
        self.Client.insert_one(document.__dict__)

    def find(self, filter: Dict[str, Any]) -> List[TrainStatModel]:
        result = []
        cursor: Cursor = self.Client.find(filter)
        for document in cursor:
            result.append(TrainStatModel(**document))
        return result

    def find_one(self, filter: Dict[str, Any]) -> TrainStatModel:
        try:
            document = self.Client.find_one(filter)
            if document:
                return document
            else:
                return None
        except ServerSelectionTimeoutError:
            return None
