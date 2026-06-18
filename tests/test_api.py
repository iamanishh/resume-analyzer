from urllib import response

from fastapi.testclient import TestClient
from app import app
from io import BytesIO

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Resume analyzer API is running"
    }

def test_upload_non_pdf():

    response = client.post(
        "/analyze",
        files={
            "file": (
                "image.jpg",
                BytesIO(b"fake image"),
                "image/jpeg"
            )
        }
    )

    assert response.status_code == 415
    assert response.json()["detail"] == "Only PDF files are allowed."
