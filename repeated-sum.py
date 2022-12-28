x = '666812999'
res = 0
final_res = ''
result = ''
final_string_found = False
start_index = 0
end_index = 1
i = 0
while not final_string_found:
    if end_index == len(x)-1:
        break
    if x[i] == x[end_index]:
        end_index += 1
        i += 1
        continue
    for j in range(start_index, end_index):
        res+=x[j]
# for i in range(len(x)):
#     if i == len(x)-1:
#         break
#     if x[i] == x[i+1]:
#         res += int(x[i])
#         x= x.replace(x[i],'',1)
#         final_res = str(res)
#     else:
#         final_res += x[i]
#         res=0

print(final_res)
        
    