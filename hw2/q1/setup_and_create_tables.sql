/*init create_tables.sql test.sqlite3
.open test.sqlite3
.open create_tables.sql
.dump create_tables.sql*/

.open movieratings.db

CREATE TABLE Movies (
    title VARCHAR (64) NOT NULL
    PRIMARY KEY,
    year INT, 
    genre VARCHAR (64),
    rating REAL,

    numvotes INT,
    plot VARCHAR (128),
    CHECK (year>1887 AND year <2021),
    CHECK (rating>=1 AND rating <=10)
);

CREATE TABLE Ratings (
    username VARCHAR(64) NOT NULL,
    movie_title VARCHAR(64) NOT NULL, 
    rating INT,
    CHECK (rating>=1 AND rating <=10),
    
     FOREIGN KEY(username) REFERENCES Users (username) ON DELETE NO ACTION
                                                           ON UPDATE CASCADE
                                                           MATCH SIMPLE,
     FOREIGN KEY(movie_title) REFERENCES Movies (movie_title) ON DELETE NO ACTION
                                                           ON UPDATE CASCADE
                                                           MATCH SIMPLE
    
);

CREATE TABLE Users (
    username VARCHAR(64) NOT NULL
    PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL
)