import os

# The h-index is a metric that measures both the productivity and citation impact 
# of a researcher. Specifically, a researcher's h-index is the largerst number h such that 
# the research has published h ppapers that have each been cited at least h times
# for example, if carl has published papers A,B,C,D,E,F,G,H,I, which have been
# cited 1,4,1,4,2,1,3,5,6 times, respectively, then his h-index is 4
# (corresponding to papers B,D,H,I)

# design an algorithm that determinse a researcher's h-index

# time cost O(n^2)
def h_index_1(citations: list):

    print("citations: {}".format(citations))

    h_index = 0
    for i in range(len(citations)):
        print("Round {}".format(i))
        for c in citations:
            if c >= i: 
                h_index += 1
    
        if h_index < i:
            print(f"H index {h_index} is less than count {i}")
            break
        else:
            # reset index
            h_index = 0
    
    return i-1


if __name__ == '__main__':

    s = input()
    cit = [int(c) for c in s.split(',')]

    result = h_index_1(cit)
    print(f"H-index is {result}")


