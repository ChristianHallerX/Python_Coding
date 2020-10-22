def swap(arr,i,j):
    '''Reverses order of two speific elements in an array'''
    arr[i],arr[j] = arr[j],arr[i]

def zigzag(arr):
    '''Takes an array and sorts it in zig-zag fashion - i.e., higher, lower, higher, lower'''
    srt = sorted(arr) # after sorting, the first list item is low
    print('sorted: ', srt)
    left = 1 # starting list index is second list item

    while left < len(srt)-1:    # execute if left item is low (should be higher)
        swap(srt, left, left+1) #pairwise swap
        left = left + 2 #go to next pair
    print('zigzag: ', srt)

print('input:   [5,3,7,2,8,33,55,2,22,11]')
zigzag([5,3,7,2,8,33,55,2,22,11])
