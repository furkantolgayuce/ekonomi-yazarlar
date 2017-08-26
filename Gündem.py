import requests
from bs4 import BeautifulSoup
from datetime import *
dosya_adi="Gündem.html"
# Ay Çevirme Fonksiyonu #
bugun=str(datetime.now())
def ay_cevir():
    if (bugun[5:7]=="01"):
        gun= bugun[8:10] + " Ocak " + bugun[:4]
    elif (bugun[5:7]== "02" ):
        gun =bugun[8:10] + " Şubat "+ bugun[:4]
    elif (bugun[5:7]== "03" ):
        gun =bugun[8:10] + " Mart "+ bugun[:4]
    elif (bugun[5:7]== "04" ):
        gun= bugun[8:10] + " Nisan "+ bugun[:4]
    elif (bugun[5:7]== "05" ):
        gun=bugun[8:10] + " Mayıs "+ bugun[:4]
    elif (bugun[5:7]== "06" ):
        gun=bugun[8:10] + " Haziran "+ bugun[:4]
    elif (bugun[5:7]== "07"  ):
        gun =bugun[8:10] + " Temmuz " +bugun[:4]
    elif (bugun[5:7]== "08" ):
        gun =bugun[8:10] + " Ağustos "+ bugun[:4]
    elif (bugun[5:7]== "09"  ):
        gun=bugun[8:10] + " Eylül "+ bugun[:4]
    elif (bugun[5:7]== "10" ):
        gun=bugun[8:10] + " Ekim "+ bugun[:4]
    elif (bugun[5:7]== "11" ):
        gun=bugun[8:10] + " Kasım "+ bugun[:4]
    elif (bugun[5:7]== "12" ):
        gun=bugun[8:10] + " Aralık "+ bugun[:4]
    return gun
# Ay Çevirme Fonksiyonu Bitiş #

def navigasyon():
    # Hava Durumu - Borsa İstanbul - Dolar - Euro - Altın #

    # Tarih #
    tarih=ay_cevir()

    with open(dosya_adi, "w") as dosya:
        dosya.write("<!DOCTYPE html><html><head><link href='reset.css' type='text/css' rel='stylesheet'/></head><body><table border='1' ><tr><td><b>" + tarih + "</b></td>")

    dunya_url = "https://www.dunya.com/"
    r = requests.get(dunya_url)
    soup = BeautifulSoup(r.content, "html.parser")

    # Hava Durumu#
    hava_html = soup.find_all("span", {"class": "deg"})
    hava = "<b>Hava Durumu:</b> " + hava_html[0].text

    with open(dosya_adi, "a") as dosya:
        dosya.write("<td>" + hava + "</td></tr>")


    # Navigasyon #
    cubuk_html = soup.find_all("ul", {"class": "clearfix"})
    cubuk_html_gelenveri = cubuk_html[1].find_all("li")

    # Borsa İstanbul Endeks#
    bist_html_gelenveri = cubuk_html_gelenveri[0].find_all("span")
    bist = bist_html_gelenveri[0].text

    with open(dosya_adi, "a") as dosya:
        dosya.write("<tr><td>" + bist + "</td>")

    # Dolar#
    dolar_html_gelenveri = cubuk_html_gelenveri[1].find_all("span")
    dolar = dolar_html_gelenveri[0].text

    with open(dosya_adi, "a") as dosya:
        dosya.write("<td>" + dolar + "</td>")

    # Euro#
    euro_html_gelenveri = cubuk_html_gelenveri[2].find_all("span")
    euro = euro_html_gelenveri[0].text

    with open(dosya_adi, "a") as dosya:
        dosya.write("<td>" + euro + "</td>")

    # Altın#
    altın_html_gelenveri = cubuk_html_gelenveri[3].find_all("span")
    altın = altın_html_gelenveri[0].text

    with open(dosya_adi, "a") as dosya:
        dosya.write("<td>" + altın + "</td></tr>")

    # Hava Durumu - Borsa İstanbul - Dolar - Euro - Altın # Bitiş #

    # Son Açıklanan Ekonomi Verileri #

    ekonomi_html = soup.find_all("div", {"class": "fns-wid trk-eco"})
    ekonomi_html = ekonomi_html[0].find_all("div", {"class": "tbl"})
    ekonomi = ekonomi_html[0].text

    # İşsizlik #
    issizlik = ekonomi[3:30]

    with open(dosya_adi, "a") as dosya:
        dosya.write("<tr><td>" + issizlik + "</td>")

    # Cari Açık #
    cari_acik = ekonomi[34:70]

    with open(dosya_adi, "a") as dosya:
        dosya.write("<td>" + cari_acik + "</td>")

    # Sanayi Üretimi #
    sanayi_uretimi = ekonomi[70:107]

    with open(dosya_adi, "a") as dosya:
        dosya.write("<td>" + sanayi_uretimi + "</td>")

    # TÜFE #
    tufe = ekonomi[107:136]

    with open(dosya_adi, "a") as dosya:
        dosya.write("<td>" + tufe + "</td></tr></table>")
        dosya.write("<br><br>")
        # Son Açıklanan Ekonomi Verileri # Bitiş #
