from faker import Factory
import pytest

from business_rules.services import word_count

fake = Factory.create()

@pytest.mark.asyncio
@pytest.mark.parametrize(
    'words',
    [3,
    300,
    3000]
)
async def test_correct_count_of_words_common(words):
    """
    Test CORRECT COUNT OF WORDS - COMMON PHRASES
    
    This test returns a count of words from a common text
    
    input: words count

    """
    text = fake.sentence(nb_words=words, variable_nb_words=False)
    received_count = await word_count(text=text)
    assert words == received_count
    
@pytest.mark.asyncio
async def test_correct_count_of_words_corner_case():
    """
    test CORRECT COUNT OF WORDS CORNER CASE
    
    This test covers the folloing corner case:
    
    007 is an amazing book series
    Real count: 6 words
    
    """
    text = '007 is an amazing book series'
    received_count = await word_count(text=text)
    assert 6 == received_count