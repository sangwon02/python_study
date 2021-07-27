import time, random

def bubbleSort(A):
    count=0#몇번 횟수 실행이 되었는지 카운트하는 변수를 정해준다.
    for i in range(1, len(A)): #리스트의 크기만큼 반복시킴
        for j in range(0, len(A)-1): #전부 정렬아 안되면 정렬
            if A[j] > A[j+1]:#현재 값이 다음 값보다 크면 실행시킴
                A[j+1], A[j] = A[j], A[j+1] #두 위치 바꾸기
                count+=1#한번 실행 할 때 마다 카운트
    return count#카운트를 값으로 보내준다.
    
def insertionSort(A):
    count=0
    for i in range(1, len(A)):
        for j in range(i, 0, -1):  #j이 값이 줄어 줄면서 위치를 찾을 때까지 반복
            if A[j] > A[j-1]:
                A[j], A[j-1] = A[j-1], A[j] 
                count+=1
            else : break # 계속 반복을 위해 멈춤
    return count

def selectionSort(A):
    count=0
    for i in range(len(A)-1):#리스트의 크기의 -1만큼 반복
        for j in range(i+1, len(A)): #행당 값의 +1부터, 리스트 크기만큼 반복
            if A[i] < A[j]: #현재 값이 비교 값보다 크다면 실행
                A[i] , A[j]  = A[j], A[i]
                count+=1
    return count

def quickSort(A, start, end):#재귀함수 사용
    global quick_cnt #글로벌 변수 사용
    quick_cnt=0
    if start < end:#시작 값이 끝의 값보다 클경우 실행
        left = start
        pivot = A[end] 
        for i in range(start, end):#시작 값부터 끝 값까지 반복
            if A[i] < pivot:#현재 값이 끝 값 보다 작을 경우 실행
                A[i], A[left] = A[left], A[i]
                left += 1
                quick_cnt += 1
        A[left] , A[end] = A[end], A[left]
        quickSort(A, start, left-1)#재귀 호출
        quickSort(A, left+1, end)#재귀 호출
        return quick_cnt


def randomNumber(a,b):#랜덤한 리스트 생성
    randomlist = []
    for i in range(0,a):
        n = random.randint(1,b)
        randomlist.append(n)
    return randomlist

randomList = randomNumber(1000,1000)
#randomList = [158, 20, 119, 39, 66, 41, 124, 151, 168, 154]
randomList1 = randomList[:]         # 리스트 복사하는 방법1
randomList2 = list(randomList)      # 리스트 복사하는 방법2
randomList3 = randomList.copy()     # 리스트 복사하는 방법3
randomList4 = randomList.copy()     # 리스트는 할당으로 복사하면 주소를 전달한다. 
randomList5 = randomList.copy()     

print("원래 배열 (정렬 전)    :", randomList1)
start1 = time.time()
numOfIteration1 = selectionSort(randomList1)
print(time.time()-start1,"초만에", numOfIteration1, "번만에 선택 정렬로 내림차순으로 정렬하였습니다.")
print("선택 정렬로 정렬된 배열:", randomList1, "\n")

print("원래 배열 (정렬 전)    :", randomList2)
start2 = time.time()
numOfIteration2 = insertionSort(randomList2)
print(time.time()-start2,"초만에", numOfIteration2, "번만에 삽입 정렬로 내림차순으로 정렬하였습니다.")
print("삽입 정렬로 정렬된 배열:", randomList2, "\n")

print("원래 배열 (정렬 전)    :", randomList3)
start3 = time.time()
numOfIteration3 = bubbleSort(randomList3)
print(time.time()-start3,"초만에", numOfIteration3, "번만에 버블 정렬로 오름차순으로 정렬하였습니다.")
print("버블 정렬로 정렬된 배열:", randomList3, "\n")

print("원래 배열 (정렬 전)    :", randomList4)
start4 = time.time()
numOfIteration4 = bubbleSort(randomList4)
quickSort(randomList4, 0, len(randomList4)-1)
print(time.time()-start4,"초만에", numOfIteration4, "번만에 퀵 정렬로 오름차순으로 정렬하였습니다.")
print("퀵 정렬로 정렬된 배열:", randomList4, "\n")

start5 = time.time()
randomList5.sort()
print("파이썬 내장함수로는 ", time.time()-start4,"초만에 정렬하였습니다.")