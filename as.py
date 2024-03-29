from scipy import stats # scipy paketini chaqirib foydalanish

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # X = Avtpomobilning yoshi
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # Y = Avtomobil tezligi

slope, intercept, r, p, std_err = stats.linregress(x, y)
#stats.linregress(x, y) funktsiyasi scipy modulida mavjud bo'lgan chiziqli regressiya 
def myfunc(x): # myfunc(x) funktsiyasi avtomobilning yoshiga moslashtirilgan tezligini qaytaradi
  return slope * x + intercept
        #slope va intercept o'zgaruvchilar tezligi va boshlanish nuqtasi uchun moslashtirilgan 
        #chiziqli regressiya funksiyasining ko'efitsiyentlari bo'ladi.
speed = myfunc(10)
    #speed = myfunc(10) avtomobilning 10 yoshda bo'lgan tezligini hisoblaydi va speed o'zgaruvchisiga yozadi.
print(speed) # ishga tushirish