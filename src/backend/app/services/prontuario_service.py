import os, json
def build_prontuario(user_id):
    base = {"user_id": user_id, "fotos": {}}
    # look at data/captures for available images
    capt_dir = os.path.abspath(os.path.join(os.getcwd(),"..","..","data","captures"))
    if os.path.exists(capt_dir):
        for f in os.listdir(capt_dir):
            base["fotos"][f] = os.path.join("data","captures", f)
    return base
