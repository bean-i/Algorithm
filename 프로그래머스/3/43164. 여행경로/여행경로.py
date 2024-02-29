def dfs(answer, tickets, visited, current, cnt):
    if cnt == len(tickets):
        return True
    for i in range(len(tickets)):
        a, b = tickets[i]
        if not visited[i] and a == current:
            visited[i] = 1
            answer.append(b)
            if dfs(answer, tickets, visited, b, cnt+1):
                return True
            visited[i] = 0
            answer.pop()
    return False

            

def solution(tickets):
    answer = ["ICN"]
    tickets.sort()
    visited = [0] * len(tickets)
    dfs(answer, tickets, visited, "ICN", 0)

    return answer