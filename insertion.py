
def insertion_sorting(original_list):
    for i in range(1, len(original_list)):
        key = original_list[i]
        for j in range(1, i+1):
            com = original_list[i-j]
            if(com<key) : break
            original_list[i-j+1] = com
            original_list[i-j] = key
    return original_list

def main():
    unsorted_string = input("입력하세요(숫자의 구분은 띄어쓰기) : ")
    unsorted_list = unsorted_string.split(' ')
    print(unsorted_list)
    print("정렬된 리스트 :" ,insertion_sorting(unsorted_list))

main()
