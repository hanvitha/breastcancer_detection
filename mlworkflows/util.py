import numpy as np

import os
import cloudpickle as cp

def serialize_to(obj, default_filename):
    filename = os.getenv("S2I_PIPELINE_STAGE_SAVE_FILE", default_filename)
    cp.dump(obj, open(default_filename, "wb"))
    cp.dump(obj, open(filename, "wb"))


