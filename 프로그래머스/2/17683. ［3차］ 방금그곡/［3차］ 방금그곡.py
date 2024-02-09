def replacement(data):
    replacements = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for old, new in replacements.items():
        data = data.replace(old, new)
    return data

def solution(m, musicinfos):
    answer = '(None)'
    m = replacement(m)

    max_time = 0
    for music in musicinfos:
        start, end, name, info = music.split(",")
        info = replacement(info)

        play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        value = (info * play_time)[:play_time]

        if m in value and play_time > max_time:
            max_time = play_time
            answer = name

    return answer
