SELECT avg(speed)
FROM pc;

SELECT maker, avg(screen)
FROM laptop
JOIN product on product.model = laptop.model
GROUP BY maker;

SELECT avg(speed)
FROM laptop
WHERE price > 1000;

SELECT avg(price)
FROM pc
GROUP BY hd;

SELECT avg(price)
FROM pc 
WHERE speed > 500
GROUP BY speed;

SELECT avg(price)
FROM pc 
JOIN product on product.model = pc.model 
GROUP BY maker like 'A';

SELECT avg(price)
FROM pc 
JOIN product on product.model = pc.model 
GROUP BY maker like 'B'
UNION ALL
SELECT avg(price)
FROM laptop
JOIN product on product.model = laptop.model 
GROUP BY maker like 'B';

SELECT maker
FROM product
WHERE type='PC'
GROUP BY maker
HAVING count(maker) >= 3;


SELECT maker
FROM product
JOIN pc ON product.model = pc.model
WHERE price = (SELECT max(price)
                FROM pc
                );


SELECT avg(hd)
FROM PC
LEFT OUTER JOIN product ON product.model = pc.model
GROUP BY maker
HAVING maker in (SELECT maker 
                  FROM product
                  WHERE type = 'Printer');