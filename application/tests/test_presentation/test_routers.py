import pytest
from business_rules import services 
import mock
from fastapi import Form
@pytest.mark.asyncio
async def test_get_template(client):
    """
    test GET TEMPLATE
    This test guarantees the template returns
    """
    URL = '/'
    expected_status_code = 200
    expected_content_type = 'text/html'
    
    response = await client.get(URL)
    
    assert '<!doctype html>' in str(response.content)
    assert expected_status_code == response.status_code
    assert expected_content_type in response.headers['content-type']
    
@pytest.mark.asyncio
async def test_post_template_err_405(client):
    """
    test GET TEMPLATE
    This test guarantees that other methods like post for / is not allowed
    """
    URL = '/'
    
    response = await client.post(URL)
    expected_status_code = 405
    
    assert expected_status_code == response.status_code
    
    
@pytest.mark.asyncio
async def test_post_word_checker_function_not_called_422(client):
    """
    test POST WORD CHECKER - FUNCTION IS NOT CALLED
    This test guarantees that the API returns 200 when no FORM data is sent, with 0 as response
    """
    URL = '/word_counter'
    
    expected_status_code = 200
    expected_response = b'<span style="color: red;">Text is Required!</span>'
    async_mock = mock.AsyncMock(return_value=300)
    with mock.patch.object(services, 'word_count', async_mock) as mocked_count :
        response = await client.post(URL, json={'text':'any'})
        assert expected_status_code == response.status_code
        assert expected_response == response.content
        
    
@pytest.mark.asyncio
async def test_post_word_checker_function_called(client):
    """
    test POST WORD CHECKER - FUNCTION IS CALLED
    This test guarantees that the ~function reads the form data and calls the service
    """
    URL = '/word_counter'
    
    expected_status_code = 200
    async_mock = mock.AsyncMock(return_value=300)
    with mock.patch.object(services, 'word_count', async_mock) as mocked_count :
        response = await client.post(URL, data={'text':'any'}, headers={
            'content-type':'application/x-www-form-urlencoded'}
        )
        mocked_count.assert_called_once()
        assert expected_status_code == response.status_code