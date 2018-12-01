OBJECT_VERB_LIST = {
    "formwork_material":["not_interacting_with","next_to","carrying","standing_on","installing"],
    "scaffolding":["not_interacting_with","next_to","standing_on","installing","standing_in"],
    "formwork_working":["not_interacting_with","next_to","standing_on","installing","uninstalling"],
    "steel":["not_interacting_with","next_to","standing_on","installing"],
    "dump_truck":["not_interacting_with","operating","standing_on","next_to"],
    "crane":["not_interacting_with","operating","standing_under","next_to"],
    "excavator":["not_interacting_with","next_to","operating","standing_under"],
    "rebar_material":["not_interacting_with","next_to","carrying","welding"],
    "rebar_working":["not_interacting_with","next_to","installing"],
    "machine_other":["not_interacting_with","operating","next_to"],
    "tower_crane":["not_interacting_with","standing_under","next_to"],
    "concrete_pump":["not_interacting_with","operating","next_to"],
    "concrete_mixer":["not_interacting_with","operating","next_to"],
    "bulldozer":["not_interacting_with","operating","next_to"],
    "concrete_bucket":["not_interacting_with","operating","next_to"],
    "concrete_pouring":["not_interacting_with","leveling"]
}
VERB_LIST=["next_to","installing","standing_on","standing_in","carrying","welding","uninstalling","leveling","operating","standing_under","not_interacting_with",]

VERB_EXPLANATION ={
    "next_to":"交互人和对象靠得很近，正在构成或即将构成交互关系",
    "installing":"交互人正在安装对象（模板 钢筋等）",
    "standing_on":"交互人站在交互对象的空间上方",
    "standing_in":"交互人站在交互对象的空间内部（脚手架）",
    "carrying":"交互人正持有交互对象",
    "welding":"交互人正在焊接对象（钢筋）",
    "uninstalling":"交互人正在拆除对象（模板）",
    "leveling":"交互人正在整平对象（混凝土）",
    "operating":"交互人正在操作对象（机器设备）",
    "standing_under":"交互人站在对象的正下方（塔吊 吊车等）",
    "not_interacting_with":"交互人和对象在空间上有一定距离，没有明确的交互关系",
}

OBJECT_EXPLANATION = {
    "rebar_working":"使用中的钢筋",
    "scaffolding":"脚手架",
    "rebar_material":"钢筋材料",
    "steel":"钢构件",
    "formwork_working":"使用中的模板",
    "formwork_material":"模板材料",
    "concrete_pouring":"倾倒中的混凝土",
    "machine_other":"其他设备",
    "excavator":"挖掘机",
    "tower_crane":"塔吊",
    "crane":"吊车",
    "dump_truck":"自卸车",
    "concrete_pump":"混凝土泵车",
    "concrete_mixer":"混凝土搅拌车",
    "bulldozer":"推土机"
}

def possible_verbs_explanations(object_type):
    if object_type in OBJECT_VERB_LIST:
        verblist = OBJECT_VERB_LIST[object_type]
    else:
        verblist = []
    result= []
    for verb in verblist:
        result.append({"verb":verb,"explanation":VERB_EXPLANATION[verb]})
    return result

def possible_verbs(object_type):
    if object_type in OBJECT_VERB_LIST:
        verblist = OBJECT_VERB_LIST[object_type]
    else:
        verblist = []
    return verblist

def explanation():
    return VERB_EXPLANATION

def to_anno(anno):
    result=""
    for i in range(len(VERB_LIST)):
        if VERB_LIST[i] in anno:
            result +='1'
        else:
            result +='0'
    return result

def object_explain(object_type):
    return OBJECT_EXPLANATION[object_type]

if __name__ =="__main__":
    print(possible_verbs("scaffoldin"))