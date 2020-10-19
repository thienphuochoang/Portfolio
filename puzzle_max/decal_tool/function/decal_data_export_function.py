import pymxs
import json
rt = pymxs.runtime
dataDict = {}
for obj in rt.geometry:
    objMax = list(obj.max)
    objMin = list(obj.min)
    dataDict[obj.name] = objMax, objMin
decalDataFilePath = (rt.maxfilepath.replace("\\","/")) + (rt.maxfilename).split(".")[0] + ".json"
with open(decalDataFilePath, 'w') as fp:
    json.dump(dataDict, fp)