SELECT address
FROM STUDIO
WHERE name = 'MGM';

SELECT birthdate
FROM MOVIESTAR
WHERE name = 'Kim Basinger';

SELECT name
FROM MOVIEEXEC
WHERE networth > 10000000;

SELECT name
FROM MOVIESTAR
WHERE gender == 'M' OR address == 'Prefect Rd.';

INSERT INTO MOVIESTAR (Name, Address, Gender, Birthdate)
VALUES ( 'Zahari Baharov', 'Lozenetz, Sofia', 'M', '1970-12-12');

DELETE FROM STUDIO
WHERE address LIKE "%5%";

UPDATE MOVIE
SET  studioname = 'Fox'
WHERE Title Like "%Str%";
