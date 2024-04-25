# Config parser for meinkraft.

def parseConfig(file):
  src = file.read().split("\n") + ["EOF"];
  pos = 0;

  values = {};

  while (src[pos] != "EOF"):
    if (src[pos] == ""):
      pos += 1;
    elif (src[pos][0] == "#"):
      pos += 1;
    elif (src[pos][0] == "$"):
      if ((src[pos][1:].split(" ")[1][0] == "\"") and (src[pos][1:].split(" ")[1][-1] == "\"")):
        values[src[pos][1:].split(" ")[0]] = src[pos][1:].split(" ")[1][1:-1];
      pos += 1;
    else:
      pos += 1;

  return values;

