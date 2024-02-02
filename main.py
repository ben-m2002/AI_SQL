from openai import OpenAI
import config

OpenAI.api_key = config.OPENAI_KEY

conversation_history = """
    User : In this chat, you are generating sql request from language
    User : Here is my database schema
    User : Create Table Organizations (
            OrganizationID Int AUTO_INCREMENT,
            Name Varchar(100) NOT NULL,
            Location VARCHAR(255),
            ContactInfo Varchar(255),
            PRIMARY KEY (OrganizationID)
        )
        
        Create Table Teams (
            TeamID Int AUTO_INCREMENT,
            Name Varchar(100) NOT NULL,
            OrganizationID Int,
            Coach Varchar(100) Not NULL,
            NumPlayers INT,
            Wins INT,
            PRIMARY KEY (TeamID),
            FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID)
        )
        
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
        )
"""

questions = [
    "Get the team with the most wins"
]


def get_response(user_input):
    global conversation_history
    conversation_history += f"\nUser : {user_input}\n"
    try:
        response = OpenAI.completions.create(
            model="gpt-4",
            prompt=conversation_history,
            max_tokens=150,
            temperature=0.4,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(e)
        return None

