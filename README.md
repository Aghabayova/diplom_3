# Diploma Project 3:
## Automation test of Web Application [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
### Prepared By: Samira Aghabayova


## Test Coverage(All the tests are located in the "tests" directory")


1. test_login_page.py 
2. test_main_page.py 
3. test_order_page.py 
4. test_profile_page.py 
5. test_retrieve_password_page.py 


Notes: some of the tests are inconsistent in firefox such as test_check_order_in_progress or test_add_ingredient_check_counter, but they are working in chrome. 

The list of all installed libraries is specified in the `requirements.txt` file.  
Before running the project, it is necessary to execute the command:

```bash
pip3 install -r requirements.txt
```
Run the Tests with pytest:
```bash
pytest -v
```