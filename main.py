import easygui
from mgz.model import parse_match

with open(easygui.fileopenbox(msg='Select aoe2 record file'), 'rb') as h:
    match = parse_match(h)
    result = []
    for i in match.chat:
        result.append('['+str(i.timestamp)[:-10]+']'+'('+str(i.audience)+')' + str(i)[16:]+'\n')
    easygui.msgbox(title='AOE2 Chat Parser', msg=''.join(result))


