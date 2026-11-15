def bo_mot_mau(D, kc):
    so_dung = 0
    danh_sach_sai = []
    tong_so = len(D)
    
    for i in range(tong_so):
        best_dist = float('inf')
        best_label = ""
        for j in range(tong_so):
            if i == j: 
                continue # Bo qua chinh no
            
            dist = kc(D[i]['x'], D[j]['x'])
            if dist < best_dist:
                best_dist = dist
                best_label = D[j]['y']
                
        if best_label == D[i]['y']:
            so_dung += 1
        else:
            danh_sach_sai.append(i + 1) # Danh so tu 1 cho de doc
            
    return so_dung, tong_so, danh_sach_sai

def main():
    pass

if __name__ == '__main__':
    main()
