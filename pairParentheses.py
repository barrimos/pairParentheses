def checkParenthese(parenthese: str, sort: bool = False):
  OPENTAG: list[str] = ['[', 0, '{', 0, '(', 0, '<', 0]
  CLOSETAG: list[str] = [']', 0, '}', 0, ')', 0, '>', 0]
  length: int = len(parenthese)
  result: str = ''
  i = 0

  def findIndex(i):
    idx: int = OPENTAG.index(parenthese[i]) if parenthese[i] in OPENTAG else CLOSETAG.index(parenthese[i])
    return idx

  if sort:
    list_p = list(parenthese)
    for i in range(len(list_p)):
      idx: int = findIndex(i)
      if parenthese[i] in OPENTAG:
        OPENTAG[idx + 1] += 1
      else:
        CLOSETAG[idx + 1] += 1

    for i in range(1, 8, 2):
      diff: int = abs(OPENTAG[i] - CLOSETAG[i])
      for j in range(diff):
        if OPENTAG[i] < CLOSETAG[i]:
          list_p.append(OPENTAG[i - 1])
        else:
          list_p.append(CLOSETAG[i - 1])
    
    list_p.sort()
    new_p = ''.join(list_p)
    
    return new_p


  while length > 0:
    # find index in OPENTAG or CLOSETAG
    idx: int = findIndex(i)
    next: str = '' if i >= len(parenthese) - 1 else parenthese[i + 1]

    if parenthese[i] + next != OPENTAG[idx] + CLOSETAG[idx]:
      i += 1
    else:
      i += 2
      length -= 1
    result += OPENTAG[idx] + CLOSETAG[idx]

    length -= 1

  return result

print(checkParenthese(')()((', True)) # ()()()() || ((()))