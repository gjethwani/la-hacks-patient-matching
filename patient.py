class Patient:
    group_id = 0
    patient_id = 0
    acct_no = ""
    f_name = ""
    m_initial = ""
    l_name = ""
    dob = ""
    sex = ""
    street_one = ""
    street_two = ""
    city = ""
    state = ""
    zip_code = ""
    prev_f_name = ""
    prev_m_initial = ""
    prev_l_name = ""
    prev_street_one = ""
    prev_street_two = ""
    prev_city = ""
    prev_state = ""
    prev_zip_code = ""            

    def __init__(self, **kwargs):
        valid_keys = ["group_id","patient_id","acct_no","f_name","m_initial","l_name","dob","sex","street_one","street_two","city","state","zip_code","prev_f_name","prev_m_initial","prev_l_name","prev_street_one","prev_street_two","prev_city","prev_state","prev_zip_code"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))