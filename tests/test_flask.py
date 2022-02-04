import pytest
from app import app
from datetime import datetime


@pytest.fixture()
def client():
    """
    リクエストを送るテスト用クライアントを作成する。
    @pytest.fixtureにより、作成したクライアントは各テストの引数に渡される
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_all_user(client):
    """全レコードの取得テスト"""
    rv = client.get('/user', follow_redirects=True)
    response_body = rv.get_json()

    # StatusCodeが200か？
    assert rv.status_code == 200

    # 返ってきた値が配列か？
    assert type(response_body) == list

    for x in response_body:
        # 返ってきたBodyの中身が正しいか？
        assert type(x['id']) == int  # autoincrement
        assert type(x['username']) == str
        assert type(x['email']) == str
        assert datetime.strptime(x['birth_day'], '%Y-%m-%d')  # 正しい日付フォーマットかどうか
        assert type(x['height']) == float
        assert type(x['memo']) == str
        assert datetime.strptime(x['created_at'], '%Y-%m-%dT%H:%M:%S')  # 正しい日付フォーマットかどうか
        assert datetime.strptime(x['updated_at'], '%Y-%m-%dT%H:%M:%S')  # 正しい日付フォーマットかどうか
        assert type(x['is_active']) == bool


def test_insert_user(client):
    """レコードの１件追加テスト"""
    request_body = {
        'username': 'あいうえおアイウエオｱｲｳｴｵaiueoAIUEOａｉｕｅｏＡＩＵＥＯ㈱☺🐰',
        'email': 'あいうえおアイウエオｱｲｳｴｵaiueoAIUEOａｉｕｅｏＡＩＵＥＯ㈱☺🐰',
        'birth_day': '2022-02-03',
        'height': 999.999,
        'memo': 'あいうえおアイウエオｱｲｳｴｵaiueoAIUEOａｉｕｅｏＡＩＵＥＯ㈱☺🐰',
        'is_active': True
    }
    rv = client.post('/user', follow_redirects=True, json=request_body)
    response_body = rv.get_json()

    # StatusCodeが200か？
    assert rv.status_code == 200

    # 返ってきたBodyの中身が正しいか？
    assert type(response_body['id']) == int  # autoincrement
    assert response_body['username'] == request_body['username']
    assert response_body['email'] == request_body['email']
    assert response_body['birth_day'] == request_body['birth_day']
    assert response_body['height'] == request_body['height']
    assert response_body['memo'] == request_body['memo']
    assert datetime.strptime(response_body['created_at'], '%Y-%m-%dT%H:%M:%S')  # 正しい日付フォーマットかどうか
    assert datetime.strptime(response_body['updated_at'], '%Y-%m-%dT%H:%M:%S')  # 正しい日付フォーマットかどうか
    assert response_body['is_active'] == request_body['is_active']


def test_get_user(client):
    """IDを指定してレコードの１件取得テスト"""
    # todo: 実装
    pass


def test_update_user(client):
    """IDを指定してレコードの１件更新テスト"""
    # todo: 実装
    pass


def test_delete_user(client):
    """IDを指定してレコードの１件削除テスト"""
    # todo: 実装
    pass
