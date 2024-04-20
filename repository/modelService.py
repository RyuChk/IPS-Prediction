import joblib
import functools
import os
import pandas as pd

@functools.lru_cache(maxsize=256)
def LoadPredictionModel(building):
    if building == "CMKL":
        model_directory = "./model/"
        lr = joblib.load(model_directory+"cmkl_model.pkl")  # Load "model.pkl"
        print('Model loaded')
    else:
        print("invalid building")
        return None, True

    return lr, False

def PredictUserLocation(lr, request):
    strengths = request.strength
    req_obj = {"strengths": strengths}

    apColumns, err = convertStrengthToAPs(req_obj)
    if err:
        return 1, True
    
    query = pd.DataFrame(apColumns, index=[0])
    pred = list(lr.predict(query))
    return pred, False

def convertStrengthToAPs(rssi):
    ap = {}
    strengths = rssi["strengths"]
    prefix = "RSSI"
    maxAP = int(os.getenv("MAX_AP"))

    if len(strengths) != maxAP:
        return 1, True
    for i in range(maxAP):
        ap_name = prefix+str(i+1)
        ap[ap_name] = strengths[i]
        
    return ap, False