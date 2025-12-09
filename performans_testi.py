import csv
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# 1. Test edilecek sitelerin listesi
siteler = [
    "https://www.harunider.com.tr",
    "https://www.udemy.com",
    "https://github.com",
    "https://www.kitapyurdu.com",
    "https://stackoverflow.com"
]

# 2. Chrome tarayıcısını başlat (Döngü dışında başlatmak performansı artırır)
options = webdriver.ChromeOptions()
# options.add_argument("--headless") # İstersen tarayıcıyı görmemek için bu satırı açabilirsin
driver = webdriver.Chrome(options=options)

print("Test başlıyor, lütfen bekleyiniz...\n")

# CSV dosyasını yazma modunda açıyoruz
with open('sonuclar.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV Başlıkları
    writer.writerow(['Web Sitesi', 'Deneme No', 'Yükleme Süresi (ms)'])

    # Her site için döngü
    for url in siteler:
        print(f"--- {url} test ediliyor ---")
        site_sureleri = [] # İstatistik hesabı için süreleri tutacak liste

        # Her siteyi 10 kez test et
        for i in range(1, 11):
            try:
                driver.get(url)
                
                # Sayfanın tamamen oturması için kısa bir bekleme (Opsiyonel ama sağlıklı ölçüm için önerilir)
                # time.sleep(1) 

                # JavaScript ile performans verilerini al
                timing = driver.execute_script("return window.performance.timing")
                
                navigation_start = timing["navigationStart"]
                dom_complete = timing["domComplete"]

                # Eğer domComplete henüz oluşmadıysa (0 dönerse), veri hatalı olmasın diye kontrol
                if dom_complete == 0:
                     # Çok hızlı yüklemelerde bazen 0 gelebilir, tekrar dener veya es geçeriz
                    yuklenme_suresi = 0 
                else:
                    yuklenme_suresi = dom_complete - navigation_start
                
                # Listeye ekle ve CSV'ye yaz
                site_sureleri.append(yuklenme_suresi)
                writer.writerow([url, i, yuklenme_suresi])
                
                print(f"Deneme {i}: {yuklenme_suresi} ms")

            except WebDriverException as e:
                print(f"Hata oluştu ({url}): {e}")

        # 3. İstatistikleri Hesapla (Ortalama, En Düşük, En Yüksek)
        if site_sureleri:
            ortalama = sum(site_sureleri) / len(site_sureleri)
            en_dusuk = min(site_sureleri)
            en_yuksek = max(site_sureleri)

            print(f"\n> SONUÇLAR ({url}):")
            print(f"  Ortalama: {ortalama:.2f} ms")
            print(f"  En Düşük: {en_dusuk} ms")
            print(f"  En Yüksek: {en_yuksek} ms")
            print("-" * 30)
            
            # İstatistikleri de CSV dosyasına ekleyelim (Opsiyonel, rapor için güzel olur)
            writer.writerow([f"{url} İSTATİSTİK", "Ortalama", f"{ortalama:.2f}"])
            writer.writerow([f"{url} İSTATİSTİK", "Min", en_dusuk])
            writer.writerow([f"{url} İSTATİSTİK", "Max", en_yuksek])
            writer.writerow([]) # Boş satır

# 4. Tarayıcıyı kapat
driver.quit()
print("\nTest tamamlandı. Veriler 'sonuclar.csv' dosyasına kaydedildi.")