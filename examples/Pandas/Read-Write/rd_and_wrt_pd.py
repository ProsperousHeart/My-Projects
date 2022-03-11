# pip install pandas
import pandas as pd
import numpy as np

# https://prosperousheart.com/python-visualizers
# import snoop
from loguru import logger

file_name_c = "gsom_sample_csv.csv"
file_name_x = "gsom_sample_xlsx.xlsx"


# @snoop
@logger.catch
def get_num(req: int):
    """
    This function expects to take in 2 numbers: 1, 0
        - 1:  1st round (file type to read in from)
        - 0:  last round (file type to write to)

    Gets user input and returns a 2 element tuple:
        - typecast int of acceptable user input str ("1" or "2")
        - file type str ("csv" or "xlsx")
    """
    if req not in [0, 1]:
        return None
    else:
        if req == 0:
            strt = "OUTPUT OPTION:  "
        else:
            strt = "INPUT OPTION:  "
    while True:
        itm = input(f"{strt}Provide 1 for CSV or 2 for XLS:\t")
        if itm in ["1", "2"]:
            if itm == "1":
                xtra = "csv"
            else:
                xtra = "xlsx"
            return int(itm), xtra


if __name__ == "__main__":
    """
    Takes in 2 input from user:
        - only acceptable response is "1" or "2"
        - 1st:  type of file they want to read from
        - 2nd:  type of file to write to
    
    Completes requested task - only utilizing
    some columns of original DataFrame.
    """

    # https://www.interviewqs.com/ddi-code-snippets/create-df-random-integers
    new_frame = pd.DataFrame(np.random.randint(0, 100, size=(7, 3)), columns=['yo', 'wut', 'up'])
    file_name = ""
    for item in [1, 0]:
        choice, rst = get_num(item)
        # choice = None
        if choice is None:
            print("Somehow there's a problem?")
            break
        if item == 1:
            tmp_name = f"in_{rst}"
            if choice == 1:
                # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
                new_frame = pd.read_csv(file_name_c, header=0)
            else:
                # https://pandas.pydata.org/docs/user_guide/io.html#excel-files
                new_frame = pd.read_excel(file_name_x, header=0)
                # new_frame = pd.read_excel(file_name_x, engine="openpyxl", header=0)
        else:
            tmp_name = f"_out_{rst}.{rst}"
        file_name += tmp_name
        if item == 0:
            tmp_frm = new_frame[["STATION", "NAME", "LATITUDE", "LONGITUDE"]]
            print(file_name + "\n", tmp_frm)
            if choice == 1:
                tmp_frm.to_csv(file_name, index=False)
            else:
                # https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter
                with pd.ExcelWriter(file_name) as wrtr:
                    tmp_frm.to_excel(wrtr, index=False)
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html
    print(new_frame.head(3))
