import libgeohash as gh

def getGeoHash(lat, lng, num_precision=9):
    return gh.encode(lat=lat, lon=lng, precision=num_precision)

def getBoundingBoxForGeoHash(ghash, commaSep=False):
    bbox = gh.bbox(ghash, False)
    if not commaSep:
        return bbox
    return str(bbox['s']) + ',' + str(bbox['w']) + ',' + str(bbox['n']) + ',' + str(bbox['e'])

def getTopLeftCornerOfBoundingBox(ghash):
    bbox = gh.bbox(ghash, False)
    lat = bbox['n']
    lng = bbox['w']
    return lat, lng

def getTopRightCornerOfBoundingBox(ghash):
    bbox = gh.bbox(ghash, False)
    lat = bbox['n']
    lng = bbox['e']
    return lat, lng

def getBottomLeftCornerOfBoundingBox(ghash):
    bbox = gh.bbox(ghash, False)
    lat = bbox['s']
    lng = bbox['w']
    return lat, lng

def getBottomRightCornerOfBoundingBox(ghash):
    bbox = gh.bbox(ghash, False)
    lat = bbox['s']
    lng = bbox['e']
    return lat, lng

def getMidPointOfGeoHash(ghash):
    return getBoundingBoxMidPoint(gh.bbox(ghash, False))

def getBoundingBoxMidPoint(bbox):
    return getMidPoint(bbox['n'], bbox['s'], bbox['e'], bbox['w'])

def getMidPoint(northLat, southLat, eastLng, westLng):
    midLat = (northLat + southLat) / 2.0
    midLng = (eastLng + westLng) / 2.0
    return midLat, midLng