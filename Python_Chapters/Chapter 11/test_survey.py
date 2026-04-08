#The code tests if the AnonymousSurvey class properly stores a single response by creating a survey, 
# storing the response 'English', and then asserting that 'English' is included in the list of responses.

# from survey import AnonymousSurvey

# def test_store_single_response():
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)   # 1. Create an instance of the survey.
#     language_survey.store_response('English')     # 2. Store a response ('English').
#     assert 'English' in language_survey.responses # 3. Check if 'English' is stored in the responses.

import pytest
from survey import AnonymousSurvey

# Define a fixture to create a survey that will be used in multiple test functions
@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)  # Create an instance of the survey
    return language_survey  # Return the survey instance

# Test that a single response is stored properly
def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')      # Store the response 'English'
    assert 'English' in language_survey.responses  # Assert that 'English' is in the responses

# Test that three individual responses are stored properly
def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']    # List of responses to store
    for response in responses:
        language_survey.store_response(response)      # Store each response
    for response in responses:
        assert response in language_survey.responses  # Assert each response is in the stored responses
