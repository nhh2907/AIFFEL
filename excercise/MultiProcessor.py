import multiprocessing
import time

num_list = ['p1', 'p2', 'p3', 'p4']
start = time.time()  # 시작시간

def count(name):
    time.sleep(4)  # 해당 시간(초)동안 지연/대기
    print("finish:"+name+"\n")

if  __name__ == '__main__':
    pool = multiprocessing.Pool(processes = 2)  # 병렬 처리 시, 2개의 프로세스를 사용하도록 합니다.
                                                # CPU 코어의 개수만큼 입력해 주면 최대의 효과를 볼 수 있습니다
    pool.map(count, num_list)  # 병렬화를 시키는 함수로, count 함수에 num_list의 원소들을 하나씩 넣어 놓습니다.
                                # 여기서 num_list의 원소는 4개이므로 4개의 count 함수에 각각 하나씩 원소가 들어가게 됩니다.
    pool.close()  # pool 오브젝트를 닫기
    pool.join()  # 멀티프로세서가 완료될 때까지 대기

print("time :", time.time() - start)  # 시작 시간과 끝나는 시간의 차이 = 연산 처리 시간
