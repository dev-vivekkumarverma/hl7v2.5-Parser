from .typedef import v2EncodingChars
def get_encoding_characters(messageHeaderSegment:str)->v2EncodingChars:
    encodeCharMap=v2EncodingChars()
    if messageHeaderSegment.startswith("MSH"):
        dataFieldSep=messageHeaderSegment[3]
        encodeCharMap['dataFieldSep']=dataFieldSep
        encodingDataField=messageHeaderSegment.split(dataFieldSep)[1]
        encodeCharMap['componentSep']=encodingDataField[0]
        encodeCharMap['repetitionSep']=encodingDataField[1]
        encodeCharMap['escapeSeq']=encodingDataField[2]
        encodeCharMap['sub-componentSep']=encodingDataField[3]
    else:
        raise Exception("Not s HL7-v2 message header segment")
    
    return encodeCharMap