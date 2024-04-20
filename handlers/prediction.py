import os
import grpc
from dotenv import load_dotenv

import ips.model.v1.model_pb2_grpc as modelv1_grpc
import ips.model.v1.model_pb2 as modelv1

from utils import error_logging
from repository import modelService, redisService, mongoService


class ModelServiceServicer(modelv1_grpc.ModelServiceServicer):
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.redisClient = redisService.RedisService()
        self.CMKLCollection = mongoService.MongoDBClient(str(os.getenv("CMKL_COLLECTION_NAME")))
        self.TWBuildingCollection = mongoService.MongoDBClient(str(os.getenv("TW_BUILDING_COLLECTION_NAME")))

    def PredictCoordinate(self, request, context):
        building = request.building

        building_model, err = modelService.LoadPredictionModel(building)
        if err:
            error_logging.Error(context, grpc.StatusCode.INTERNAL, "error loading model")
            return 1, True
        
        orderID, err = modelService.PredictUserLocation(building_model, request)
        if err:
            error_logging.Error(context, grpc.StatusCode.INTERNAL, "error predict user location")
            return 1, True
        
        result, err = self.redisClient.findCoordinateCache(orderID, building)
        if err:
            filter_criteria = {"order": float(orderID[0])}
            location = {}
            if building == "CMKL":
                result = self.CMKLCollection.find_one(filter_criteria)
                if not result:
                    error_logging.Error(context, grpc.StatusCode.INTERNAL, "error getting location from database or timeout")
                    return 1, True
                
                location = {
                    "x": result.get("x"),
                    "y": result.get("y"),
                    "z": result.get("z"),
                    "label": result.get("label"),
                    "building": building
                }
            else :
                result = self.TWBuildingCollection.find_one(filter_criteria)
                if not result:
                    error_logging.Error(context, grpc.StatusCode.INTERNAL, "error getting location from database or timeout")
                    return 1, True
                
                location = {
                    "x": result.get("x"),
                    "y": result.get("y"),
                    "z": result.get("z"),
                    "label": result.get("label"),
                    "building": building
                }

            self.redisClient.saveCoordinateCache(location, orderID[0])

        return modelv1.PredictCoordinateResponse(
            x=location["x"],
            y=location["y"],
            z=location["z"],
            label=location["label"],
            building=location["building"]
        )