# 🚀 Web Performans ve Yükleme Süresi Ölçüm Aracı

Bu proje, **Python** ve **Selenium WebDriver** kullanarak belirlenen web sitelerinin sayfa yüklenme sürelerini (Page Load Time) otomatik olarak ölçen, analiz eden ve sonuçları CSV formatında raporlayan bir test otomasyon aracıdır.

## 📋 Proje Hakkında

Bu araç, web tarayıcılarının `window.performance` API'sini kullanarak hassas ölçümler yapar. Özellikle yazılım test ve doğrulama süreçlerinde performans metriklerini toplamak amacıyla geliştirilmiştir.

Program şu adımları izler:
1. Belirlenen 5 farklı web sitesini (Udemy, Harunider, Github, Kitapyurdu, Google, StackOverflow) ziyaret eder.
2. Her site için **10 kez** tekrar test yapar (Toplam 50 ölçüm).
3. Her yükleme için süreyi hesaplar.
4. Elde edilen verilerin **Ortalama**, **En Düşük (Min)** ve **En Yüksek (Max)** değerlerini hesaplar.
5. Tüm ham verileri ve istatistikleri `sonuclar.csv` dosyasına kaydeder.

## ⚙️ Kullanılan Teknoloji ve Algoritma

Proje, yükleme süresini hesaplamak için aşağıdaki W3C Navigation Timing standardını kullanır:

$$Yükleme Süresi = domComplete - navigationStart$$

* **navigationStart:** Tarayıcının kaynağı yüklemeye başladığı zaman damgası.
* **domComplete:** Sayfanın ve tüm alt kaynakların (resimler, scriptler vb.) yüklenmesinin bittiği zaman damgası.

## 🛠️ Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
* Python 3.x
* Google Chrome Tarayıcısı

### Kütüphanelerin Yüklenmesi
Gerekli olan `selenium` kütüphanesini yüklemek için terminalde şu komutu çalıştırın:

```bash
pip install selenium