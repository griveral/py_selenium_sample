# Author: Giovanni Riveral
# version: 0.1
# Description: This test case covers
#     1. important task link test case (favorite page)
#     2. important task page and content test case (favorite page)
#     3. all tasks link test cases
#     4. all tasks page and content test case 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

from login import create_session
from myday import create_test_data, create_imp_tasks_test_data

task_list = ['task1', 'task2', 'important_task']
sleep_time = 1

def important_task(driver):
    important_link = driver.find_element_by_xpath('//div/mat-nav-list/app-nav-menu-item[3]/a')
    important_link.click()
    # time.sleep(sleep_time)

    # get all important task in the list
    imp_tasks = driver.find_element_by_xpath('//app-important-tasks-page/div').text
    # print(imp_tasks.text)

    # removing star text and it's duplicate
    imp_task_list = imp_tasks.split("\n")
    imp_task_list = list(set(imp_task_list))
    imp_task_list.remove('star')
    print('Test data list vs Actual Imp task list: {} == {}'.format(task_list, imp_task_list))
    
    # compare test data and actual task lists
    if (task_list.sort() == imp_task_list.sort()):
        # all mark task as important are found in important list link
        # PASSED
        status = 0
    else:
        status = 1

    time.sleep(sleep_time)
    return status

def all_tasks_page(driver):
    testdata_task_list = ['Test task 1', 'task1', 'task2', 'important_task']
    all_tasks_link = driver.find_element_by_xpath('//div/mat-nav-list/app-nav-menu-item[2]/a')
    all_tasks_link.click()
    # time.sleep(sleep_time)

    all_tasks = driver.find_element_by_xpath('//app-all-tasks-page/div').text
    # print(all_tasks)

    all_task_list = all_tasks.split("\n")
    all_task_list = list(set(all_task_list))
    all_task_list.remove('star')
    print('Test data list vs actual task list: {} == {}'.format(testdata_task_list, all_task_list))

    # compare test data and actual all task lists
    if (testdata_task_list.sort() == all_task_list.sort()):
        # all test data tasks are found in actual all task lists' link
        # PASSED
        status = 0
    else:
        status = 1

    time.sleep(sleep_time)
    return status


if __name__ == "__main__":
    # driver = create_test_data()
    driver = create_imp_tasks_test_data()

    it = important_task(driver)
    if (it == 0):
        print('important task - PASSED')
    else:
        print('important task - FAILED')
    
    all_page = all_tasks_page(driver)
    if (all_page == 0):
        print('All task page - PASSED')
    else:
        print('All task page - FAILED')

    driver.close()
