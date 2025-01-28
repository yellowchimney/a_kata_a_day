from src.caesars_cypher import counter_intelligence

def test_returns_an_empty_string():
    assert counter_intelligence('') == ''

def test_returns_decoded_character():
    assert counter_intelligence('Y') == 'X'

def test_returns_multiple_decoded_characters():
    assert counter_intelligence('NKRRU YCKKZNKGXZ D') == 'HELLO SWEETHEART X'
    assert counter_intelligence('CJR DN TJPM NKMDIO KMJBMZNNDIB? S') == 'HOW IS YOUR SPRINT PROGRESSING? X'

def test_returns_decrypted_message_for_mixed_case_letters():
    assert counter_intelligence('NkRrU yCKKZnKGXz D') == 'HELLO SWEETHEART X'
    assert counter_intelligence('ngbk g toik jge :) d') == 'HAVE A NICE DAY :) X'