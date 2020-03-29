import random
import editdistance
from parse import parse

keys = ["acct_no", "f_name", "l_name", "dob", "street_one", "street_two", "city", "state", "zip_code", "prev_f_name", "prev_m_initial", "prev_l_name", "prev_street_one", "prev_street_two", "prev_city", "prev_state", "prev_zip_code"]

def get_edit_distances(p1, p2):
    p1Dict = p1.__dict__
    p2Dict = p2.__dict__
    toReturn = {}
    for k in keys:
        if (p1Dict[k] != "" and p2Dict[k] != ""):
            d = editdistance.eval(p1Dict[k].lower(), p2Dict[k].lower())
            toReturn[k] = d
        else:
            toReturn[k] = -1
    return toReturn

def convert_dict_to_csv(distances):
    csv = ""
    for k in keys:
        if k in distances:
            csv += str(distances[k])
        csv+= ","
    return csv

def prepare(patients):
    csv = ""
    random.shuffle(patients)
    for i in range(len(patients) - 1):
        for j in range(i+1, len(patients)):
            currCSV = ""

            currCSV += patients[i].patient_id + ","
            currCSV += patients[j].patient_id + ","

            distances = get_edit_distances(patients[i], patients[j])
            currCSV += convert_dict_to_csv(distances)
            if (patients[i].group_id == patients[j].group_id):
                currCSV += "1"
            else:
                currCSV += "0"
            currCSV += "\n"

            csv += currCSV
    f = open("nn.csv","w+")
    f.write(csv)
    f.close()

patients = parse("data.csv")
prepare(patients)