# Creating DB
DROP DATABASE IF EXISTS Library;
CREATE DATABASE Library;
USE Library;

# Creating tables
# User table
CREATE TABLE User_ (
    UserID          INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    FirstName		VARCHAR(255) NOT NULL,
    LastName		VARCHAR(255) NOT NULL,
    UserStatus		ENUM('Active', 'Terminated', 'Blocked') NOT NULL,

    PRIMARY KEY(UserID)
);

# Author table
CREATE TABLE Author (
    AuthorID		INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    AuthorName		VARCHAR(255) NOT NULL,
    

    PRIMARY KEY(AuthorID)
);

# Publisher table
CREATE TABLE Publisher (
    PublisherID		INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    PublisherName	VARCHAR(255) NOT NULL,
    Country 		VARCHAR(255),

    PRIMARY KEY(PublisherID)
);

# Book table
CREATE TABLE Book (
    BookID		INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    Title		VARCHAR(300) NOT NULL,
    InStock       INTEGER NOT NULL,
    PublicationYear        INTEGER,
    PublisherID		INTEGER,

    PRIMARY KEY(BookID),
    FOREIGN KEY(PublisherID) REFERENCES Publisher(PublisherID) ON DELETE CASCADE
);

# Fines table
CREATE TABLE Fine (
    FineID		INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    Amount		DECIMAL(8, 2) NOT NULL,
    UserID		INTEGER NOT NULL,
    PaymentStatus	ENUM('PAID', 'NOT PAID') NOT NULL,	# Can be PAID or NOT PAID

    PRIMARY KEY(FineID),
    FOREIGN KEY(UserID) REFERENCES User_(UserID) ON DELETE CASCADE
);

# Writes table
CREATE TABLE Writes (
    AuthorID	        INT NOT NULL,
    BookID		INT NOT NULL,

    PRIMARY KEY(AuthorID, BookID),
    FOREIGN KEY(AuthorID) REFERENCES Author(AuthorID) ON DELETE CASCADE,
    FOREIGN KEY(BookID) REFERENCES Book(BookID) ON DELETE CASCADE
);



