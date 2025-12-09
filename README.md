🚀 Web Performans ve Yükleme Süresi Ölçüm Aracı

Bu proje, Python ve Selenium WebDriver kullanarak belirlenen web sitelerinin sayfa yüklenme sürelerini (Page Load Time) otomatik olarak ölçen, analiz eden ve sonuçları CSV formatında raporlayan bir test otomasyon aracıdır.

📋 Proje Hakkında

Bu araç, tarayıcıların window.performance API'sini kullanarak yükleme sürelerini milisaniye hassasiyetinde ölçer. Yazılım test ve doğrulama süreçlerinde performans metriklerini toplamak amacıyla geliştirilmiştir.

Program şu adımları takip eder:

Belirlenen web sitelerini ziyaret eder (Udemy, Harunider, GitHub, Kitapyurdu, Google, StackOverflow vb.).

Her site için 10 kez tekrar test yapar.

Her tekrar için yükleme süresini hesaplar.

Tüm verilerin Ortalama, En Düşük (Min) ve En Yüksek (Max) değerlerini çıkarır.

Tüm sonuçları sonuclar.csv dosyasına kaydeder.

⚙️ Kullanılan Teknoloji ve Algoritma

Proje, sayfanın yüklenme süresini aşağıdaki W3C Navigation Timing standardına göre hesaplar:

Yükleme Süresi = domComplete – navigationStart


navigationStart: Tarayıcının hedef kaynağı yüklemeye başladığı an.

domComplete: Sayfadaki tüm içeriklerin (HTML, img, script, CSS) yüklenmesinin tamamlandığı an.

🛠️ Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için şu adımları izleyin.

📌 Gereksinimler

Python 3.x

Google Chrome Tarayıcısı

Selenium WebDriver

📦 Kütüphanelerin Yüklenmesi

Aşağıdaki komutu terminalde çalıştırarak Selenium'u yükleyin:

pip install selenium

▶️ Kullanım

Proje klasörüne girin ve programı başlatın:

python performans_testi.py


Program çalıştığında otomatik olarak Chrome açılır ve test işlemleri başlar. Testler tamamlanınca tarayıcı kapanır ve sonuclar.csv dosyası oluşturulur.

📊 Örnek CSV Çıktısı
Web Sitesi, Deneme No, Yükleme Süresi (ms)
https://www.google.com, 1, 1240
https://www.google.com, 2, 1150
...
https://www.google.com İSTATİSTİK, Ortalama, 1195.00

📁 Dosya Yapısı
Dosya	Açıklama
performans_testi.py	Ana test senaryosu ve yükleme süresi ölçümleri
sonuclar.csv	Test tamamlandıktan sonra oluşturulan sonuç dosyası
README.md	Proje dökümantasyonu
👤 Yazar

Geliştirici: Harunİder10
Ders: Yazılım Test ve Doğrulama