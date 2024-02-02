Create Database FootballLeague;
use FootballLeague;

Create Table Organizations (
	OrganizationID Int AUTO_INCREMENT,
    Name Varchar(100) NOT NULL,
    Location VARCHAR(255),
    ContactInfo Varchar(255),
    PRIMARY KEY (OrganizationID)
);

Create Table Teams (
    TeamID Int AUTO_INCREMENT,
    Name Varchar(100) NOT NULL,
    OrganizationID Int,
    Coach Varchar(100) Not NULL,
    NumPlayers INT,
    Wins INT,
    PRIMARY KEY (TeamID),
    FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID)
);

Create Table Coaches (
    CoachID Int AUTO_INCREMENT,
    Name Varchar(100) NOT NULL,
    TeamID Int UNIQUE NOT NULL,
    DateOfBirth Date,
    CoachingRating Int,
    PRIMARY KEY (CoachID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);

Create Table Players (
    PlayerID Int AUTO_INCREMENT,
    Name Varchar(100) NOT NULL,
    TeamID Int Not NULL ,
    DateOfBirth Date,
    Position Varchar(100),
    JerseyNumber Int,
    JoinDate Date,
    PlayerRating Int,
    PlayerMorale VARCHAR(20), # Good, Bad, Neutral
    PRIMARY KEY (PlayerID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);