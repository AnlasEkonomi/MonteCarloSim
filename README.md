# Monte Carlo Simülasyonu


Monte Carlo Simülasyonu, sonuçları hesaplamak için tekrarlanan rastgele örneklemeye ve istatistiksel analize
dayanan bir simülasyon türüdür (Raychaudhuri, 2008:91).

Monte Carlo Simülasyonu ilk olarak atom bombası üzerinde çalışan bilim adamları tarafından kullanılmıştır
(Kochanski, 2005: 1). İsmini kumarhaneleriyle ünlü Monako tatil beldesi Monte Carlo'dan almıştır. İkinci Dünya
Savaşı'ndaki tanıtımından bu yana, Monte Carlo Simülasyonu çeşitli fiziksel ve kavramsal sistemleri modellemek için
kullanılmıştır (Balogh vd.; 2013: 33-34).

Monte Carlo simülasyonu analitik olarak zor olan ve deney yapmanın çok zaman alıcı ve maliyetli olduğu veya
pratik olmadığı problemler için çok kullanılan bir bilimsel araçtır (Harrison, 2010: 17-18).

Bir çok alanda aktif olarak kullanılan bu yöntemin arkasında yatan mantık, gelecekteki belirsizliğin sınırlarını çizmek adına var olan veri setininin dağılımını taklit etmek ve bunu çok defa tekrarlamak. Normal dağılımdan spesifik dağılımlara kadar kullanılabilir. Ancak Central Limit Theorem (Merkezi Limit Teoremi) göz önüne alınarak gelenllikle normal dağılım simüle edilmeye çalışılır. 

![222](https://github.com/user-attachments/assets/106230c1-cf2b-4b70-8b56-754b34e82a48)



Örneğimizde Bist100 verilerini kullanarak örnek bir çalışma yazdım. Fiyat verileri yerine daha bariz bir dağılım gösteren getirileri kullanarak simülasyonu gerçekleştirdim. Daha sonra simüle edilmiş getiriler üzerinden tekrar fiyat hesaplaması yaptım. 

Not: Ne kadarlık bir simüle sayısı ve ne kadarlık geçmişe yönelik veriye ihtiyacımız olması konusu daha teknik bir konudur. O konuya burada girmiyorum. Merak edenler için hem Türkçe hem de İngilizce olarak bir çok Monte Carlo Simülasyonu çalışması internette mevcuttur.

