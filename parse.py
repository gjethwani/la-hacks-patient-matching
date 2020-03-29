import csv
from patient import Patient

states = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PW": "Palau",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

def sanitize_state(state):
    for k in states:
        if states[k].lower() == state.lower():
            return k
    return state
 

def parse(filename):
    patients = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                sex = row[7]
                if sex.lower() == "male":
                    sex = "m"
                if sex.lower() == "female":
                    sex = "f"
                patients.append(Patient(group_id = row[0], patient_id = row[1], acct_no = row[2], f_name = row[3], m_initial = row[4], l_name = row[5], dob = row[6], sex = sex, street_one = row[8], street_two = row[9], city = row[10], state = sanitize_state(row[11]), zip_code = row[12], prev_f_name = row[13], prev_m_initial = row[14], prev_l_name = row[15], prev_street_one = row[16], prev_street_two = row[17], prev_city = row[18], prev_state = sanitize_state(row[19]), prev_zip_code = row[20]))
                line_count += 1
        print(f'Processed {line_count} lines.')
    return patients

def convert_train_data_to_array(filename):
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        curr_group_id = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                group_id = int(row[0])
                patient_id = int(row[1])
                if len(result) == 0:
                    result.append([patient_id])
                    curr_group_id = group_id
                else:
                    if group_id == curr_group_id:
                        result[-1].append(patient_id)
                    else:
                        curr_group_id = group_id
                        result.append([patient_id])
                line_count += 1
        print(f'Processed {line_count} lines.')
    return result