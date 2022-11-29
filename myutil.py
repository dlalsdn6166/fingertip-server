
def encode(ocr_result):
    result = {"results":[]}

    for i in ocr_result:
        if len(i) != 3:
            continue
        rect = i[0]
        txt = i[1]
        txt = txt.replace('\'','')
        txt = txt.replace('\"', '')
        result['results'].append({"rect":[rect[0][0],rect[2][0],rect[0][1],rect[2][1]], "text":txt})

    return str(result).encode()