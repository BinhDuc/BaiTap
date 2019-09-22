import os,json

danhsachhanghoa = []
danhsachloaihanghoa = []
danhsachhoadon=[]

def load_loaihanghoa_luckhoidong():
  files = os.listdir("danhsach")
  if "loaihanghoa.csv" not in files:
     return

  with open('danhsach/loaihanghoa.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        #print("str_to_reads:", str_to_reads)
        if len(str_to_reads) > 1:
            loaihanghoa = {}
            loaihanghoa["id"] = str_to_reads[0]
            tenloai = str_to_reads[1]
            if tenloai.endswith('\n'):
                tenloai = tenloai[0:len(tenloai)-1]
            loaihanghoa["ten"] = tenloai
            danhsachloaihanghoa.append(loaihanghoa)
        line = f.readline()
  print("danhsachloaihanghoa:", danhsachloaihanghoa)

def load_hanghoa_luckhoidong():
  files = os.listdir("danhsach")
  if "hanghoa.csv" not in files:
     return

  with open('danhsach/hanghoa.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        if len(str_to_reads) > 1:
            hanghoa = {}
            hanghoa["id"] = str_to_reads[0]
            hanghoa["ten"] = str_to_reads[1]
            hanghoa["giaban"] = int(str_to_reads[2])
            hanghoa["loaihanghoa_id"] = str_to_reads[3]

            if hanghoa["loaihanghoa_id"].endswith('\n'):
                hanghoa["loaihanghoa_id"] = hanghoa["loaihanghoa_id"][0:len(hanghoa["loaihanghoa_id"])-1]
            danhsachhanghoa.append(hanghoa)
        line = f.readline()
  print("danhsachhanghoa:", danhsachhanghoa)

load_hanghoa_luckhoidong()

def tao_loaihanghoa():
  data = {}
  id = input("xin moi nhap id loai hang hoa:")
  tim_id_daco = xem_loaihanghoa(id)
  if tim_id_daco is not None:
     print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
     return

  data["id"] = id
  data["ten"] = input("xin moi nhap ten loai hang hoa:")
  danhsachloaihanghoa.append(data)
  str_to_save = data["id"] + "#" + data["ten"] + '\n'
  with open('danhsach/loaihanghoa.csv', 'a') as f:
            data = f.write(str_to_save)


def xem_loaihanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id loai hang hoa:")
  for loai in danhsachloaihanghoa:
    if loai["id"] == id:
      print("loai hang hoa: ", loai)
      return loai
def tao_hanghoa():
  data = {}
  id = input("xin moi nhap id hang hoa:")
  tim_id_daco = xem_hanghoa(id)
  if tim_id_daco is not None:
     print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
     return
  data["id"] = id
  data["ten"] = input("xin moi nhap ten hang hoa:")
  data["giaban"] = input("xin moi nhap gia ban:")
  loaihanghoa_id = input("xin moi nhap id loai hang hoa:")

  co_hienthi_danhsachloai = False
  tim_idloai_daco = xem_loaihanghoa(loaihanghoa_id)

  while tim_idloai_daco is None:
     print("Danh sach loai hang hoa:")
     for loaihanghoa in danhsachloaihanghoa:
        print(loaihanghoa["id"])
     loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
     tim_idloai_daco = xem_loaihanghoa(loaihanghoa_id)


  data["loaihanghoa_id"] = loaihanghoa_id
  danhsachhanghoa.append(data)
  str_to_save = data["id"] + "#" + data["ten"] + '#' + data["giaban"] + "#" +  data["loaihanghoa_id"] + '\n'
  with open('danhsach/hanghoa.csv', 'a') as f:
      data = f.write(str_to_save)
def KiemTraSoHoaDon(tenhoadon_cankt):
    danhsach_sohoadon=os.listdir('hoadon')
    if tenhoadon_cankt+'.json' in danhsach_sohoadon:
        print('so hoa don nay da ton tai')
        return False
    return True
def GhiFileHoaDon(thongtinhoadon,tenhoadon):
    with open('hoadon/hoadon'+str(tenhoadon)+'.json','w') as wfile:
        json.dump(thongtinhoadon,wfile)
def xem_hanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id hang hoa:")
  for hanghoa in danhsachhanghoa:
    if hanghoa["id"] == id:
      return hanghoa

def KiemTraid(tim_id):
    for timid in danhsachhanghoa:
        if tim_id==timid['id']:
            return True
    return False
hanghoaban = {}
load_loaihanghoa_luckhoidong()

def tao_hoadon():
    print("moi ban tao hoa don")
    hoadon={}
    while True:
        hoadon["sohoadon"] = input("nhap so hoa don:")
        if KiemTraSoHoaDon(hoadon['sohoadon'])==False:
                print('so hoa don nay da ton tai xin moi nhap so hoa don khac: ')
        else:break
    hoadon["ngayhoadon"]= input("nhap ngay hoa don :")
    hoadon["nguoimua"]= input("nhap nguoi mua hang :")
    hoadon["tongtientruocthue"] = 0
    hoadon["thue"] = 0.1
    hoadon["tongtien"] = 0
    hoadon["danhsachhanghoa"] = []

    nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
    while nhaphanghoa.upper() == 'Y':
        hanghoa = {}
        hanghoa["stt"] = input("nhap so thu tu: ")
        hanghoa["stt_x"]=str(hanghoa["stt"])
        for i in range(len(hanghoa["stt_x"]),7):
            hanghoa["stt_x"]= ' '+hanghoa["stt_x"]
        idhanghoa=input('nhap id hang hoa: ')
        if KiemTraid(idhanghoa)==False:
            print('khong tim thay id hang hoa ')
        else:
            for timid in danhsachhanghoa:
                if idhanghoa==timid['id']:break
            hanghoa['ten']=timid['ten']
            print("ten:",hanghoa['ten'])
            hanghoa["ten_x"]=hanghoa["ten"]
            for i in range(len(hanghoa["ten_x"]),16):
                hanghoa["ten_x"]=hanghoa["ten_x"]+ ' '
            hanghoa['dongia']=timid['giaban']
            print('don gia ; ',hanghoa['dongia'])
            hanghoa["dongia_x"]=str(hanghoa["dongia"])
            for i in range(len(hanghoa["dongia_x"]),13):
                hanghoa["dongia_x"]= ' '+hanghoa["dongia_x"]
        while True:
            soluong = input('nhap so luong( phai la so)')
            try:
                soluong=int(soluong)
                break
            except:
                print('nhap lai so luong')
        hanghoa['soluong']=soluong
        hanghoa["soluong_x"]=str(hanghoa["soluong"])
        for i in range(len(hanghoa["soluong_x"]),8):
            hanghoa["soluong_x"]= ' '+hanghoa["soluong_x"]
        hanghoa["thanhtien"] = hanghoa["soluong"] * hanghoa["dongia"]
        hanghoa["thanhtien_x"]=str(hanghoa["thanhtien"])
        for i in range(len(hanghoa["thanhtien_x"]),16):
            hanghoa["thanhtien_x"]=' '+hanghoa["thanhtien_x"]

        if hanghoa["ten"] in hanghoaban:
            hanghoaban[hanghoa["ten"]]["tongso"] = hanghoaban[hanghoa["ten"]]["tongso"] + hanghoa["soluong"]
            hanghoaban[hanghoa["ten"]]["doanhthu"] = hanghoaban[hanghoa["ten"]]["doanhthu"] + hanghoa["thanhtien"]
        else:
            hanghoaban[hanghoa["ten"]] = {
                "tongso": hanghoa["soluong"],
                "doanhthu": hanghoa["thanhtien"]
            }

        hoadon["danhsachhanghoa"].append(hanghoa)
        hoadon["tongtientruocthue"] = int(hoadon["tongtientruocthue"]) + int(hanghoa["thanhtien"])
        hoadon['tongtientt'] = str(hoadon["tongtientruocthue"])
        for i in range(len(hoadon['tongtientt']),16):
            hoadon['tongtientt'] = ' '+hoadon['tongtientt']

        nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")

    hoadon["tongtien"] = hoadon["tongtientruocthue"] + hoadon["tongtientruocthue"]*hoadon["thue"]
    hoadon['tongtienst']=str(hoadon["tongtien"])
    for i in range(len(hoadon['tongtienst']),16):
        hoadon['tongtienst']=' '+hoadon['tongtienst']
    danhsachhoadon.append(hoadon)
    print("Kiemtra:", danhsachhoadon)
    GhiFileHoaDon(hoadon,hoadon['sohoadon'])
def load_hoadon():
    danhsachtenhoadon=os.listdir('hoadon')
    for tenhoadon in danhsachtenhoadon:
        with open('hoadon/'+str(tenhoadon),'r') as l:
            f=json.load(l)
            danhsachhoadon.append(f)
    return danhsachhoadon
    print(danhsachhoadon)
load_hoadon()
def in_hoadon():
    timthay = False
    while timthay is False:
        sohoadon_canxem = input("nhap so hoa don can xem:")
        for hoadon in danhsachhoadon:
            if hoadon["sohoadon"] == sohoadon_canxem:
                timthay = True
                print("                          HOA DON MUA HANG                                  ")
                print("so hoa don:",hoadon["sohoadon"])
                print("ngay xuat:",hoadon["ngayhoadon"])
                print("ten khach hang:",hoadon["nguoimua"])
                print("_____________________________thong tin hoa don_______________________________")
                print("+----------+------------------+----------+---------------+------------------+")
                print("|   STT    |     hang hoa     | so luong |    don gia    |    thanh tien    |")
                print("+----------+------------------+----------+---------------+------------------+")
                for hanghoa in hoadon["danhsachhanghoa"]:
                    print("| "+hanghoa["stt_x"]+"  | " +hanghoa["ten_x"]+ " | "+hanghoa["soluong_x"]+" | "+hanghoa["dongia_x"]+" | "+hanghoa["thanhtien_x"]+" |")
                print("+----------+------------------+----------+---------------+------------------+")
                print("|          tong tien truoc thue                          |" +hoadon['tongtientt']+ "|")
                print("+--------------------------------------------------------+------------------+")
                print("|          tong tien (thue 10%)                          | "+hoadon['tongtienst']+"|")
                print("+--------------------------------------------------------+------------------+")
                break

def tongdoanhthu():
    tongdoanhthu = 0
    for hoadon in danhsachhoadon:
        tongdoanhthu = tongdoanhthu + hoadon["tongtien"]
    print("Tong doanh thu la: ", tongdoanhthu)

def tonghanghoabanra():
    tongsohanghoa = 0
    doanhsoban = 0

    tenhanghoa = input("nhap ten hang hoa can xem:")
    for hoadon in danhsachhoadon:
        for hanghoa in hoadon["danhsachhanghoa"]:
            if hanghoa["ten"] == tenhanghoa:
                tongsohanghoa = tongsohanghoa + hanghoa["soluong"]
                doanhsoban = doanhsoban + hanghoa["thanhtien"]
                break
    print("Tong so hang hoa: ", tongsohanghoa)
    print("Doanh so ban: ", doanhsoban)
