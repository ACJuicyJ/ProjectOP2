import psycopg2
from functions import *


def interaction(testing123):
    print(testing123)
    # interactie opzetten dmv .cursor
    conn = psycopg2.connect(" dbname=project_2_highscore user=postgres password = 123456 ")
    cursor = conn.cursor()

    cursor.execute(testing123)
    conn.commit()

    result = None
    try:
        result = cursor.fetchall()
    except psycopg2.ProgrammingError:

        pass #als er geen data is om in te zetten

    cursor.close()
    conn.close()

    return result


# Uploads a score into the highscore table
def upload_score(score, name):
    interaction("UPDATE highscore SET score = {} WHERE name = '{}'"
                           .format(score, name))


# retrieves scores from database
def display_scores():
    return interaction("SELECT * FROM score")


# show highest highscore from database
def display_top_score():
    result = interaction("SELECT * FROM score ORDER BY score")[0][1]
    return result



def insert_score(name, score):
    interaction("Insert INTO highscore(score, name) Values ({} , '{}')"
                           .format(score, name))

#om de correcte database te maken voer de volgende sql syntax in
#create database project_2_highscore
# en dan
#create table highscore(
#    score integer,
#    name TEXT
#);
