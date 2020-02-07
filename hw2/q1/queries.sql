/*
print counts of movies with at least 1000 votes, grouped by their rating bin.
All movies with the same integer part of rating fall in the same rating bin.
*/

SELECT COUNT(title), SUBSTR(rating,1,1) AS ratebin 
FROM Movies
WHERE numvotes>=1000
GROUP BY ratebin;

/*
SELECT COUNT(title), rating
FROM Movies
WHERE numvotes>=1000
GROUP BY rating
*/