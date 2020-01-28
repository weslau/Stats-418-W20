/* you have now created two tables from the import of data.csv into DATA table in sql done through pandas*/
/* Write an SQL script hw1/q5/queries.sql to answer the following queries:


5.2 Which store makes the maximum sales on Sundays?
5.3 Find all stores with total sales in December lower than those of S5.
5.4 Which store recorded the highest number of sales for the largest number of days?
5.5 What week in 2019 has the highest total sales across all the stores?
*/

/*5.2 Which store makes the maximum sales on Sundays? = Store 2

SELECT * FROM sales WHERE strftime('%w', sale_date)= '0'

SELECT
   SUM(num_sold)  
FROM
   sales WHERE strftime('%w', sale_date)= '0'
GROUP BY
   store_name;
   
SELECT
   SUM(num_sold)  
FROM
   sales 
WHERE 
    strftime('%w', sale_date)= '0'
GROUP BY
   store_name
ORDER BY
    SUM(num_sold) DESC;
*/
SELECT store_name,
       SUM(num_sold) 
  FROM sales
 WHERE strftime('%w', sale_date) = '0'
 GROUP BY store_name
 ORDER BY SUM(num_sold) DESC;
   

/*
5.3 Find all stores with total sales in December lower than those of S5. label num_sold sum in dec as dec_sold
*/
CREATE VIEW dec_sales 
AS 
SELECT store_name,
       SUM(num_sold) AS dec_sold
  FROM sales
 WHERE strftime('%m', sale_date) = '12'
 GROUP BY store_name
 ORDER BY SUM(num_sold) DESC

/*above gets all the stuff sold in dec, below gets all the stuff sold in dec by S5
SELECT SUM(num_sold) from sales WHERE strftime('%m', sale_date) = '12' AND store_name = 'S5'
*/
/* figure out how to store variables in SQL*/ 
CREATE VIEW S5_sales
AS
SELECT SUM(num_sold) from sales WHERE strftime('%m', sale_date) = '12' AND store_name = 'S5'

SELECT store_name
FROM dec_sales
WHERE dec_sold < (SELECT * FROM S5_sales)

/*
5.4 Which store recorded the highest number of sales for the largest number of days? what does this mean?


select *
from (
select
    sale_date, max(num_sold) as _max
from sales
group by sale_date
) t, sales
where t.sale_date = sales.sale_date and t._max = sales.num_sold
order by sales.sale_date
*/
/* now you have a list thats inner joined, shows which store won each day. you just need to count up the number of times each store  name appears on this table*/
SELECT store_name, COUNT(store_name) from
(
select *
from (
select
    sale_date, max(num_sold) as _max
from sales
group by sale_date
) t, sales
where t.sale_date = sales.sale_date and t._max = sales.num_sold
order by sales.sale_date
)
GROUP BY store_name
ORDER BY COUNT(store_name) DESC


/*
5.5 What week in 2019 has the highest total sales across all the stores? answer = 18th week?

SELECT SUM(num_sold) AS all_store_sales, sale_date
FROM sales
GROUP BY sale_date

SELECT strftime('%m', timestamp), count(*) FROM Data
WHERE timestamp >= strftime('%s', '2019-01-01 00:00:00') 
AND timestamp < strftime('%s', '2020-01-01 00:00:00') 
GROUP BY strftime('%m', timestamp);
*/

SELECT strftime('%W', sale_date), SUM(all_store_sales) FROM
(
SELECT SUM(num_sold) AS all_store_sales, sale_date
FROM sales
GROUP BY sale_date
)
WHERE sale_date >= strftime('%Y-%m-%d', '2019-01-01') 
AND sale_date < strftime('%Y-%m-%d', '2020-01-01') 
GROUP BY strftime('%W', sale_date);

/* why isn't this producing correct result, checking it by the data.csv adding by week? filtering by week seems to work, are we not supposed to sum all store sales?
in the innner table, it seems like day 1 sales added across all stores is 540 instead of 533 from inspecting CSV... why?
*/