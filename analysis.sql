-----SQL
SELECT TOP 5 Company_Name, Avg_Salary
FROM DS_Jobs
ORDER BY CAST(Avg_Salary AS FLOAT) DESC;