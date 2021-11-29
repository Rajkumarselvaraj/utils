
def getwindow(arr,ws):
    i=0
    while i+ws<=len(arr):
        yield arr[i:i+ws]
        i+=1
list_avg = lambda inp_list:sum(inp_list)/len(inp_list)

if __name__ == '__main__':
    array=[1,2,3,4,5,6,7,8,9,10]
    window=4
    generated_list = getwindow(array,window)

    for x in generated_list:
        print(x, "-->",list_avg(x))