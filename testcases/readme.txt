1. task manager ui app requirements should be install.
2. task manager app is running or serving
3. For testing
    a. install pandas
        pip install pandas
    b. There are 3 py scripts
        b.1. login.py
        b.2. myday.py
        b.3. pages.py
        these can be run individually. 
        python <script>.py
    c. test_suite.py - this will run all the test cases.
        python test_suite.py
    d. csv/features.csv - this is the controller file to turn on/off the testcase.
        d.1. Note that add/rm/unmark/mark test cases should be turn on/off together.
        d.2. Likewise with all task page and important task page test cases
    e. test_summary_result.csv - this will be generated after the test_suite.py is run. It will display all the test cases and their respective status.
    f. make sure selenium/browser drivers (chrome)/etc are properly configure
    g. every py script has a sleep_time variable. I set it to 1sec, you can increase this if you want to slower down the automation driver.
4. Bugs founds:
    4.1. Important task page. This feature cannot load a newly added task
        a. when you remove an important task, this will still be in the important task list
    4.2. Important task cannot be set back as normal task
    4.3. Existing task cannot be mark as important.
    4.4. Cannot clearly mark task to done
    4.5. Change password popup appear every session or login


Thank you. This is really a good exercise :)

