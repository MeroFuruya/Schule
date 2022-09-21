
array = '1,v,2,a,3,l,4,u,5,e'.split(',')

for i in range(int(len(array)/2)):
    print(f'index: {array[i*2]} value: {array[i*2+1]}')
