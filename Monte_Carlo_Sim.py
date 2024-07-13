import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

#Varlık Fiyatı Çekme Fonksiyonu
def hisse(ad,periyod):
    veri=pd.DataFrame(yf.download(ad,period=periyod)["Adj Close"])
    veri["Getiri"]=veri["Adj Close"].pct_change()
    veri.dropna(axis=0,inplace=True)
    return veri

#Monte Carlo Simülasyonu Fonksiyonu
def mc(basla,ort,ss,sim,gün):
    array=np.zeros((sim,gün))

    for i in range(sim):
        norm=np.random.normal(ort,ss,gün)
        fiyat=[basla]

        for j in range(1,gün):
            fiyat.append(fiyat[-1]*(1+norm[j]))

        array[i,:]=fiyat
    return array

#Simülasyon İçin Gerekli Parametreler
hisse_senedi="XU100"

veri=hisse(hisse_senedi+"."+"IS",periyod="1y")
ilkfiyat=veri["Adj Close"].iloc[-1]
ort_getiri=np.mean(veri["Getiri"])
standart_sapma=np.std(veri["Getiri"])
deneme_sayısı=1000
gün_sayısı=252 

#Simülasyonu Çalıştırma
simülasyon=mc(ilkfiyat,ort_getiri,standart_sapma,deneme_sayısı,gün_sayısı)

#Güven Aralıkları ve Ortalama
alt_sınır=np.percentile(simülasyon,2.5,axis=0)
ust_sınır = np.percentile(simülasyon,97.5,axis=0)
sim_ort=np.mean(simülasyon,axis=0)

#Görselleştirme
plt.plot(simülasyon.T,alpha=0.1,color="blue")
plt.plot(sim_ort,color="red",label="Ortalama Simülasyon")
plt.plot(alt_sınır,color="black",linestyle="--",label="%95 Alt Güven Aralığı",linewidth=2.2)
plt.plot(ust_sınır,color="black",linestyle="--",label="%95 Üst Güven Aralığı",linewidth=2.2)
plt.title(f'{hisse_senedi} İçin Monte Carlo Simülasyonu (Deneme Sayısı:{deneme_sayısı})')
plt.xlabel("Gün Sayısı")
plt.ylabel("Fiyat")
plt.legend()
plt.tight_layout()
plt.show()
