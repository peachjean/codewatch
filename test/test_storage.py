import codewatch.storage as cws

def test_load():
  print(cws.load_data("blah", "sha"))
  for line in cws.load_data("blah", "sha"):
    print(line)
