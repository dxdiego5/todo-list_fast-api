from http import HTTPStatus


def test_read_root_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'App TO LIST'}


def test_create_user_retornar_usuario_criado(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Testuser',
            'email': 'test@test.com',
            'password': 'tTstpassword',
            'disabled': True,
        },
    )
    # validar status ccode correto
    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'username': 'Testuser',
        'email': 'test@test.com',
        'id': 1,
        'disabled': True,
    }


def test_read(client):
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {
                'username': 'Testuser',
                'email': 'test@test.com',
                'id': 1,
                'disabled': True,
            }
        ]
    }


def test_update_ser(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'UpdatedUser1',
            'email': 'UpdatedUser1@adad.com',
            'password': 'UpdatedPassword1',
            'disabled': False,
            'id': 1,  # id não deve ser enviado no update
        },
    )  # Act

    assert response.json() == {
        'username': 'UpdatedUser1',
        'email': 'UpdatedUser1@adad.com',
        'disabled': False,
        'id': 1,  # id não deve ser enviado no update
    }


def test_delete_user(client):
    response = client.delete('/users/1')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'User deleted successfully'}
