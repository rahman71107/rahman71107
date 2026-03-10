Author : Abdul Hameed
Nested Lists

if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        res.append([name, score])
        
    unique_student = sorted(list(set([x[1] for x in res])))
    seccond_lowest = unique_student[1]
    final_names = sorted([stc[0] for stc in res if stc[1] == seccond_lowest])
    
    for fn in final_names:
        print(fn)
