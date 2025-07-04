from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_deposit_and_get_balance():
    uuid = "test-wallet-1"
    res = client.post(f"/api/v1/wallets/{uuid}/operation", json={"operation_type": "DEPOSIT", "amount": 1000})
    assert res.status_code == 200
    assert res.json()["balance"] == 1000

    res = client.get(f"/api/v1/wallets/{uuid}")
    assert res.status_code == 200
    assert res.json()["balance"] == 1000

def test_withdraw_success():
    uuid = "test-wallet-2"
    client.post(f"/api/v1/wallets/{uuid}/operation", json={"operation_type": "DEPOSIT", "amount": 500})
    res = client.post(f"/api/v1/wallets/{uuid}/operation", json={"operation_type": "WITHDRAW", "amount": 200})
    assert res.status_code == 200
    assert res.json()["balance"] == 300

def test_withdraw_fail():
    uuid = "test-wallet-3"
    res = client.post(f"/api/v1/wallets/{uuid}/operation", json={"operation_type": "WITHDRAW", "amount": 100})
    assert res.status_code == 400
    assert "Insufficient funds" in res.text
