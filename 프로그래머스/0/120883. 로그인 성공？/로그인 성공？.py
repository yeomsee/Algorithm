# My Code
def solution(id_pw, dbs):
    for db in dbs:
        user_id, user_pd = db
        if user_id == id_pw[0]:
            if user_pd == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

# Best Code
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
