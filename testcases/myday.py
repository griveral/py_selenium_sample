# Author: Giovanni Riveral
# version: 0.1
# Description: This test case covers
#    1. creation of test data - normal task and important task
#    2. add task test case
#    3. remove task test case
#    4. marking of task as complete test case
#    5. unmarking of task from complete back to normal state test case

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

from login import create_session
task_list = ['task1', 'task2', 'important_task']
sleep_time = 1

def create_test_data():
    driver = create_session()
    task_title = driver.find_element_by_id('mat-input-2')
    task_desc = driver.find_element_by_id('mat-input-3')
    Add_btn = driver.find_element_by_id('addTask')
    # add new task
    # day = driver.find_element_by_class_name('mat-calendar-body-cell-content mat-calendar-body-selected mat-calendar-body-today').text
    
    for task in task_list:
        task_title.send_keys(task)
        str_desc = task+' '+'description'
        task_desc.send_keys(str_desc)
        if(task == 'important_task'):
            driver.find_element_by_class_name('mat-checkbox-inner-container').click()
        
        time.sleep(sleep_time)
        Add_btn.click()

    return driver

def create_imp_tasks_test_data():
    driver = create_session()
    task_title = driver.find_element_by_id('mat-input-2')
    task_desc = driver.find_element_by_id('mat-input-3')
    Add_btn = driver.find_element_by_id('addTask')
    # add new task
    # day = driver.find_element_by_class_name('mat-calendar-body-cell-content mat-calendar-body-selected mat-calendar-body-today').text
    
    for task in task_list:
        task_title.send_keys(task)
        str_desc = task+' '+'description'
        task_desc.send_keys(str_desc)
        driver.find_element_by_class_name('mat-checkbox-inner-container').click()
        
        time.sleep(sleep_time)
        Add_btn.click()

    return driver

def add_task(driver):
    # get task in the task list section
    test_data_task1 = task_list[0]
    first_task_from_list = driver.find_element_by_xpath('//div/mat-card[3]/mat-card-content/span').text
    print('{} == {}'.format (first_task_from_list,  test_data_task1))
    time.sleep(sleep_time)

    if(first_task_from_list == test_data_task1):
        # Add task PASSED
        return 0
    else:
        # Add task FAILED
        return 1

def remove_task(driver):
    rm_btn = driver.find_element_by_xpath('//div/mat-card[3]/mat-card-content/mat-icon[1]')
    rm_btn.click()
    time.sleep(sleep_time)

    test_data_task1 = task_list[1]
    first_task_from_list = driver.find_element_by_xpath('//div/mat-card[3]/mat-card-content/span').text
    print('{} == {}'.format (first_task_from_list,  test_data_task1))
    time.sleep(sleep_time)

    # task1 should be removed from the list, and task2 should be in the task list
    if(first_task_from_list == test_data_task1):
        # rm task PASSED
        return 0
    else:
        # rm task FAILED
        return 1

def mark_complete_task(driver):
    # mark task1 task to complete
    driver.find_element_by_xpath('//div/mat-card[3]/mat-card-content/mat-checkbox/label/div').click()
    # task2
    testdata_complete_task = task_list[1]

    try:
        complete_task = driver.find_element_by_class_name('completed-task')
    except NoSuchElementException:
        complete_task = 0

    # print(complete_task)
    if (complete_task != 0):
        print('completed task vs test data: {} == {}'.format(complete_task.text, testdata_complete_task))
        if (complete_task.text == testdata_complete_task):
            status = 0
        else:
            status = 1
    else:
        print('no task mark as complete')
        status = 1

    time.sleep(sleep_time)
    return status

def unmark_complete_task(driver):
    # mark task1 task to complete
    driver.find_element_by_xpath('//div/mat-card[3]/mat-card-content/mat-checkbox/label/div').click()

    try:
        complete_task = driver.find_element_by_class_name('completed-task')
    except NoSuchElementException:
        complete_task = 0

    # print(complete_task)
    if (complete_task == 0):
        # unmarking complete task is successful. No more completed task in the task list.
        status = 0
    else:
        print('unmarking of completed task in unsuccessful - {}'.format(complete_task.text))
        status = 1

    time.sleep(sleep_time)
    return status

if __name__ == "__main__":
    driver = create_test_data()
    at = add_task(driver)

    if (at == 0):
        print('Add task - PASSED')
    else:
        print('Add task - FAILED')

    rm_t = remove_task(driver)
    if (rm_t == 0):
        print('remove task - PASSED')
    else:
        print('remove task - FAILED')

    comp_task = mark_complete_task(driver)
    if (comp_task == 0):
        print('completed task - PASSED')
    else:
        print('completed task - FAILED')
    
    unmark_comp_task = unmark_complete_task(driver)
    if (unmark_comp_task == 0):
        print('unmarking completed task - PASSED')
    else:
        print('unmarking completed task - FAILED')

    driver.close()




