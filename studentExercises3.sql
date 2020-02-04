DROP TABLE IF EXISTS StudentExercise;

CREATE TABLE Cohort (
	Id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name	TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
	Id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName	TEXT NOT NULL,
	LastName	TEXT NOT NULL,
	SlackHandle	TEXT NOT NULL,
	CohortId	INTEGER NOT NULL,
	FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Instructor (
	Id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName	TEXT NOT NULL,
	LastName	TEXT NOT NULL,
	SlackHandle	TEXT NOT NULL,
	CohortId	INTEGER NOT NULL,
	Specialty	TEXT NOT NULL,
	FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
	Id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name		TEXT NOT NULL,
	ExLanguage	TEXT NOT NULL
);

CREATE TABLE StudentExercise (
	Id				INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentId		INTEGER NOT NULL,
	ExerciseId		INTEGER NOT NULL,
	InstructorId	INTEGER NOT NULL,
	FOREIGN KEY(StudentId) REFERENCES Student(Id)
	FOREIGN KEY(ExerciseId) REFERENCES Exercise(Id)
);

INSERT INTO Cohort
VALUES (null, "Cohort 1");

INSERT INTO Cohort
VALUES (null, "Cohort 2");

INSERT INTO Cohort
VALUES (null, "Cohort 3");

SELECT * FROM Cohort;

INSERT INTO Exercise
VALUES (null, "Exercise 1", "Python");

INSERT INTO Exercise
VALUES (null, "Exercise 2", "Python");

INSERT INTO Exercise
VALUES (null, "Exercise 3", "Javascript");

INSERT INTO Exercise
VALUES (null, "Exercise 4", "Javascript");

INSERT INTO Exercise
VALUES (null, "Exercise 5", "Java");

SELECT * FROM Exercise;

INSERT INTO Instructor
VALUES (null, "Brad", "S", "brad_slack", 1, "nerd jokes");

INSERT INTO Instructor
VALUES (null, "Josh", "D", "josh_slack", 2, "embarrassing people");

INSERT INTO Instructor
VALUES (null, "Kayla", "S", "kayla_slack", 3, "explanations");

SELECT * FROM Instructor;

INSERT INTO Student
VALUES (null, "Chase", "F", "chase_slack", 1);

INSERT INTO Student
VALUES (null, "Corri", "G", "corri_slack", 2);

INSERT INTO Student
VALUES (null, "Matt", "B", "chase_slack", 2);

INSERT INTO Student
VALUES (null, "Ryan", "B", "ryan_slack", 3);

INSERT INTO Student
VALUES (null, "Ken", "B", "ken_slack", 1);

INSERT INTO Student
VALUES (null, "Ryan", "C", "ryan_c_slack", 3);

INSERT INTO Student
VALUES (null, "Shawna", "C", "shawna_slack", 2);

SELECT * FROM Student;

INSERT INTO StudentExercise
VALUES (null, 1, 1, 1);

INSERT INTO StudentExercise
VALUES (null, 1, 2, 2);

INSERT INTO StudentExercise
VALUES (null, 2, 3, 3);

INSERT INTO StudentExercise
VALUES (null, 2, 4, 1);

INSERT INTO StudentExercise
VALUES (null, 3, 5, 2);

INSERT INTO StudentExercise
VALUES (null, 3, 1, 3);

INSERT INTO StudentExercise
VALUES (null, 4, 2, 1);

INSERT INTO StudentExercise
VALUES (null, 4, 3, 2);

INSERT INTO StudentExercise
VALUES (null, 5, 4, 3);

INSERT INTO StudentExercise
VALUES (null, 5, 5, 1);

INSERT INTO StudentExercise
VALUES (null, 6, 1, 2);

INSERT INTO StudentExercise
VALUES (null, 6, 2, 3);

INSERT INTO StudentExercise
VALUES (null, 7, 3, 1);

INSERT INTO StudentExercise
VALUES (null, 7, 4, 2);

SELECT * FROM StudentExercise;