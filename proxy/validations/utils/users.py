ALUNO = "aluno"
PROFESSOR = "professor"
GESTOR = "gestor"
ESCOLA = "escola"


def is_user(user, _type):
    if hasattr(user, _type):
        return True
    return False
