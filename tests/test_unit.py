import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_process_input():
    from app import process_input
    important_words = process_input("The quick brown fox jumps over the lazy dog.")
    assert important_words == ['fox', 'dog']

def test_download_images():
    from app import download_images

    # Assuming you have a valid query and API keys for testing
    query = 'test'
    use_pixabay = True
    num_images = 1

    # Ensure that there are no exceptions raised
    download_images(query, num_images, use_pixabay)

# Add more tests as needed

if __name__ == '__main__':
    pytest.main()

