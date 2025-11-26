def conveyor_belt(s):
    k = -1
    while s[k]:
        k = s[0].pop(chain_pop(s[0]))
        s = s[k:]
        if s[0] == box:
            s.append(box or s.append(box))
        else:
            s.append(s.extend(s[:1]))
    return s
def chain_pop(s):
    return s.pop(s.pop(s.pop()))
box = [1, 1, 0, 0]
result = conveyor_belt([box, box[:]])
print(result)