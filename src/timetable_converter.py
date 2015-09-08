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
    return slotStrDic[slotType]

def slotTypeStringAsType(slotTypeStr):
    return slotStrToEnumConvertDic[slotTypeStr]
