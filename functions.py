import pandas as pd
import numpy as np


def get_all_marks(data, subj):
    #issue here is that in some years float is separated with comma and it is interpreted as string.
    #If someone never had or failed exam he has NaN or np.nan which has float or np.float64 type
    # I try to resolve it by switching comma to dot and taking out nan rows
    res = []
    fail = []
    for i in data.iterrows():
        val = i[1][subj]
        if type(val) is str:
            conv_val = np.float(val.replace(',', '.'))
            data[subj][i[0]] = conv_val
            if conv_val <0.1:
                res.append(False)
                fail.append(i[0])
            else:
                res.append(True)
        elif pd.isna(val):
            res.append(False)
        elif val <0.1:
            res.append(False)
            fail.append(i[0])
        else:
            res.append(True)
    passed = data[res]
    passed[subj] = passed[subj].astype(np.float)
    failed = data.loc[fail, :]
    failed[subj] = failed[subj].astype(np.float)
    return passed, failed

    # data1 = data.loc[pd.Series([type(i[1][subj]) is str for i in data.iterrows()])]
    # if np.shape(data1)[0] == 0:
    #     data = data.loc[pd.Series([not np.isnan(i[1][subj]) for i in data.iterrows()])]
    #     return data
    # else:
    #     data1[subj] = pd.Series([float(i[1][subj].replace(',', '.')) for i in data.iterrows()], index = data.index)
    #     return data1
