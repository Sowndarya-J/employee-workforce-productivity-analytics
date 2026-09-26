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