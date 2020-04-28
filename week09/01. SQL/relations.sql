SELECT starname
FROM STARSIN
JOIN MOVIESTAR on starname = name
WHERE gender = 'M' and movietitle = 'Terms of Endearment';

SELECT starname
FROM STARSIN
join MOVIE on movietitle = title and Movieyear = Year
WHERE studioname = 'MGM' and movieyear = 1995;

ALTER TABLE STUDIO
    ADD COLUMN President TEXT;

##Used table from task2, that's why there are only two rows for update
UPDATE STUDIO
SET President = 'George'
WHERE Name = "MGM";

UPDATE STUDIO
SET President = 'Nick'
WHERE Name = "USA Entertainm.";

Select President
From STUDIO
WHERE Name = "MGM";
