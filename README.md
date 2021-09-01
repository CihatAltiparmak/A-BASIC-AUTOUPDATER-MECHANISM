# A BASIC AUTOUPDATER MECHANISM

Merhaba, kendimce uygulama açılınca güncelleme olup olmadığını kontrol eden, eğer uygulamamız güncel değilse uygulamamızı güncelleyen bir mekanizma yazdım.

Şimdi bizim temelde iki tane bileşenimiz var. Birincisi, uygulamayı başlatan script, diğeri de uygulamanın ta kendisi.

Öncelikle uygulamayı başlatacak olan scriptten uygulamanın güncel olup olmadığını kontrol ediyoruz (Bu iş için localimizde bulunan uygulama dizinindeki `version.json` u kullanıyoruz, `version.json` daki version bilgisyle githubdaki `version.json` un bilgilerini karşılaştırıyoruz. Eğer iki bilgi de aynıysa uygulamammız zaten günceldir). 

Eğer uygulama güncel ise uygulamayı direkt açıyoruz.

Eğer uygulamamız güncel değil ise önce `main.py (uygulamayı açan script)` dosyası dışındaki bütün dosya ve dizini siliyoruz. 

Sonra github repomuzdan güncel uygulamayı `zip şeklinde` çekiyoruz ve bunu .cache adlı bir dizin oluşturarak bu zipi o dizine koyuyoruz. Sonra da zipi orada çıkarıyoruz.

En son bu `.cache` dizininde bulunan dosyaları vs. bizim kendi uygulama dizinimize taşıyoruz. Böylelikle uygulamamız güncellenmiş oluyor.

Bu arada neden `main.py` dosyası silinmiyor diye soranlar olabilir. `main.py` dosyası bizim çalışan dosyamız. Bu yüzden silinemez (en azında Windows'da, Linux'da silinebilir*)


* Kaynağım yok, sadece deneme yanılma yoluyla test ettim bu olayı. 

* Bir şeyi anlatırken yanlış bilgi verdiysem bunu lütfen issue açın veya herhangi bir iletişim kanalından bana ulaşınız. Ve dediğim şeyleri bir araştırmanızı öneriyorum. Araştırmak güzeldir.
