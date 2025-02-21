print("welcome to BINUS @ malang Canteen")
print("1.Dmas")
print("2.Phoulette")
print("3.Lalapanku")
print("4.Baksoku")
print("5.Temenan sehat")
kedai = int(input("Pilih kedai [1-5]:"))

match kedai:
  case 1:
    print("welcome to DMAS")
    print("1.Gorengan Rp. 5000")
    print("2.Nasi goreng Rp 10000")
    print("3.Mie ayam Rp 8000")
    menu = int(input("pilih menu [1-3]:"))
    match menu :
      case 1:
        print("anda memilih gorengan, ayo bayar Rp 5000")
      case 2:
        print("anda memilih nasi goreng, ayo bayar Rp 10000")
      case 3:
        print("anda memilih mie ayam, ayo bayar Rp 8000")

    pembayaran = int(input("Tekan 1 untuk pembayaran tunak \n Tekan 2 untuk pembayaran Qris"))
    match pembayaran :
      case 1:
        print("Berikan uang anda")
      case 2 :
        print("scan kode ini")



match kedai:
  case 2:
    print("welcome to Phoulette")
    print("1.Katsu BBQ Rp. 20000")
    print("2.Katsu Chesee Rp 20000")
    print("3.Katsu Blackpapper Rp 20000")
    menu = int(input("pilih menu [1-3]:"))
    match menu :
      case 1:
        print("anda memilih katsu BBQ, ayo bayar Rp 20000")
      case 2:
        print("anda memilih katsu chesee, ayo bayar Rp 20000")
      case 3:
        print("anda memilih katsu blackpapper, ayo bayar Rp 20000")

    pembayaran = int(input("Tekan 1 untuk pembayaran tunak \n Tekan 2 untuk pembayaran Qris"))
    match pembayaran :
      case 1:
        print("Berikan uang anda")
      case 2 :
        print("scan kode ini")



match kedai:
  case 3:
    print("welcome to Lalapanku")
    print("1.Lalapan ayam Rp. 20000")
    print("2.Ayam geprek Rp 15000")
    print("3.Lalapan jamur Rp 10000")
    menu = int(input("pilih menu [1-3]:"))
    match menu :
      case 1:
        print("anda memilih Lalapan ayam, ayo bayar Rp 20000")
      case 2:
        print("anda memilih Ayam geprek, ayo bayar Rp 15000")
      case 3:
        print("anda memilih Lalapan jamur, ayo bayar Rp 10000")
    
    pembayaran = int(input("Tekan 1 untuk pembayaran tunak \n Tekan 2 untuk pembayaran Qris"))
    match pembayaran :
      case 1:
        print("Berikan uang anda")
      case 2 :
        print("scan kode ini")


match kedai:
  case 4:
    print("welcome to Baksoku")
    print("1.Pentol Rp. 5000")
    print("2.Siomay Rp 2000")
    print("3.Tahu Rp 2000")
    print("4.Mie kuning 1000")
    menu = int(input("pilih menu [1-4]:"))
    match menu :
      case 1:
        print("anda memilih pentol, ayo bayar Rp 5000")
      case 2:
        print("anda memilih siomay, ayo bayar Rp 2000")
      case 3:
        print("anda memilih tahu, ayo bayar Rp 2000")
      case 4:
        print("anda memilih mie kuning, ayo bayar Rp 1000")

    pembayaran = int(input("Tekan 1 untuk pembayaran tunak \n Tekan 2 untuk pembayaran Qris"))
    match pembayaran :
      case 1:
        print("Berikan uang anda")
      case 2 :
        print("scan kode ini")


match kedai:
  case 5:
    print("welcome to Temenan Sehat")
    print("1.Jus tropical Rp. 15000")
    print("2.Jus strawberry Rp 12000")
    print("3.Jus mangga Rp 13000")
    print("4.Jus anggur 20000")
    menu = int(input("pilih menu [1-4]:"))
    match menu :
      case 1:
        print("anda memilih pentol, ayo bayar Rp 5000")
      case 2:
        print("anda memilih siomay, ayo bayar Rp 2000")
      case 3:
        print("anda memilih tahu, ayo bayar Rp 2000")
      case 4:
        print("anda memilih mie kuning, ayo bayar Rp 1000")

    pembayaran = int(input("Tekan 1 untuk pembayaran tunak \n Tekan 2 untuk pembayaran Qris"))
    match pembayaran :
      case 1:
        print("Berikan uang anda")
      case 2 :
        print("scan kode ini")