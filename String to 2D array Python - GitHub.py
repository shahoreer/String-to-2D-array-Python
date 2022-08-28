data="abc.mp4,1,2,3,abc2.mp4,4,5,6,7,abc3.mp4,8,9,10,11,12,13,14"
split_by=","
new_arry_by=".mp4"

data=data.split(split_by)
fxd_data=[]

finished=0
for idx, target in enumerate(data):
    if (target.__contains__(new_arry_by) or (idx==len(data)-1)) and not idx==0:
        fxd_data.insert (len(fxd_data),data[finished:idx])
        if idx==len(data)-1:
            fxd_data[len(fxd_data)-1].append(target)
        finished=idx

print(fxd_data)