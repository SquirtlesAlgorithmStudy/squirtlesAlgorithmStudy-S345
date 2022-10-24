def solution(genres, plays):
    answer = []
    # key 장르 value 고유번호
    genre_list = {}
    for idx, genre in enumerate(genres):
        if (genre_list.get(genre) == None):
            genre_list[genre] = [idx]
            continue
        genre_list[genre].append(idx)
    # step 1. 각 value의 합계를 구하고 내림차순으로 정렬, key값(장르)들만 뽑아 리스트를 만들어준다.
    step1_genre_list = {}
    for key, vals in genre_list.items():
        tmp = 0
        for val in vals:
            tmp += plays[val]
        if (step1_genre_list.get(key) == None):
            step1_genre_list[key] = tmp

    # value 기준(item[1]) sort
    step1_genre_list = dict(sorted(step1_genre_list.items(), key=lambda item: item[1], reverse=True))
    step1_result = list(step1_genre_list.keys())
    # step2
    for genre, values in genre_list.items():
        # sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
        genre_list[genre] = sorted(values, key=lambda value: plays[value], reverse=True)

    # step3
    for genre in step1_result:
        answer.append(genre_list[genre][:2])

    answer = sum(answer, [])

    return answer