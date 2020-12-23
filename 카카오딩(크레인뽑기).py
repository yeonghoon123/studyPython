def answer(board, moves):
    get = []
    answer = 0
    for cnt in range(0, len(moves)):
        for j in range(0, len(board)):
            if board[j][moves[cnt]-1] != 0:
                get.append(board[j][moves[cnt]-1])
                board[j][moves[cnt]-1] = 0
                print(get)
                if len(get) > 1:
                    for i in range(0, len(get)-1):
                        if get[i] == get[i+1]:
                            del get[i]
                            answer += 1
                            del get[i]
                            answer += 1
                            break
                break

    print(answer)


answer([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