def bloomberg_ht(yazar,bloomberg_url):
    bugun = ay_cevir()
    bugun = str(bugun[:14])
    ##URL BULMA AŞAMASI

    r = requests.get(bloomberg_url)
    soup = BeautifulSoup(r.content, "html.parser")

    bugun = str(datetime.now())
    bugun = bugun[8:10]

    satir_html = soup.find_all("div", {"class": "col-lg-12 col-md-12 col-sm-12 col-xs-12 pad0 marB10"})
    tarih = satir_html[0].find_all("span", {"class": "timeGroup"})
    tarih = str(tarih[0].text)
    tarih = tarih[0:2]
    linkler = satir_html[0].find_all("a")
    for link in linkler:
        url = link.get("href")
    url = "http://www.bloomberght.com" + url

    if (bugun == tarih):

        # URL SONRASI AŞAMA
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        tarih_html = soup.find_all("li", {"class": "pull-right"})
        tarih = tarih_html[0].text
        tarih = str(tarih[:14])

        baslik_html = soup.find_all("h2")
        baslik = baslik_html[0].text

        metin = soup.find_all("p")
        metin = str(metin)

        with open(dosya_adi, "a") as dosya:
            dosya.write("<br><br><br>")
            dosya.write(
                "<h1>" + yazar + "<br>" + "<a href='" + url + "' target='_blank' style='text-decoration:none'>" + baslik + "</a></h1><br>")
            dosya.write("<b>Tarih: </b>" + tarih + "<br><br>")
            dosya.write(metin)
        print(yazar + " Yazısı Eklendi.")
    else:
        print(yazar + " Bugün Yazısı Yok.")
def mahfi_egilmez(yazar,m_egilmezurl):
    bugun = ay_cevir()
    bugun = str(bugun[:14])
    ##URL BULMA AŞAMASI
    r = requests.get(m_egilmezurl)
    soup = BeautifulSoup(r.content, "html.parser")

    bugun = ay_cevir()
    bugun = str(bugun[:14])

    tarih_html = soup.find_all("h2", {"class": "date-header"})
    tarih = str(tarih_html[0].text)
    tarih = tarih[:14]
    url_html = soup.find_all("h3", {"class": "post-title entry-title"})
    url_html_gelenveri = (url_html[0])
    linkler = url_html_gelenveri.find_all("a")
    for link in linkler:
        url = link.get("href")

    if (bugun == tarih):

        # URL SONRASI AŞAMA
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        tarih_html = soup.find_all("h2", {"class": "date-header"})
        tarih = tarih_html[0].text
        tarih = str(tarih)
        baslik_html = soup.find_all("h3", {"class": "post-title entry-title"})
        baslik = baslik_html[0].text

        metin_html = soup.find_all("div", {"class": "post-body entry-content"})
        metin = metin_html[0]
        metin = str(metin)

        with open(dosya_adi, "a") as dosya:
            dosya.write(
                "<h1>" + yazar + "<br>" + "<a href='" + url + "' target='_blank' style='text-decoration:none'>" + baslik + "</a></h1><br>")
            dosya.write("<b>Tarih: </b>" + tarih + "<br><br>")
            dosya.write(metin)
            print(yazar + " Yazısı Eklendi.")
    else:
        print(yazar + " Bugün Yazısı Yok.")
def dunya_yazar(yazar,dunya_url):
    bugun = ay_cevir()
    bugun = str(bugun[:14])

    ##URL BULMA AŞAMASI
    r = requests.get(dunya_url)
    soup = BeautifulSoup(r.content, "html.parser")

    tarih_html = soup.find_all("time")
    tarih = str(tarih_html[0].text)
    tarih = str(tarih[:14])
    url_html = soup.find_all("article")
    url_html_gelenveri = (url_html[0])
    linkler = url_html_gelenveri.find_all("a")
    for link in linkler:
        url = link.get("href")
    url = "https://www.dunya.com" + url

    if (bugun == tarih):

        # URL SONRASI AŞAMA
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        tarih_html = soup.find_all("time")
        tarih = tarih_html[0].text
        tarih = str(tarih)
        baslik_html = soup.find_all("h1")
        baslik = baslik_html[0].text

        metin_html = soup.find_all("div", {"class": "artc-cnt"})
        metin = metin_html[0]
        metin = str(metin)

        with open(dosya_adi, "a") as dosya:
            dosya.write(
                "<h1>" + yazar + "<br>" + "<a href='" + url + "' target='_blank' style='text-decoration:none'>" + baslik + "</a></h1><br>")
            dosya.write("<b>Tarih: </b>" + tarih + "<br><br>")
            dosya.write(metin)
        print(yazar + " Yazısı Eklendi.")
    else:
        print(yazar + " Bugün Yazısı Yok.")
