# Author: Giovanni Riveral
# version: 0.1
# Description: This test suite will controll all the test.

import pandas as pd
from datetime import datetime
from login import *
from myday import *
from pages import *

myday_driver = create_test_data()
pages_driver = create_imp_tasks_test_data()

def run_test_cases():
    print(datetime.now())
    test_cases = pd.read_csv('../csv/features.csv')
    column_names = ['Test case','status']
    test_summary_result = pd.DataFrame(columns=column_names)

    for i in range(len(test_cases)):
        tc = test_cases.loc[i, "testcase"]
        is_active = test_cases.loc[i, "is_active"]
        if(is_active.lower() == 'y'):
            if (tc == 'Wrong credentials'):
                wc = wrong_credential()
                if(wc == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
            elif(tc == 'Landing page'):
                lp = landing_page()
                if(lp == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
            # myday test cases
            elif(tc == 'Add task'):
                at = add_task(myday_driver)
                if (at == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
            elif(tc == 'Remove task'):
                rm_t = remove_task(myday_driver)
                if (rm_t == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
            elif(tc == 'Mark complete task'):
                comp_task = mark_complete_task(myday_driver)
                if (comp_task == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
            elif(tc == 'Unmark complete task'):
                unmark_comp_task = unmark_complete_task(myday_driver)
                if (unmark_comp_task == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
                # note: same driver with add/rm/mark/unmark testcases..
                myday_driver.close()
            # pages test cases
            elif(tc == 'Important task page'):
                it = important_task(pages_driver)
                if (it == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
            elif(tc == 'All task page'):
                all_page = all_tasks_page(pages_driver)
                if (all_page == 0):
                    status = 'PASSED'
                else:
                    status = 'FAILED'
                pages_driver.close()

            new_record = {
                            'Test case': tc,
                            'status': status
                        }
            test_summary_result = test_summary_result.append(new_record,ignore_index=True)

    print('\n Test Result Summary:')
    print('=================================')
    print(test_summary_result)
    test_summary_result.to_csv ('../csv/test_summary_result.csv', index = False, header=True)
    print(datetime.now())

if __name__ == "__main__":
    run_test_cases()