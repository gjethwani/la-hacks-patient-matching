from parse import parse
from prepare import get_edit_distances, convert_dict_to_csv
from keras.models import model_from_json
import numpy as np

def generate_accuracy_array(groups):
    result = []
    for g in groups:
        to_push = []
        for i in g:
            to_push.append(int(i.patient_id))
        result.append(to_push)
    return result

def dump_to_file(result):
    result_txt = ""
    group_id = 1
    for r in result:
        result_txt += str(group_id) + ": "
        for i in r:
            result_txt += str(i) + " "
        group_id += 1
        result_txt += "\n"

    f = open("result.txt","w+")
    f.write(result_txt)
    f.close()

def load_model():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    return loaded_model

def predict(filename, model, yes_threshold):
    groups = []
    patients = parse(filename)
    for p in patients:
        if len(groups) == 0:
            groups.append([p])
        else:
            appended = 0
            for i in range(len(groups)):
                group_distances = []
                for j in range(len(groups[i])):
                    distances = get_edit_distances(groups[i][j], p)
                    csv = convert_dict_to_csv(distances)
                    arr = csv[:-1].split(",")
                    for k in range(len(arr)):
                        arr[k] = int(arr[k])
                    group_distances.append(arr)
                classes = model.predict_classes(np.array(group_distances))
                ones = 0
                for c in classes:
                    if c == 1:
                        ones += 1
                if (int(p.patient_id) == 555):
                    print(ones)
                if (float(ones) / float(len(groups[i]))) > yes_threshold:
                    groups[i].append(p)
                    appended = 1
                    break
            if appended == 0:
                groups.append([p])
    return groups

loaded_model = load_model()
groups = predict("input.csv", loaded_model, 0.5)
accuracy_array = generate_accuracy_array(groups)
print(accuracy_array)
dump_to_file(accuracy_array)




