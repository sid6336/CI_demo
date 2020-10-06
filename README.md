# CI_demo
(Training) CI demo

#Continuous Integration, 6-Oct-2020
#https://realpython.com/python-continuous-integration/

#1.create a git repo & clone the repo to the local folder
"""
git clone https://github.com/sid6336/CI_demo.git
"""

#2.set up environment
"""
conda create -n CI_demo flake8 pytest pytest-cov
conda activate CI_demo
"""

#3.conda env export
"""
go to the local folder
conda env export > CI_demo.yml
"""

#4.create CI_demo.py 

#5.Commit to GIT
"""
Go to the folder
git remote add origin git_repo_path
git config --global user.email 'xxx'
git add CI_demo.py
git commit -m "initial commit"
git status
git push origin master
git log
"""

#6.Flake8 is commonly used to check if your code conforms to the standard Python coding style.
"""
flake8 --statistics
"""

#7. Unit Test
"""
create test_calculator.py
pytest -v --cov
"""