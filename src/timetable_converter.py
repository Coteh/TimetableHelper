from src.timetable_types import SlotType

slotStrDic = {
    SlotType.none : "NONE",
    SlotType.lecture : "LEC",
    SlotType.lab : "LAB",
    SlotType.exam : "EXAM"
}

slotStrToEnumConvertDic = {
    "lecture" : SlotType.lecture,
    "lab" : SlotType.lab,
    "exam" : SlotType.exam
}

def slotTypeAsString(slotType):
    slotStr = ""
    try:
        slotStr = slotStrDic[slotType]
    except KeyError as e:
        slotStr = slotStrDic[SlotType.none]
    return slotStr

def slotTypeStringAsType(slotTypeStr):
    slotType = SlotType.none
    try:
        slotType = slotStrToEnumConvertDic[slotTypeStr]
    except KeyError as e:
        pass
    return slotType
