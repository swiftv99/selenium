| Command                                                        | Description                                     |
| -------------------------------------------------------------- | ----------------------------------------------- |
| pytest -m [math, login, positive, negative, exception, debug ] | Execute only test cases with the specified mark |
| pytest --html=reports/report.html                              | See the outputs of test cases in browser        |
| pytest --browser=firefox                                       | Run test cases in Firefox browser               |
| pytest -n=4                                                    | Run test cases in parallel (4 threads)          |


### If page_objects is not recognized by tests, run this following command
```
export PYTHONPATH=/home/abdulaziz/coding/selenium-webui:$PYTHONPATH
```