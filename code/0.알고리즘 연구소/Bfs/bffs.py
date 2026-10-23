from collections import deque
sm,em = '700134652','123456700'
aro = {0:[3, 1],1:[4, 0, 2],2:[5, 1],3:[0, 6, 4],4:[1, 7, 3, 5],5:[2, 8, 4],6:[3, 7],7:[4, 6, 8],8:[5, 7]}
ze = {}
for i in range(len(sm)):
    if sm[i] == '0':
        ze[sm] = i


    
def main():
    q = deque([sm])
    while q:
        cur = q.popleft()
        if cur == em:
            break
        
        
