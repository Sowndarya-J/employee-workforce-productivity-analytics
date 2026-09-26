-- Employee Workforce & Productivity Analytics
-- SQL Analysis Queries


-- 1. Employee Count by Department

SELECT
    Department,
    COUNT(*) AS Employee_Count
FROM employee_productivity
GROUP BY Department
ORDER BY Employee_Count DESC;


-- 2. Performance Analysis by Department

SELECT
    Department,
    COUNT(*) AS Employee_Count,
    ROUND(AVG(Performance_Score), 2) AS Avg_Performance,
    ROUND(AVG(Work_Hours_Per_Week), 2) AS Avg_Work_Hours,
    ROUND(AVG(Overtime_Hours), 2) AS Avg_Overtime_Hours,
    ROUND(AVG(Employee_Satisfaction_Score), 2) AS Avg_Satisfaction
FROM employee_productivity
GROUP BY Department
ORDER BY Avg_Performance DESC;


-- 3. Overall Resignation Rate

SELECT
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) AS Resigned_Employees,
    ROUND(
        100.0 * SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS Resignation_Rate
FROM employee_productivity;


-- 4. Resignation by Department

SELECT
    Department,
    COUNT(*) AS Employee_Count,
    SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) AS Resigned_Employees,
    ROUND(
        100.0 * SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS Resignation_Rate
FROM employee_productivity
GROUP BY Department
ORDER BY Resignation_Rate DESC;


-- 5. Resignation vs Overtime

SELECT
    CASE
        WHEN Overtime_Hours < 10 THEN 'Low Overtime'
        WHEN Overtime_Hours < 20 THEN 'Medium Overtime'
        WHEN Overtime_Hours < 30 THEN 'High Overtime'
        ELSE 'Very High Overtime'
    END AS Overtime_Group,
    COUNT(*) AS Employee_Count,
    SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) AS Resigned_Employees,
    ROUND(
        100.0 * SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS Resignation_Rate
FROM employee_productivity
GROUP BY Overtime_Group
ORDER BY Resignation_Rate DESC;


-- 6. Resignation vs Employee Satisfaction

SELECT
    CASE
        WHEN Employee_Satisfaction_Score < 2 THEN 'Low Satisfaction'
        WHEN Employee_Satisfaction_Score < 3 THEN 'Medium Satisfaction'
        WHEN Employee_Satisfaction_Score < 4 THEN 'High Satisfaction'
        ELSE 'Very High Satisfaction'
    END AS Satisfaction_Group,
    COUNT(*) AS Employee_Count,
    SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) AS Resigned_Employees,
    ROUND(
        100.0 * SUM(CASE WHEN Resigned = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS Resignation_Rate
FROM employee_productivity
GROUP BY Satisfaction_Group
ORDER BY Resignation_Rate DESC;


-- 7. Training vs Performance

SELECT
    CASE
        WHEN Training_Hours <= 25 THEN 'Low Training'
        WHEN Training_Hours <= 50 THEN 'Medium Training'
        WHEN Training_Hours <= 75 THEN 'High Training'
        ELSE 'Very High Training'
    END AS Training_Group,
    COUNT(*) AS Employee_Count,
    ROUND(AVG(Training_Hours), 2) AS Avg_Training_Hours,
    ROUND(AVG(Performance_Score), 2) AS Avg_Performance,
    ROUND(AVG(Employee_Satisfaction_Score), 2) AS Avg_Satisfaction
FROM employee_productivity
GROUP BY Training_Group
ORDER BY Avg_Training_Hours;