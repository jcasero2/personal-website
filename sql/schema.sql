PRAGMA foreign_keys = ON;

CREATE TABLE calendar(
	teamname VARCHAR(40) NOT NULL,
	week VARCHAR(40) NOT NULL,
	games CHARACTER(64) NOT NULL,
	PRIMARY KEY (teamname)
);

CREATE TABLE users(
  username VARCHAR(20) NOT NULL,
	fullname VARCHAR(40) NOT NULL,
	email VARCHAR(40) NOT NULL,
	password CHARACTER(256) NOT NULL,
	created timestamp DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (username)
);

CREATE TABLE players(
  fullname VARCHAR(20) NOT NULL,
  username2 VARCHAR(20) NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (username1, username2),
);
