def report_long_words(words):
  non_hyphened = [word for word in words if '-' not in word]
  longer_than_10 = [word for word in non_hyphened if len(word) > 10]
  shorten_to_15 = [word[:15] + '...' if len(word) > 15 else word for word in longer_than_10]
  return shorten_to_15

print(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]))

