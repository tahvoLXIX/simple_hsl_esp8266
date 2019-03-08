import urequests
import ujson
HSL_QUERY = '{"query":"{\\n  stop(id:\\"xxxDIGITRANSIT_STATION_IDxxx\\") {\\n name\\n stoptimesWithoutPatterns(numberOfDepartures: 10, startTime: xxxSTART_TIMExxx) {\\n serviceDay\\n realtimeDeparture\\n trip {\\n route {\\n shortName\\n }\\n }\\n headsign\\n }\\n  } \\n}","variables":null,"operationName":null}'

STATION_K = 'xxxDIGITRANSIT_STATION_IDxxx'
TIME_K = 'xxxSTART_TIMExxx'
STOP_ID = 'HSL:1462106'


HSL_API_URL = 'https://api.digitransit.fi:443/routing/v1/routers/hsl/index/graphql'
HSL_API_HEADERS = {'Content-type' : 'application/json'}


def make_query(timestamp, stop_id=STOP_ID):
    return HSL_QUERY.replace(STATION_K, stop_id).replace(TIME_K, str(timestamp))


def doit(ts, stop_id=STOP_ID):
    print('fetching for ts {}'.format(ts))
    return urequests.post(HSL_API_URL, data=make_query(ts, stop_id), headers=HSL_API_HEADERS)

def transform_response(res):
    try:
        if res.status_code != 200:
            return []
        d = ujson.loads(res.content.decode('utf-8'))
        data = d['data']['stop']['stoptimesWithoutPatterns']
        # NOTE - hsl might actually return these already sorted hmm
        # in that case, just return data
        sorted_items = [item for _, item in sorted([ (item['serviceDay'] + item['realtimeDeparture'], item) for item in data], key = lambda item : item[0])]
        return sorted_items
    except Exception as ex:
        print(ex)
        return []
