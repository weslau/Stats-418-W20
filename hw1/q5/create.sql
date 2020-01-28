CREATE TABLE stores (
    store_name VARCHAR (64) NOT NULL
                          PRIMARY KEY
);


CREATE TABLE sales (
    store_name VARCHAR (64) NOT NULL
                            REFERENCES stores (store_name) ON DELETE NO ACTION
                                                           ON UPDATE CASCADE
                                                           MATCH SIMPLE,
    sale_date  DATE,
    num_sold   INT

)

/*SELECT name FROM PRAGMA_TABLE_INFO('DATA');
INSERT INTO stores (store_name) SELECT name FROM PRAGMA_TABLE_INFO('DATA') OFFSET 1 ROWS


INSERT INTO stores (store_name) SELECT name FROM PRAGMA_TABLE_INFO('DATA') EXCEPT 
SELECT name FROM PRAGMA_TABLE_INFO('DATA') ORDER BY name ASC LIMIT 1*/

INSERT INTO stores (store_name) SELECT name FROM PRAGMA_TABLE_INFO('DATA') LIMIT 10 OFFSET 1

INSERT into sales (
store_name, sale_date, num_sold
)
SELECT 'S1', Date, S1 from DATA
INSERT into sales (
store_name, sale_date, num_sold
)
SELECT 'S2', Date, S2 from DATA



INSERT into sales (
store_name, sale_date, num_sold
)
SELECT 'S1', Date, S1 from DATA
UNION ALL
SELECT 'S2', Date, S2 from DATA
UNION ALL
SELECT 'S3', Date, S3 from DATA
UNION ALL
SELECT 'S4', Date, S3 from DATA
UNION ALL
SELECT 'S5', Date, S5 from DATA
UNION ALL
SELECT 'S6', Date, S6 from DATA
UNION ALL
SELECT 'S7', Date, S7 from DATA
UNION ALL
SELECT 'S8', Date, S8 from DATA
UNION ALL
SELECT 'S9', Date, S9 from DATA
UNION ALL
SELECT 'S10', Date, S10 from DATA

/* you have now created two tables from the import of data.csv into DATA table in sql done through pandas*/
/* Write an SQL script hw1/q5/queries.sql to answer the following queries:
5.2 Which store makes the maximum sales on Sundays?
5.3 Find all stores with total sales in December lower than those of S5.
5.4 Which store recorded the highest number of sales for the largest number of days?
5.5 What week in 2019 has the highest total sales across all the stores?
*/