# Author:Tom_Steve
# Date:2021-07-17


def countStudentClass(studnetScoreList):
    if len(studnetScoreList) < 1:
        print("Please add at least 1 item into the list")
        return 0

    nerdCount_list = [0] * 7  # initialize the output list

    # Please write your own program here
    for studentScore in studnetScoreList:  # 单独对task1-3解决的部分
        if 0 <= studentScore <= 1:
            nerdCount_list[0] = nerdCount_list[0] + 1
        elif 1 < studentScore <= 10:
            nerdCount_list[1] = nerdCount_list[1] + 1
        elif 10 < studentScore <= 100:
            nerdCount_list[2] = nerdCount_list[2] + 1
        elif 100 < studentScore <= 500:
            nerdCount_list[3] = nerdCount_list[3] + 1
        elif 500 < studentScore <= 1000:
            nerdCount_list[4] = nerdCount_list[4] + 1
        elif 1000 < studentScore <= 2000:
            nerdCount_list[5] = nerdCount_list[5] + 1
        elif studentScore > 2000:
            nerdCount_list[6] = nerdCount_list[6] + 1
    print(nerdCount_list[0:6])
    return nerdCount_list


if __name__ == '__main__':
    # test cases
    # studnetScoreList = []
    studnetScoreList = [23, 76, 1300, 600]  # output should be [0, 0, 2, 0, 1, 1, 0]

    print(countStudentClass(studnetScoreList))
