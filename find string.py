string = input().strip()
sub_string = input().strip()
def count_substring(string, sub_string):
    stringl =len(string)
    subl = len(sub_string)
    count = 0
    for i in range(0, stringl):
        temp = string[i: i+subl]
        if(temp==sub_string):
            count = count+1
    return count
count = count_substring(string, sub_string)
print(count)
