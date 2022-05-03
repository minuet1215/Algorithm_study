import re

def solution(new_id):
    l_1 = new_id.lower()
    l_2 = re.sub('[^a-z0-9-_.]', '', l_1)
    l_3 = re.sub('[..]+', '.', l_2)
    l_4 = re.sub('^[.]', '', l_3)
    l_5 = 'a' if not l_4 else l_4

    l_6 = l_5[:15] if len(l_5) > 15 else l_5
    l_6 = re.sub('[.]$', '', l_6)

    # l_7
    l_7 = l_6
    if len(l_7) <= 2:
        last = l_7[-1]
        while len(l_7) < 3:
            l_7 += last
    # print(l_7)

    answer = l_7

    return answer
