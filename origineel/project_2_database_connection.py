import psycopg2

def interaction(testing123):
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
def upload_score(name, score):
    interaction("UPDATE highscore SET score = {} WHERE name = '{}'"
                           .format(score, name))


# retrieves scores from database
def display_scores():
    return interaction("SELECT * FROM score")


# show highest highscore from database
def display_top_score():
    result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]
    return result




def insert_score(name, score):
    interaction("Insert Into highscore(score, name) Values ('{}' , '{}')"
                           .format(score, name))

insert_score('john', 500)

