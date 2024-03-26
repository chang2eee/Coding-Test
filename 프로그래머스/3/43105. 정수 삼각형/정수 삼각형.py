def solution(triangle):
    # 삼각형의 높이
    height = len(triangle)
    
    # 높이가 1일 때는 그 값이 정답
    if height == 1:
        return triangle[0][0]
    
    # 삼각형의 아래에서 두 번째 줄부터 시작하여
    # 각 위치까지의 최대값을 계산하여 저장
    for i in range(1, height):
        for j in range(len(triangle[i])):
            # 맨 왼쪽 값일 때는 위에서 오는 경로가 없음
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            # 맨 오른쪽 값일 때는 위에서 오는 경로가 없음
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            # 그 외의 경우에는 위에서 오는 두 경로 중 큰 값을 선택하여 더함
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    
    # 마지막 줄의 값 중 최대값이 최종 결과
    return max(triangle[-1])