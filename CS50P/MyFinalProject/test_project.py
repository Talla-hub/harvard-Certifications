import pytest
from project import app  # Import the Flask app from your main file

# Set up the Flask testing client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the root route (index)
def test_index(client):
    # Simulate a GET request to the index route
    response = client.get('/')
    assert response.status_code == 200
    assert b'Rock-Paper-Scissors Game' in response.data
# Test the reset functionality
def test_reset_scores(client):
    # First, simulate a game play to change the score
    client.post('/', data={'move': 'rock'})
    response = client.post('/reset', follow_redirects=True)  # Reset scores
    assert response.status_code == 200
    assert b'Wins: 0' in response.data  # Make sure the scores are reset
    assert b'Loses: 0' in response.data
    assert b'Ties: 0' in response.data

# Test invalid move (not rock, paper, or scissors)
def test_invalid_move(client):
    response = client.post('/', data={'move': 'invalid'})
    assert response.status_code == 200
    assert b'Invalid move' not in response.data  # Assuming you handle invalid moves gracefully
