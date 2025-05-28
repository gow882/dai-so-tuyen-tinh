danhsach1 = [1. , 3.]
danhsach2 = [5. , 7.]
danhsach = danhsach1 + danhsach2

danhsach_gapdoi = 2 * danhsach
print(danhsach*2)

#print(danhsach / 2)  #khong chia duoc


mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]

anh_xa = zip(thu_tu, mon_hoc, diem_so)


tap_hop = set(anh_xa)
print("Tập hợp:", tap_hop)


anh_xa = zip(thu_tu, mon_hoc, diem_so)

lay_TT, lay_monhoc , lay_diem = zip(*anh_xa)
print("Môn học:", lay_monhoc)
