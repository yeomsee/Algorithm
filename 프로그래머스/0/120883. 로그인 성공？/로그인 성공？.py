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