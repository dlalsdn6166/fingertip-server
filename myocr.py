import easyocr

model_directory = 'model'
network_directory = 'network'
reader = easyocr.Reader(['ko'], gpu = True, model_storage_directory=model_directory, recog_network='custom', user_network_directory=network_directory)

def read(img):
    result = reader.readtext(img)
    return result
    
def detect(img):
    result = reader.detect(img)
    return result