# SQL Alchemy Challenge

* The task of this challenge is to examine the available database for employee, from 1980s to 1990s. The employee database is consisted of 6 CSV files with various
* data properties such as employee ID, name, department, salary, starting and end of working date. 

## Step 1 - Climate Analysis and Exploration

### *File Output: climate_starter.ipynb

### 1.1) Precipitation Analysis

![](Images_Output/Precipitation.png)

### 1.2) Station Analysis

![](Images_Output/PTemperaturevsFrequency.png)




* The above diagram show the relationship among 6 table / database (stored as CSV files under the folder "data"). As can be seen, the unique code (or primary key) is located in "dept_no"
* under Departments database and "emp_no" under Employee database. Other database will use reference to those two. 


## Step 2 -  Climate App
![](ERD-Employee_Database.png)
### *File Output: app.py

* From the previous diagram in Data Modeling, we can create a table schema which specify the data type, primary key, and foreign key. 


## Bonus: Other Recommended Analyses
### Temperature Analysis I
![](Images_Output/TripAvgTemp.png)
### File Output: query.sql

### Temperature Analysis II
![](Images_Output/AreaPlot.png)
### File Output: query.sql

* With variety of queries command in Postgress,  we can show the relation for these 8: 

* 1) List the following details of each employee: employee number, last name, first name, gender, and salary.

* 2) List employees who were hired in 1986.

* 3) List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

* 4) List the department of each employee with the following information: employee number, last name, first name, and department name.

* 5) List all employees whose first name is "Hercules" and last names begin with "B."

* 6) List all employees in the Sales department, including their employee number, last name, first name, and department name.

* 7) List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

* 8) In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.


* Analysis: It is worth noted that the same employee can be recorded more than one time and have more than one employee ID. The reason is that one employee can work in more than one department. 
* A detail look at "from_date" and "start_date" column will show us the different duration that employee has worked on each departments.   


## IV) Bonus
### File Output: SalaryHistogramBarChart.ipynb
* Create histogram for employee salary range. 

* Create bar chart for salary per job title. 

![](image_output/AverageSalaryTitle.png)

* Analysis: Majority of the salary falls into the lowest range. Highest average salary are for senior staff and staff. 