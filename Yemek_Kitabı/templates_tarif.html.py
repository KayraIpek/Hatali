from flask import Flask, render_template, request

app = Flask(__name__)

# --- Sabit tarif listesi ---

tarifler = [
    {
        "ad": "Menemen",
        "resim": "menemen",
        "malzemeler": [
            "3 adet yumurta",
            "2 adet domates",
            "2 adet yeşil biber",
            "1 yemek kaşığı sıvı yağ",
            "Tuz, karabiber"
        ],
        "yapilis": [
            "Tavaya yağı koyup ısıtın, doğranmış biberleri ekleyip kavurun.",
            "Doğranmış domatesleri ekleyip suyunu çekene kadar pişirin.",
            "Yumurtaları kırın, isteğe göre karıştırarak ya da bütün bırakarak pişirin.",
            "Tuz ve karabiber ile tatlandırıp servis edin."
        ]
    },
    {
        "ad": "Islak Kek (Kakaolu)",
        "resim": "islak_kek",
        "malzemeler": [
            "3 adet yumurta",
            "1 su bardağı toz şeker",
            "1 su bardağı süt",
            "1 su bardağı sıvı yağ",
            "2 yemek kaşığı kakao",
            "1 paket kabartma tozu",
            "1,5 su bardağı un"
        ],
        "yapilis": [
            "Yumurta ve şekeri köpürene kadar çırpın.",
            "Süt, sıvı yağ, kakao ekleyip karıştırın, sonra un ve kabartma tozunu ekleyin.",
            "Yağlanmış kalıba döküp önceden ısıtılmış 180°C fırında yaklaşık 25–30 dakika pişirin.",
            "Fırından çıkarınca üzerine ılık sos döküp dinlendirdikten sonra servis edin."
        ]
    },
    {
        "ad": "Mercimek Çorbası",
        "resim": "MercoCorb",
        "malzemeler": [
            "1 su bardağı kırmızı mercimek",
            "1 adet soğan",
            "1 adet havuç (isteğe bağlı)",
            "1 yemek kaşığı un",
            "1 yemek kaşığı salça",
            "4 su bardağı su veya tavuk suyu",
            "Tuz, karabiber"
        ],
        "yapilis": [
            "Soğanı yemeklik doğrayıp tencerede yağ ile kavurun, rendelenmiş havucu ekleyin.",
            "Unu ve salçayı ekleyip kısaca karıştırın.",
            "Yıkanmış mercimek ve suyu ekleyip mercimekler yumuşayana kadar pişirin.",
            "Blenderdan geçirip pürüzsüz hale getirin, gerekirse kıvamını ayarlayın, tuz-karabiber ekleyip servise hazır hale getirin."
        ]
    },
    {
        "ad": "Meyhane Pilavı",
        "resim": "meyhn_plv",
        "malzemeler": [
            "1 su bardağı pilavlık bulgur",
            "1 orta boy soğan",
            "2 adet sivri biber",
            "1 adet küçük boy kapya biber",
            "2 orta boy domates",
            "1 yemek kaşığı domates salçası",
            "1 tatlı kaşığı tuz",
            "Sıvı yağ"
        ],
        "yapilis": [
            "Tencerede kıyılmış soğanı yağ ile pembeleşinceye kadar kavurun ve salça ekleyin.",
            "Küp küp doğranmış domates, sivri ve kapya biberleri ilave edin.",
            "Bulguru ekleyip hepsini birlikte bir iki dakika daha kavurun.",
            "Tuz ve 2 bardak sıcak suyu ekleyip kaynamaya bırakın.",
            "Kaynadıktan sonra ocağın ateşini kısıp tencerenin kapağını sıkıca kapatarak suyunu çekene kadar pişirin.",
            "Ocaktan alıp 10 dakika dinlendirdikten sonra karıştırıp servis edin."
        ]
    },
    {
        "ad": "Karnıyarık",
        "resim": "karnyark",
        "malzemeler": [
            "5 adet orta boy patlıcan",
            "300 g kıyma",
            "1 adet soğan",
            "2 diş sarımsak",
            "2 adet domates",
            "2 yemek kaşığı salça",
            "Tuz, karabiber, sıvı yağ"
        ],
        "yapilis": [
            "Patlıcanları alacalı soyup ortadan uzunlamasına yarın, tuzlu suda biraz bekletip kurulayın ve kızgın yağda kızartın veya fırında fırınlayın.",
            "Soğan ve sarımsağı doğrayıp kavurun, kıymayı ekleyip pişirin, salça ve doğranmış domatesleri ekleyip kıvam alana kadar pişirin; tuz ve karabiber ekleyin.",
            "Kızarmış patlıcanların ortasını açıp kıymalı harcı yerleştirip fırın tepsisine dizin, üzerlerine domates dilimi koyup 180°C’de 15–20 dakika pişirin.",
            "Sıcak servis edin."
        ]
    },
    {
        "ad": "Sütlaç",
        "resim": "sutlac",
        "malzemeler": [
            "1 litre süt",
            "1 çay bardağı pirinç",
            "1 su bardağı toz şeker",
            "1 yemek kaşığı nişasta (isteğe bağlı kıvam için)",
            "Tarçın (servis için)"
        ],
        "yapilis": [
            "Pirinçleri yıkayıp su ile yumuşayana kadar haşlayın.",
            "Sütü ekleyip kaynatın, şekerini ekleyip birkaç dakika daha pişirin.",
            "İstersen nişastayı az su ile açıp ekleyip kıvamını ayarlayın.",
            "Kaselere paylaştırıp soğuttuktan sonra tarçınla servis edin."
        ]
    }
]


@app.route('/')
def tarif_goster():
    # URL’deki ?index= parametresi hangi tarifi göstereceğimizi belirler
    index = int(request.args.get("index", 0))
    tarif = tarifler[index]

    # Geri / ileri geçiş için indeks hesapla
    onceki = (index - 1) % len(tarifler)
    sonraki = (index + 1) % len(tarifler)

    return render_template("tarif.html", tarif=tarif, onceki=onceki, sonraki=sonraki)

if __name__ == "__main__":
    app.run(debug=True)
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>{{ tarif.ad }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>{{ tarif.ad }}</h1>
        <img src="{{ url_for('static', filename=tarif.resim) }}" alt="Tarif Fotoğrafı" class="foto">


        <h2>Malzemeler</h2>
        <ul>
            {% for m in tarif.malzemeler %}
                <li>{{ m }}</li>
            {% endfor %}
        </ul>

        <h2>Yapılışı</h2>
        <ol>
            {% for adim in tarif.yapilis %}
                <li>{{ adim }}</li>
            {% endfor %}
        </ol>

        <div class="buttons">
            <a href="/?index={{ onceki }}" class="btn">⬅ Önceki</a>
            <a href="/?index={{ sonraki }}" class="btn">Sonraki ➡</a>
        </div>
    </div>
</body>
</html>
