from fastapi import FastAPI, HTTPException,APIRouter
from pymongo import MongoClient
from bson import ObjectId
app = FastAPI()

class MongoDB:
    def __init__(self, database_name, collection_name):
        self.client = MongoClient('mongodb+srv://Saipriya:Priya2002@cluster0.voqtxao.mongodb.net/')
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
        self.router = APIRouter()

        @self.router.post("/")
        def create(data:dict):
            return {"id":self.create_document(data)}
        @self.router.get("/")
        def read(id:str):
            return self.read_document(id)
        @self.router.put("/")
        def update(id:str,data:dict):
            return {"id":self.update_document(id,data)}
        @self.router.delete("/")
        def delete(id:str):
            return self.delete_document(id)


    def create_document(self, document:dict):
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def read_document(self, id):
        result = self.collection.find_one({"_id":ObjectId(id)})
        return str(result)

    def update_document(self,id:str,data:dict):
        result = self.collection.update_one({"_id":ObjectId(id)}, {'$set': data})
        return True

    def delete_document(self, id:str):
        result = self.collection.delete_one({"_id":ObjectId(id)})
        return "Item deleted successfully."

mongo_db = MongoDB(database_name='blogs', collection_name='test')
app.include_router(mongo_db.router)
