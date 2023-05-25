# Merge the Tools

def merge_the_tools(string, k):
    substrings = [list(string[i:i+k:]) for i in range(0, len(string), k)]
    output = []
    for substring in substrings:
        reverse = substring[::-1]
        for i in range(len(substring)):
            if reverse.count(substring[i]) > 1:
                reverse.remove(substring[i])
        output.append(''.join(reverse[::-1]))
    print('\n'.join(output))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)