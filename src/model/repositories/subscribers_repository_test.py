from .subscribers_repository import SubscribersRepository


def test_insert():
    subscriber_info = {
        "name": "meuNome222",
        "email": "email22@email.com",
        "evento_id": 2
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)


def test_select_subscriber():
    email = "email@email.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)