def milliyet_yazar(yazar,milliyet_url):
    bugun = str(datetime.now())
    bugun = bugun[8:10]
    ##URL BULMA AŞAMASI
    r = requests.get(milliyet_url)
    soup = BeautifulSoup(r.content, "html.parser")

    tarih_html = soup.find_all("em")
    tarih = str(tarih_html[5].text)
    tarih = tarih[:2]
    url_html = soup.find_all("li")
    url_html_gelenveri = (url_html[6])
    linkler = url_html_gelenveri.find_all("a")
    for link in linkler:
        url = link.get("href")
    url = "http://www.milliyet.com.tr" + url
    if (bugun == tarih):

        # URL SONRASI AŞAMA
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        tarih = str(datetime.now())
        tarih = tarih[:10]
        baslik_html = soup.find_all("h1", {"itemprop": "headline"})
        baslik = baslik_html[0].text

        metin = soup.find_all("p")
        metin = str(metin)

        with open(dosya_adi, "a") as dosya:
            dosya.write(
                "<h1>" + yazar + "<br>" + "<a href='" + url + "' target='_blank' style='text-decoration:none'>" + baslik + "</a></h1><br>")
            dosya.write("<b>Tarih: </b>" + tarih + "<br><br>")
            dosya.write(metin)
        print(yazar + " Yazısı Eklendi.")
    else:
        print(yazar + " Bugün Yazısı Yok.")
def yasar_erdinc(yazar, bilge_yatirimci_url):
    bugun = ay_cevir()
    bugun = str(bugun[:14])


    ##URL BULMA AŞAMASI
    r = requests.get(bilge_yatirimci_url)
    soup = BeautifulSoup(r.content, "html.parser")

    tarih_html = soup.find_all("span", {"class": "entry-date"})
    tarih = str(tarih_html[0].text)
    tarih = str(tarih[:14])

    url_html = soup.find_all("h2", {"class": "art-postheader"})
    url_html_gelenveri = (url_html[0])
    linkler = url_html_gelenveri.find_all("a")
    for link in linkler:
        url = link.get("href")
    if (bugun == tarih):

    # URL SONRASI AŞAMA
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        tarih_html = soup.find_all("span", {"class": "entry-date"})
        tarih = str(tarih_html[0].text)
        tarih = str(tarih[:14])

        baslik_html = soup.find_all("h1")
        baslik = baslik_html[0].text

        metin_html = soup.find_all("div", {"class": "art-postcontent"})
        metin = metin_html[0]
        metin = str(metin)

        with open(dosya_adi, "a") as dosya:
            dosya.write(
                "<h1>" + yazar + "<br>" + "<a href='" + url + "' target='_blank' style='text-decoration:none'>" + baslik + "</a></h1><br>")
            dosya.write("<b>Tarih: </b>" + tarih + "<br><br>")
            dosya.write(metin)
        print(yazar + " Yazısı Eklendi.")
    else:
        print(yazar + " Bugün Yazısı Yok.")
with open(dosya_adi, "a") as dosya:
    dosya.write("</body>    </html>")


# Fonksiyon İşleme #
navigasyon()
dunya_yazar("Alaattin AKTAŞ","https://www.dunya.com/yazar/alaattin-aktas/30")
dunya_yazar("Tevfik GÜNGÖR","https://www.dunya.com/yazar/tevfik-gungor/18")
dunya_yazar("Özcan KADIOĞLU","https://www.dunya.com/yazar/ozcan-kadioglu/246")
dunya_yazar("Serbest Kürsü","https://www.dunya.com/yazar/serbest-kursu/1014")
dunya_yazar("Kemal DERVİŞ","https://www.dunya.com/yazar/kemal-dervis/212")
dunya_yazar("Taner BERKSOY","https://www.dunya.com/yazar/taner-berksoy/132")
mahfi_egilmez("Mahfi Eğilmez","http://www.mahfiegilmez.com/")
bloomberg_ht("Cüneyt Başaran", "http://www.bloomberght.com/ht-yazarlar/cuneyt-basaran-2071/2071")
dunya_yazar("Uğur CİVELEK","https://www.dunya.com/yazar/ugur-civelek/41")
milliyet_yazar("Güngör Uras","http://www.milliyet.com.tr/yazarlar/gungor-uras/")
yasar_erdinc("Yaşar Erdinç","https://www.bilgeyatirimci.com/category/ye/")