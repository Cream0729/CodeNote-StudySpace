import json
data = [{"A": "a", "B": "b", "C": "c"}, {"D": "d", "E": "e", "F": "f"}, {"G": "g", "H": "h", "I": "i"}]
jsonData = json.dumps(data, ensure_ascii=False)
print(type(jsonData))
print(jsonData)

s = '[{"A": "a", "B": "b", "C": "c"}, {"D": "d", "E": "e", "F": "f"}, {"G": "g", "H": "h", "I": "i"}]'
l = json.loads(s)
print(type(l))