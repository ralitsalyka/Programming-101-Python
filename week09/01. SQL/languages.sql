CREATE TABLE task1(
  id INTEGER PRIMARY KEY, 
  language VARCHAR(255),
  answer VARCHAR(255),
  answered INTEGER,
  guide TEXT);

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (1, 'Python', 'google', 0, 'A folder named Python was created. Go there and fight with program.py!');

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (2, 'Go', '200 OK', 0, 'A folder named Go was created. Go there and try to make Google Go run.');

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (3, 'Java', 'object oriented programming', 0, 'A folder named Java was created. Can you handle the class?');

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (4, 'Haskell', 'Lambda', 0, 'Something pure has landed. Go to Haskell folder and see it!');

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (5, 'C#', '  NDI=', 0, 'Do you see sharp? Go to the C# folder and check out.');

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (6, 'Ruby', 'https://www.ruby-lang.org/bg/', 0, 'Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!');

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (7, 'C++', 'header files', 0, "Here be dragons! It's C++ time. Go to the C++ folder.");

INSERT INTO task1 (id, language, answer, answered, guide)
VALUES (8, 'JavaScript', 'Douglas Crockford', 0, 'NodeJS time. Go to JavaScript folder and Node your way!');

ALTER TABLE task1
    ADD COLUMN rating INTEGER;

UPDATE task1
SET Rating = 1
WHERE Language = "Python";

UPDATE task1
SET Rating = 2
WHERE Language = "Go";

UPDATE task1
SET Rating = 3
WHERE Language = "Java";

UPDATE task1
SET Rating = 9
WHERE Language = "Haskell";

UPDATE task1
SET Rating = 8
WHERE Language = "C#";

UPDATE task1
SET Rating = 7
WHERE Language = "Ruby";

UPDATE task1
SET Rating = 4
WHERE Language = "C++";

UPDATE task1
SET Rating = 5
WHERE Language = "JavaScript";

UPDATE task1
SET Answered = 1
WHERE Language = "Python";

UPDATE task1
SET Answered = 1
WHERE Language = "Go"; 

SELECT Language
FROM task1
WHERE Answer == "200 OK" or Answer == "Lambda";