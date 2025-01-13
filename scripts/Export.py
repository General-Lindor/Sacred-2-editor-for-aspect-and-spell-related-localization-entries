from scripts import __basepath__

def isEntry(obj: object) -> bool:
    if isinstance(obj, dict):
        keys = list(obj.keys())
        if len(keys) == 2:
            hashes = obj.get("HASHES")
            if isinstance(hashes, list):
                for element in hashes:
                    if not isinstance(element, str):
                        return False
                value = obj.get("VALUE")
                if isinstance(value, str):
                    return True
    return False

def extractRecursive(Node: dict | list, hashMap: dict) -> dict:
    if isinstance(Node, list):
        for element in Node:
            if isinstance(element, dict | list):
                hashMap = extractRecursive(element, hashMap)
        return hashMap
    elif isEntry(Node):
        value = Node.get("VALUE")
        for hash in Node.get("HASHES"): # type: ignore
            hashMap[hash] = value
        return hashMap
    else:
        values = list(Node.values())
        for element in values:
            if isinstance(element, dict | list):
                hashMap = extractRecursive(element, hashMap)
        return hashMap

def extract(res: dict):
    return extractRecursive(res, {})

def export(res: dict, lang: str):
    hashMap = extract(res)
    with open(__basepath__ + "EXPORTED/" + lang + "/decoded.res", "w", encoding = "utf-16le") as file:
        for item in hashMap.items():
            s = item[0] + "\t" + item[1] + "\n"
            file.write(s)