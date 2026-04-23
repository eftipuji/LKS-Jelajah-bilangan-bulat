import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ─────────────────────────────────────────
# KONFIGURASI HALAMAN
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Jelajah Bilangan Bulat",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────
# CSS KUSTOM
# ─────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }

    /* Header utama */
    .main-header {
        background: linear-gradient(135deg, #1A3C6E 0%, #2E75B6 60%, #70AD47 100%);
        color: white; padding: 1.5rem 2rem; border-radius: 16px;
        text-align: center; margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(26,60,110,0.3);
    }
    .main-header h1 { font-size: 2rem; font-weight: 800; margin: 0; }
    .main-header p  { font-size: 1rem; margin: 0.3rem 0 0; opacity: 0.9; }

    /* Box fase discovery */
    .fase-box {
        border-left: 5px solid #2E75B6; background: #EBF3FB;
        padding: 0.8rem 1rem; border-radius: 0 10px 10px 0;
        margin: 0.7rem 0;
    }
    .fase-box .fase-label {
        font-weight: 800; color: #1A3C6E; font-size: 0.85rem;
        text-transform: uppercase; letter-spacing: 1px;
    }
    .fase-box .fase-text { color: #2C3E50; font-size: 0.95rem; margin-top: 0.2rem; }

    /* Card informasi */
    .info-card {
        background: #F0F7FF; border: 1px solid #BDD7EE;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }
    .warning-card {
        background: #FFF8E6; border: 1px solid #FFD966;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }
    .success-card {
        background: #F0FBF0; border: 1px solid #70AD47;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }
    .danger-card {
        background: #FEF0F0; border: 1px solid #E74C3C;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }

    /* Hasil kalkulator */
    .result-display {
        background: linear-gradient(135deg, #1A3C6E, #2E75B6);
        color: white; border-radius: 16px; padding: 1.5rem;
        text-align: center; font-size: 2.5rem; font-weight: 800;
        box-shadow: 0 4px 15px rgba(26,60,110,0.3); margin: 1rem 0;
    }
    .result-label { font-size: 0.85rem; opacity: 0.8; margin-bottom: 0.3rem; }

    /* Tabel eksplorasi */
    .table-header {
        background: #1A3C6E; color: white;
        padding: 0.5rem 1rem; border-radius: 8px 8px 0 0;
        font-weight: 700; font-size: 0.9rem;
    }

    /* Badge tanda */
    .badge-pos { background:#70AD47; color:white; padding:3px 12px; border-radius:20px; font-weight:700; }
    .badge-neg { background:#C00000; color:white; padding:3px 12px; border-radius:20px; font-weight:700; }
    .badge-nol { background:#7F7F7F; color:white; padding:3px 12px; border-radius:20px; font-weight:700; }

    /* Sidebar */
    .sidebar-title {
        background: #1A3C6E; color: white;
        padding: 0.7rem 1rem; border-radius: 10px;
        font-weight: 800; text-align: center; margin-bottom: 0.5rem;
    }

    /* Tombol kustom */
    .stButton > button {
        border-radius: 10px; font-weight: 700;
        transition: all 0.2s;
    }
    .stButton > button:hover { transform: translateY(-2px); }

    /* Metric */
    [data-testid="metric-container"] {
        background: #F8FAFF; border: 1px solid #BDD7EE;
        border-radius: 12px; padding: 0.8rem; text-align: center;
    }

    /* Nomor soal */
    .soal-num {
        background: #2E75B6; color: white;
        width: 30px; height: 30px; border-radius: 50%;
        display: inline-flex; align-items: center; justify-content: center;
        font-weight: 800; font-size: 0.9rem; margin-right: 0.5rem;
    }

    hr { border: none; border-top: 2px solid #EBF3FB; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# HEADER UTAMA
# ─────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>🔢 Jelajah Bilangan Bulat</h1>
    <p>Kalkulator Digital Interaktif • Metode Discovery Learning • SMP/MTs Kelas VII</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# SIDEBAR NAVIGASI
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧭 Menu Navigasi</div>', unsafe_allow_html=True)
    tab_choice = st.radio(
        "Pilih Fitur:",
        options=[
            "🏠 Beranda",
            "📍 KP 1 — Garis Bilangan",
            "🔧 KP 2 — Kalkulator Operasi",
            "🌳 KP 3 — Pohon Faktor & FPB/KPK",
            "📝 Soal Latihan Interaktif",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("""
    <div style="background:#F0F7FF;padding:0.8rem;border-radius:10px;font-size:0.82rem;color:#1A3C6E;">
    <b>📚 Petunjuk Penggunaan</b><br><br>
    1. Pilih fitur sesuai kegiatan pembelajaran<br>
    2. Ikuti langkah-langkah Discovery Learning<br>
    3. Catat temuan di LKS<br>
    4. Diskusikan dengan kelompokmu<br>
    5. Kerjakan soal latihan di akhir
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.78rem;color:#7F7F7F;text-align:center;">
    🎓 Kurikulum Merdeka Fase D<br>
    Penulis: Rini Utami, S.Pd., M.Pd
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# HALAMAN BERANDA
# ══════════════════════════════════════════
if tab_choice == "🏠 Beranda":
    st.markdown("## 👋 Selamat Datang, Penjelajah Matematika!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="info-card">
        <b>🎯 Fokus Kemampuan</b><br><br>
        ✅ Operasi Hitung Bilangan Bulat (TP 5)<br>
        ✅ FPB & KPK via Faktorisasi Prima (TP 8)<br>
        ✅ Masalah Kontekstual & Literasi Finansial (TP 9)
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
        <b>🔬 Metode Pembelajaran</b><br><br>
        🔵 Discovery Learning (utama)<br>
        🟢 Problem Based Learning<br>
        🟡 Cooperative Learning
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="info-card">
        <b>📱 Fitur Aplikasi</b><br><br>
        📍 Garis Bilangan Interaktif<br>
        🔧 Kalkulator Operasi Hitung<br>
        🌳 Pohon Faktor & FPB/KPK<br>
        📝 Soal Latihan Interaktif
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔬 Alur Discovery Learning dalam Aplikasi Ini")

    fases = [
        ("① STIMULATION","Kamu akan dihadapkan pada situasi nyata yang menantang — tentang suhu, uang, atau lampu yang berkedip. Ini akan membuatmu penasaran!","#2E75B6"),
        ("② PROBLEM STATEMENT","Kamu merumuskan pertanyaan sendiri. Apa yang ingin kamu temukan?","#ED7D31"),
        ("③ DATA COLLECTION","Eksplorasi bebas menggunakan kalkulator digital! Coba berbagai kombinasi dan catat hasilnya di LKS.","#70AD47"),
        ("④ DATA PROCESSING","Analisis pola dari data yang kamu kumpulkan. Apa yang kamu temukan?","#7030A0"),
        ("⑤ VERIFICATION","Bandingkan temuanmu dengan teman sekelompok. Apakah sama?","#C00000"),
        ("⑥ GENERALIZATION","Rumuskan kesimpulan dengan kata-katamu sendiri. Inilah ilmu yang benar-benar kamu pahami!","#1A3C6E"),
    ]

    cols = st.columns(3)
    for i, (label, text, color) in enumerate(fases):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="border-left:4px solid {color};background:#FAFAFA;
                        padding:0.8rem 1rem;border-radius:0 10px 10px 0;margin-bottom:0.8rem;">
                <div style="font-weight:800;color:{color};font-size:0.9rem;">{label}</div>
                <div style="font-size:0.85rem;color:#444;margin-top:0.3rem;">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="warning-card">
    <b>💡 Tips Belajar Efektif</b><br>
    Jangan langsung klik-klik tanpa tujuan! Sebelum mengeksplorasi, baca dulu petunjuk di LKS,
    lalu gunakan kalkulator digital ini untuk <b>membuktikan hipotesismu</b> dan
    <b>menemukan pola</b> yang tersembunyi dalam bilangan bulat. Catat semua temuanmu!
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# KP 1 — GARIS BILANGAN
# ══════════════════════════════════════════
elif tab_choice == "📍 KP 1 — Garis Bilangan":
    st.markdown("## 📍 Kegiatan Pembelajaran 1: Memahami Bilangan Bulat")

    # STIMULATION
    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik</div>
        <div class="fase-text">
        Suhu di <b>Puncak Jaya, Papua</b> bisa mencapai <b style="color:#C00000">−3°C</b>,
        sementara di <b>Kota Kupang</b> bisa mencapai <b style="color:#70AD47">+30°C</b>.
        Kedalaman <b>Palung Jawa</b> adalah <b style="color:#C00000">−7.000 m</b> dari permukaan laut.<br><br>
        <b>❓ Apa arti tanda "−" (negatif) pada bilangan-bilangan tersebut?</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # PROBLEM STATEMENT
    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">② Problem Statement — Rumusan Masalah</div>
        <div class="fase-text">
        Sebelum bereksplorasi, tuliskan dulu hipotesismu di LKS:<br>
        <i>"Menurutku, bilangan bulat negatif adalah... dan letaknya pada garis bilangan ada di..."</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # DATA COLLECTION — Garis Bilangan Interaktif
    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">③ Data Collection — Eksplorasi Garis Bilangan</div>
        <div class="fase-text">Gunakan slider di bawah untuk menempatkan bilangan pada garis bilangan.
        Amati letaknya dan catat temuanmu di LKS!</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        bilangan = st.slider("Pilih Bilangan:", min_value=-20, max_value=20, value=0, step=1)
        st.markdown(f"""
        <div class="result-display" style="font-size:3rem;">
            {bilangan:+d}
        </div>
        """, unsafe_allow_html=True)

        if bilangan > 0:
            st.markdown('<div class="success-card">✅ <b>Bilangan Bulat POSITIF</b><br>Terletak di sebelah <b>KANAN</b> nol pada garis bilangan</div>', unsafe_allow_html=True)
        elif bilangan < 0:
            st.markdown('<div class="danger-card">🔴 <b>Bilangan Bulat NEGATIF</b><br>Terletak di sebelah <b>KIRI</b> nol pada garis bilangan</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="info-card">⚪ <b>NOL</b><br>Bukan positif, bukan negatif. Titik tengah garis bilangan.</div>', unsafe_allow_html=True)

        inv = -bilangan
        st.markdown(f"""
        <div class="warning-card">
        <b>🔄 Invers Penjumlahan:</b><br>
        Invers dari <b>{bilangan:+d}</b> adalah <b>{inv:+d}</b><br>
        Bukti: <b>{bilangan:+d} + ({inv:+d}) = {bilangan+inv}</b>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Visualisasi garis bilangan
        fig, ax = plt.subplots(figsize=(10, 3.5))
        ax.set_xlim(-22, 22)
        ax.set_ylim(-1.5, 2)
        ax.axis("off")
        fig.patch.set_facecolor('#FAFBFF')
        ax.set_facecolor('#FAFBFF')

        # Garis utama
        ax.annotate("", xy=(21.5, 0), xytext=(-21.5, 0),
                    arrowprops=dict(arrowstyle="<->", color="#1A3C6E", lw=2.5))

        # Tick marks dan label
        for i in range(-20, 21):
            tick_h = 0.25 if i % 5 == 0 else 0.15
            col_tick = "#1A3C6E" if i % 5 == 0 else "#AAAAAA"
            ax.plot([i, i], [-tick_h, tick_h], color=col_tick, lw=1.5)
            if i % 5 == 0:
                ax.text(i, -0.55, str(i), ha='center', va='top',
                        fontsize=9, color="#1A3C6E", fontweight='bold')

        # Label negatif/positif
        ax.text(-10, 1.5, "← BILANGAN NEGATIF", ha='center', fontsize=9,
                color="#C00000", fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEEEE', edgecolor='#C00000', alpha=0.8))
        ax.text(10, 1.5, "BILANGAN POSITIF →", ha='center', fontsize=9,
                color="#70AD47", fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#EEFFEE', edgecolor='#70AD47', alpha=0.8))
        ax.text(0, 1.5, "NOL", ha='center', fontsize=9,
                color="#7F7F7F", fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#7F7F7F', alpha=0.8))

        # Titik yang dipilih
        dot_color = "#C00000" if bilangan < 0 else ("#70AD47" if bilangan > 0 else "#7F7F7F")
        ax.plot(bilangan, 0, 'o', color=dot_color, markersize=18, zorder=5,
                markeredgecolor='white', markeredgewidth=2)
        ax.text(bilangan, 0.7, f"{bilangan:+d}", ha='center', fontsize=12,
                color=dot_color, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=dot_color, lw=2))

        # Garis invers
        if bilangan != 0:
            ax.annotate("", xy=(inv, 0), xytext=(bilangan, 0),
                        arrowprops=dict(arrowstyle="->", color="#ED7D31", lw=1.5,
                                       connectionstyle="arc3,rad=-0.4"))
            mid = (bilangan + inv) / 2
            ax.text(mid, -1.1, f"invers = {inv:+d}", ha='center',
                    fontsize=8.5, color="#ED7D31", fontstyle='italic')

        ax.set_title("Garis Bilangan Interaktif — Kalkulator Digital Streamlit",
                     pad=8, fontsize=10, color="#1A3C6E", fontweight='bold')
        st.pyplot(fig)
        plt.close()

    st.markdown("---")

    # DATA PROCESSING — Tabel
    st.markdown("""
    <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
        <div class="fase-label" style="color:#7030A0;">④ Data Processing — Analisis Pola</div>
        <div class="fase-text">Eksplorasi beberapa bilangan menggunakan slider, lalu lengkapi tabel di LKS-mu:</div>
    </div>
    """, unsafe_allow_html=True)

    contoh_data = [
        ("+8", "Kanan nol", "✅ Positif", "+8 + (−8) = 0", "−8"),
        ("−5", "Kiri nol", "🔴 Negatif", "−5 + (+5) = 0", "+5"),
        ("0", "Titik tengah", "⚪ Nol", "0 + 0 = 0", "0"),
        ("−12", "...", "...", "...", "..."),
        ("+17", "...", "...", "...", "..."),
    ]

    st.markdown("""
    <table style="width:100%;border-collapse:collapse;font-size:0.88rem;">
    <tr style="background:#1A3C6E;color:white;">
        <th style="padding:8px;border:1px solid #ccc;">Bilangan</th>
        <th style="padding:8px;border:1px solid #ccc;">Letak pada Garis Bilangan</th>
        <th style="padding:8px;border:1px solid #ccc;">Jenis</th>
        <th style="padding:8px;border:1px solid #ccc;">Pembuktian Invers</th>
        <th style="padding:8px;border:1px solid #ccc;">Invers Penjumlahan</th>
    </tr>
    """ + "".join([f"""
    <tr style="background:{'#F8FAFF' if i%2==0 else 'white'};">
        <td style="padding:8px;border:1px solid #ccc;font-weight:bold;text-align:center;">{r[0]}</td>
        <td style="padding:8px;border:1px solid #ccc;text-align:center;">{r[1]}</td>
        <td style="padding:8px;border:1px solid #ccc;text-align:center;">{r[2]}</td>
        <td style="padding:8px;border:1px solid #ccc;text-align:center;">{r[3]}</td>
        <td style="padding:8px;border:1px solid #ccc;text-align:center;font-weight:bold;color:#1A3C6E;">{r[4]}</td>
    </tr>
    """ for i, r in enumerate(contoh_data)]) + "</table>", unsafe_allow_html=True)

    st.markdown("*(Baris kosong diisi berdasarkan eksplorasimu menggunakan slider)*", unsafe_allow_html=True)

    # GENERALIZATION
    st.markdown("---")
    st.markdown("""
    <div class="fase-box" style="border-color:#1A3C6E;background:#EBF3FB;">
        <div class="fase-label">⑥ Generalization — Simpulan</div>
        <div class="fase-text">Tuliskan simpulanmu di LKS berdasarkan eksplorasimu:</div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("💡 Lihat Simpulan (setelah mencoba sendiri dulu!)"):
        st.markdown("""
        <div class="success-card">
        <b>Simpulan Bilangan Bulat:</b><br>
        ✅ Bilangan bulat terdiri dari: <b>bilangan negatif (...,−3,−2,−1), nol (0), bilangan positif (1,2,3,...)</b><br>
        ✅ Semakin ke <b>kanan</b> pada garis bilangan → nilainya semakin <b>besar</b><br>
        ✅ Semakin ke <b>kiri</b> pada garis bilangan → nilainya semakin <b>kecil</b><br>
        ✅ <b>Invers penjumlahan</b> dari a adalah −a, karena a + (−a) = 0
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# KP 2 — KALKULATOR OPERASI
# ══════════════════════════════════════════
elif tab_choice == "🔧 KP 2 — Kalkulator Operasi":
    st.markdown("## 🔧 Kegiatan Pembelajaran 2: Operasi Hitung Bilangan Bulat")

    # STIMULATION
    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik</div>
        <div class="fase-text">
        Sebuah klub sepak bola <b>melepaskan 3 pemain buruk</b>. Artinya: <b>(−3) × (−1) = ?</b><br>
        Apakah performa tim naik atau turun? Mengapa <b>(−3) × (−4) = +12</b>, bukan −12?<br><br>
        <b>❓ Apa yang menentukan tanda hasil perkalian dan pembagian bilangan bulat?</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # PROBLEM STATEMENT
    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">② Problem Statement — Hipotesis</div>
        <div class="fase-text">
        Tuliskan hipotesismu di LKS sebelum bereksplorasi:<br>
        <i>"Menurutku, hasil perkalian dua bilangan negatif akan bernilai... karena..."</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">③ Data Collection — Eksplorasi Kalkulator</div>
        <div class="fase-text">Masukkan dua bilangan dan pilih operasi. Catat hasilnya di tabel LKS!</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### ⌨️ Masukkan Bilangan")
        a = st.number_input("Bilangan Pertama (a):", value=-6, step=1, min_value=-999, max_value=999)
        op = st.selectbox("Operasi:", ["+  (Penjumlahan)", "−  (Pengurangan)", "×  (Perkalian)", "÷  (Pembagian)"])
        b = st.number_input("Bilangan Kedua (b):", value=-4, step=1, min_value=-999, max_value=999)

        op_sym = op[0]
        if op_sym == "+":
            hasil = a + b
        elif op_sym == "−":
            hasil = a - b
        elif op_sym == "×":
            hasil = a * b
        else:
            if b == 0:
                st.error("⚠️ Tidak bisa membagi dengan nol!")
                hasil = None
            else:
                hasil = a // b if a % b == 0 else a / b

    with col2:
        if hasil is not None:
            tanda = "➕ POSITIF" if hasil > 0 else ("➖ NEGATIF" if hasil < 0 else "⚪ NOL")
            warna = "#70AD47" if hasil > 0 else ("#C00000" if hasil < 0 else "#7F7F7F")
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#1A3C6E,#2E75B6);color:white;
                        border-radius:16px;padding:1.5rem;text-align:center;margin-top:1.5rem;
                        box-shadow:0 4px 15px rgba(26,60,110,0.3);">
                <div style="font-size:0.85rem;opacity:0.8;margin-bottom:0.3rem;">Kalimat Matematika</div>
                <div style="font-size:1.5rem;font-weight:800;margin-bottom:0.5rem;">
                    ({a:+d}) {op_sym} ({b:+d})
                </div>
                <div style="font-size:0.85rem;opacity:0.8;">Hasil</div>
                <div style="font-size:3.5rem;font-weight:800;line-height:1.1;">
                    {hasil if isinstance(hasil, int) else f"{hasil:.4f}"}
                </div>
                <div style="margin-top:0.5rem;background:{warna};color:white;
                            padding:5px 15px;border-radius:20px;display:inline-block;font-weight:700;">
                    {tanda}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Penjelasan tanda
            if op_sym in ["×", "÷"]:
                ta = "positif" if a > 0 else ("negatif" if a < 0 else "nol")
                tb = "positif" if b > 0 else ("negatif" if b < 0 else "nol")
                th = "positif" if (hasil is not None and hasil > 0) else ("negatif" if (hasil is not None and hasil < 0) else "nol")
                st.markdown(f"""
                <div class="warning-card" style="margin-top:0.8rem;">
                <b>🔍 Analisis Tanda:</b><br>
                a = {a:+d} → <b>{ta}</b><br>
                b = {b:+d} → <b>{tb}</b><br>
                Tanda sama? <b>{'YA → hasil POSITIF ✅' if (a>0 and b>0) or (a<0 and b<0) else 'TIDAK → hasil NEGATIF 🔴'}</b>
                </div>
                """, unsafe_allow_html=True)

    # Tabel Eksplorasi Sistematis
    st.markdown("---")
    st.markdown("""
    <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
        <div class="fase-label" style="color:#7030A0;">④ Data Processing — Tabel Pola Tanda</div>
        <div class="fase-text">Coba semua kombinasi berikut menggunakan kalkulator di atas, lalu catat di LKS!</div>
    </div>
    """, unsafe_allow_html=True)

    cols3 = st.columns(2)
    with cols3[0]:
        st.markdown("**Pola Perkalian (×)**")
        pola_kali = [
            ("(+6) × (+4)", 6*4, "+", "+"),
            ("(+6) × (−4)", 6*(-4), "+", "−"),
            ("(−6) × (+4)", (-6)*4, "−", "+"),
            ("(−6) × (−4)", (-6)*(-4), "−", "−"),
        ]
        tbl = '<table style="width:100%;border-collapse:collapse;font-size:0.85rem;">'
        tbl += '<tr style="background:#1A3C6E;color:white;"><th style="padding:6px;border:1px solid #ccc;">Operasi</th><th style="padding:6px;border:1px solid #ccc;">Hasil</th><th style="padding:6px;border:1px solid #ccc;">Tanda Hasil</th></tr>'
        for op_str, res, ta, tb in pola_kali:
            t_res = "POSITIF ✅" if res > 0 else "NEGATIF 🔴"
            c_res = "#70AD47" if res > 0 else "#C00000"
            tbl += f'<tr><td style="padding:6px;border:1px solid #ccc;">{op_str}</td><td style="padding:6px;border:1px solid #ccc;text-align:center;font-weight:bold;">{res}</td><td style="padding:6px;border:1px solid #ccc;text-align:center;color:{c_res};font-weight:bold;">{t_res}</td></tr>'
        tbl += "</table>"
        st.markdown(tbl, unsafe_allow_html=True)

    with cols3[1]:
        st.markdown("**Pola Pembagian (÷)**")
        pola_bagi = [
            ("(+24) ÷ (+6)", 24//6, "+", "+"),
            ("(+24) ÷ (−6)", 24//(-6), "+", "−"),
            ("(−24) ÷ (+6)", (-24)//6, "−", "+"),
            ("(−24) ÷ (−6)", (-24)//(-6), "−", "−"),
        ]
        tbl2 = '<table style="width:100%;border-collapse:collapse;font-size:0.85rem;">'
        tbl2 += '<tr style="background:#1A3C6E;color:white;"><th style="padding:6px;border:1px solid #ccc;">Operasi</th><th style="padding:6px;border:1px solid #ccc;">Hasil</th><th style="padding:6px;border:1px solid #ccc;">Tanda Hasil</th></tr>'
        for op_str, res, ta, tb in pola_bagi:
            t_res = "POSITIF ✅" if res > 0 else "NEGATIF 🔴"
            c_res = "#70AD47" if res > 0 else "#C00000"
            tbl2 += f'<tr><td style="padding:6px;border:1px solid #ccc;">{op_str}</td><td style="padding:6px;border:1px solid #ccc;text-align:center;font-weight:bold;">{res}</td><td style="padding:6px;border:1px solid #ccc;text-align:center;color:{c_res};font-weight:bold;">{t_res}</td></tr>'
        tbl2 += "</table>"
        st.markdown(tbl2, unsafe_allow_html=True)

    # GENERALIZATION
    st.markdown("---")
    with st.expander("⑥ 💡 Lihat Simpulan Aturan Tanda (setelah mencoba sendiri dulu!)"):
        st.markdown("""
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;text-align:center;">
        <tr style="background:#1A3C6E;color:white;">
            <th style="padding:10px;border:1px solid #ccc;">Tanda a</th>
            <th style="padding:10px;border:1px solid #ccc;">Operasi</th>
            <th style="padding:10px;border:1px solid #ccc;">Tanda b</th>
            <th style="padding:10px;border:1px solid #ccc;">Tanda Hasil</th>
        </tr>
        <tr style="background:#EEFFEE;"><td>+</td><td>× atau ÷</td><td>+</td><td style="color:#70AD47;font-weight:bold;">POSITIF (+)</td></tr>
        <tr><td>−</td><td>× atau ÷</td><td>−</td><td style="color:#70AD47;font-weight:bold;">POSITIF (+)</td></tr>
        <tr style="background:#FFEEEE;"><td>+</td><td>× atau ÷</td><td>−</td><td style="color:#C00000;font-weight:bold;">NEGATIF (−)</td></tr>
        <tr style="background:#FFEEEE;"><td>−</td><td>× atau ÷</td><td>+</td><td style="color:#C00000;font-weight:bold;">NEGATIF (−)</td></tr>
        </table>
        <br>
        <div class="success-card">
        <b>✅ Aturan Emas:</b><br>
        🟢 <b>Tanda SAMA</b> (++ atau −−) → hasil <b>POSITIF</b><br>
        🔴 <b>Tanda BERBEDA</b> (+− atau −+) → hasil <b>NEGATIF</b>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# KP 3 — POHON FAKTOR & FPB/KPK
# ══════════════════════════════════════════
elif tab_choice == "🌳 KP 3 — Pohon Faktor & FPB/KPK":
    st.markdown("## 🌳 Kegiatan Pembelajaran 3: Faktor Bilangan Bulat")

    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik</div>
        <div class="fase-text">
        Ibu memiliki <b>24 kue nastar</b> dan <b>36 kue coklat</b>. Ia ingin membagi ke beberapa piring
        dengan jumlah <b>sama rata dan tidak ada sisa</b>.<br><br>
        <b>❓ Berapa paling banyak piring yang bisa digunakan? Berapa kue di setiap piring?</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    tab3a, tab3b = st.tabs(["🌳 Pohon Faktor", "📊 FPB & KPK"])

    # ── TAB POHON FAKTOR
    with tab3a:
        st.markdown("""
        <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
            <div class="fase-label" style="color:#70AD47;">③ Data Collection — Eksplorasi Pohon Faktor</div>
            <div class="fase-text">Masukkan bilangan, amati pohon faktor yang terbentuk, dan catat di LKS!</div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])
        with col1:
            n = st.number_input("Masukkan bilangan (2–200):", min_value=2, max_value=200, value=36, step=1)

            # Faktorisasi prima
            def faktorisasi_prima(n):
                faktor = {}
                d = 2
                while d * d <= n:
                    while n % d == 0:
                        faktor[d] = faktor.get(d, 0) + 1
                        n //= d
                    d += 1
                if n > 1:
                    faktor[n] = faktor.get(n, 0) + 1
                return faktor

            def semua_faktor(n):
                f = []
                for i in range(1, n + 1):
                    if n % i == 0:
                        f.append(i)
                return f

            fp = faktorisasi_prima(n)
            faktor_prima_str = " × ".join([f"{p}{'⁰¹²³⁴⁵⁶⁷⁸⁹'[e] if e > 1 else ''}" if e == 1 else f"{p}^{e}" for p, e in fp.items()])
            faktor_prima_str_clean = " × ".join([f"{p}" + (f"^{e}" if e > 1 else "") for p, e in fp.items()])
            semua_f = semua_faktor(n)
            is_prima = len(semua_f) == 2

            st.markdown(f"""
            <div style="background:#1A3C6E;color:white;border-radius:12px;padding:1rem;text-align:center;margin:0.5rem 0;">
                <div style="font-size:0.8rem;opacity:0.8;">Faktorisasi Prima</div>
                <div style="font-size:1.6rem;font-weight:800;margin:0.3rem 0;">{n} = {faktor_prima_str_clean}</div>
                <div style="font-size:0.8rem;opacity:0.8;">Bilangan Prima? {'✅ YA' if is_prima else '❌ BUKAN'}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="info-card">
            <b>Semua Faktor dari {n}:</b><br>
            <span style="font-size:0.9rem;">{{{', '.join(map(str, semua_f))}}}</span><br>
            <b>Banyak faktor:</b> {len(semua_f)}
            </div>
            """, unsafe_allow_html=True)

        with col2:
            # Visualisasi Pohon Faktor
            def get_pohon_nodes(n_asli, n, x=0, y=0, dx=1.5, level=0, nodes=None, edges=None):
                if nodes is None:
                    nodes = []
                if edges is None:
                    edges = []
                node_id = len(nodes)
                is_p = faktorisasi_prima(n) == {n: 1} or n == 1
                nodes.append((node_id, x, y, str(n), is_p, level == 0))
                if is_p or n == 1:
                    return nodes, edges
                d = 2
                while d < n:
                    if n % d == 0:
                        other = n // d
                        # child 1: d
                        cid1 = len(nodes)
                        nodes, edges = get_pohon_nodes(n, d, x - dx / (level + 1), y - 1.2,
                                                       dx * 0.6, level + 1, nodes, edges)
                        edges.append((node_id, cid1))
                        # child 2: other
                        cid2 = len(nodes)
                        nodes, edges = get_pohon_nodes(n, other, x + dx / (level + 1), y - 1.2,
                                                       dx * 0.6, level + 1, nodes, edges)
                        edges.append((node_id, cid2))
                        break
                return nodes, edges

            nodes_list, edges_list = get_pohon_nodes(n, n)

            fig2, ax2 = plt.subplots(figsize=(8, 5))
            ax2.axis("off")
            fig2.patch.set_facecolor('#FAFBFF')
            ax2.set_facecolor('#FAFBFF')

            for nid1, nid2 in edges_list:
                x1, y1 = nodes_list[nid1][1], nodes_list[nid1][2]
                x2, y2 = nodes_list[nid2][1], nodes_list[nid2][2]
                ax2.plot([x1, x2], [y1, y2], '-', color='#AAAAAA', lw=1.5, zorder=1)

            for nid, x, y, label, is_p, is_root in nodes_list:
                color = "#1A3C6E" if is_root else ("#70AD47" if is_p else "#2E75B6")
                size = 600 if is_root else 400
                ax2.scatter([x], [y], s=size, c=color, zorder=3, edgecolors='white', linewidths=2)
                ax2.text(x, y, label, ha='center', va='center', fontsize=10 if is_root else 9,
                        color='white', fontweight='bold', zorder=4)
                if is_p and not is_root:
                    ax2.text(x, y - 0.5, "prima", ha='center', va='top', fontsize=7,
                            color="#70AD47", fontstyle='italic')

            ax2.set_title(f"Pohon Faktor dari {n}   =   {faktor_prima_str_clean}",
                         pad=10, fontsize=10, color="#1A3C6E", fontweight='bold')

            legend_els = [
                mpatches.Patch(facecolor='#1A3C6E', label='Bilangan asal'),
                mpatches.Patch(facecolor='#70AD47', label='Faktor prima'),
                mpatches.Patch(facecolor='#2E75B6', label='Faktor komposit'),
            ]
            ax2.legend(handles=legend_els, loc='lower right', fontsize=8)
            st.pyplot(fig2)
            plt.close()

    # ── TAB FPB & KPK
    with tab3b:
        st.markdown("""
        <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
            <div class="fase-label" style="color:#70AD47;">③ Data Collection — Eksplorasi FPB & KPK</div>
            <div class="fase-text">Masukkan dua bilangan, amati proses faktorisasi prima, dan catat pola FPB & KPK di LKS!</div>
        </div>
        """, unsafe_allow_html=True)

        cola, colb = st.columns(2)
        with cola:
            bil1 = st.number_input("Bilangan Pertama:", min_value=2, max_value=200, value=24, step=1)
        with colb:
            bil2 = st.number_input("Bilangan Kedua:", min_value=2, max_value=200, value=36, step=1)

        fp1 = faktorisasi_prima(bil1)
        fp2 = faktorisasi_prima(bil2)
        semua_p = sorted(set(list(fp1.keys()) + list(fp2.keys())))

        # FPB & KPK
        fpb = 1
        kpk = 1
        for p in semua_p:
            e1 = fp1.get(p, 0)
            e2 = fp2.get(p, 0)
            fpb *= p ** min(e1, e2)
            kpk *= p ** max(e1, e2)

        col1, col2, col3 = st.columns([1.2, 1, 1])
        with col1:
            fp1_str = " × ".join([f"{p}" + (f"^{e}" if e > 1 else "") for p, e in fp1.items()])
            fp2_str = " × ".join([f"{p}" + (f"^{e}" if e > 1 else "") for p, e in fp2.items()])
            st.markdown(f"""
            <div class="info-card">
            <b>Faktorisasi Prima:</b><br><br>
            <span style="color:#1A3C6E;font-size:1rem;font-weight:700;">{bil1}</span>
            = {fp1_str}<br>
            <span style="color:#1A3C6E;font-size:1rem;font-weight:700;">{bil2}</span>
            = {fp2_str}
            </div>
            """, unsafe_allow_html=True)

            # Tabel perbandingan
            tbl = '<table style="width:100%;border-collapse:collapse;font-size:0.82rem;margin-top:0.5rem;">'
            tbl += f'<tr style="background:#1A3C6E;color:white;"><th style="padding:6px;border:1px solid #ccc;">Prima</th><th style="padding:6px;border:1px solid #ccc;">Pangkat di {bil1}</th><th style="padding:6px;border:1px solid #ccc;">Pangkat di {bil2}</th><th style="padding:6px;border:1px solid #ccc;">min (FPB)</th><th style="padding:6px;border:1px solid #ccc;">max (KPK)</th></tr>'
            for p in semua_p:
                e1 = fp1.get(p, 0)
                e2 = fp2.get(p, 0)
                tbl += f'<tr style="text-align:center;"><td style="padding:5px;border:1px solid #ccc;font-weight:bold;">{p}</td><td style="padding:5px;border:1px solid #ccc;">{e1 if e1>0 else "—"}</td><td style="padding:5px;border:1px solid #ccc;">{e2 if e2>0 else "—"}</td><td style="padding:5px;border:1px solid #ccc;color:#C00000;font-weight:bold;">{min(e1,e2) if min(e1,e2)>0 else "—"}</td><td style="padding:5px;border:1px solid #ccc;color:#70AD47;font-weight:bold;">{max(e1,e2)}</td></tr>'
            tbl += "</table>"
            st.markdown(tbl, unsafe_allow_html=True)

        with col2:
            fpb_str = " × ".join([f"{p}" + (f"^{min(fp1.get(p,0),fp2.get(p,0))}" if min(fp1.get(p,0),fp2.get(p,0)) > 1 else "") for p in semua_p if min(fp1.get(p,0),fp2.get(p,0)) > 0])
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#C00000,#E74C3C);color:white;
                        border-radius:14px;padding:1.2rem;text-align:center;">
                <div style="font-size:0.8rem;opacity:0.9;margin-bottom:0.3rem;">FPB({bil1}, {bil2})</div>
                <div style="font-size:0.75rem;opacity:0.8;">= {fpb_str}</div>
                <div style="font-size:3rem;font-weight:800;">{fpb}</div>
                <div style="font-size:0.8rem;opacity:0.8;margin-top:0.3rem;">
                Faktor prima SAMA, pangkat TERKECIL</div>
            </div>
            <div class="danger-card" style="margin-top:0.6rem;font-size:0.85rem;">
            <b>Artinya:</b> {bil1} dan {bil2} sama-sama bisa dibagi {fpb}.<br>
            Dalam soal kue: bisa dibagi ke <b>{fpb} piring</b>!
            </div>
            """, unsafe_allow_html=True)

        with col3:
            kpk_str = " × ".join([f"{p}" + (f"^{max(fp1.get(p,0),fp2.get(p,0))}" if max(fp1.get(p,0),fp2.get(p,0)) > 1 else "") for p in semua_p if max(fp1.get(p,0),fp2.get(p,0)) > 0])
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#70AD47,#27AE60);color:white;
                        border-radius:14px;padding:1.2rem;text-align:center;">
                <div style="font-size:0.8rem;opacity:0.9;margin-bottom:0.3rem;">KPK({bil1}, {bil2})</div>
                <div style="font-size:0.75rem;opacity:0.8;">= {kpk_str}</div>
                <div style="font-size:3rem;font-weight:800;">{kpk}</div>
                <div style="font-size:0.8rem;opacity:0.8;margin-top:0.3rem;">
                SEMUA faktor prima, pangkat TERBESAR</div>
            </div>
            <div class="success-card" style="margin-top:0.6rem;font-size:0.85rem;">
            <b>Artinya:</b> Kelipatan terkecil yang habis dibagi {bil1} dan {bil2} sekaligus.<br>
            Dalam soal lampu: lampu berkedip bersamaan tiap <b>{kpk} satuan waktu</b>!
            </div>
            """, unsafe_allow_html=True)

        with st.expander("⑥ 💡 Lihat Simpulan FPB & KPK"):
            st.markdown("""
            <div class="success-card">
            <b>✅ Cara Menentukan FPB dan KPK dengan Faktorisasi Prima:</b><br><br>
            🔴 <b>FPB</b> = kalikan faktor prima yang <b>SAMA</b> dengan pangkat <b>TERKECIL</b><br>
            🟢 <b>KPK</b> = kalikan <b>SEMUA</b> faktor prima dengan pangkat <b>TERBESAR</b><br><br>
            💡 <b>Mudah diingat:</b><br>
            FPB → irisan (sama-sama ada) → pangkat kecil<br>
            KPK → gabungan (semua diambil) → pangkat besar
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# SOAL LATIHAN INTERAKTIF
# ══════════════════════════════════════════
elif tab_choice == "📝 Soal Latihan Interaktif":
    st.markdown("## 📝 Soal Latihan Interaktif")
    st.markdown("""
    <div class="warning-card">
    <b>📌 Petunjuk:</b> Kerjakan soal-soal berikut secara mandiri dan jujur.
    Gunakan kalkulator digital di tab sebelumnya hanya untuk <b>verifikasi</b>, bukan langsung menekan tombol!
    Waktu pengerjaan: ±45 menit.
    </div>
    """, unsafe_allow_html=True)

    if 'skor' not in st.session_state:
        st.session_state.skor = 0
    if 'jawab' not in st.session_state:
        st.session_state.jawab = {}

    soal_list = [
        {
            "no": 1, "tipe": "PG", "kp": "KP 1",
            "soal": "Bilangan mana yang memiliki nilai lebih besar?",
            "konteks": "Suhu kota A = −8°C dan suhu kota B = −3°C.",
            "pilihan": ["A. −8 karena angkanya lebih besar", "B. −3 karena letaknya lebih ke kanan pada garis bilangan",
                       "C. Keduanya sama", "D. −8 karena berarti lebih dingin"],
            "jawaban": "B", "pembahasan": "Pada garis bilangan, −3 terletak lebih ke KANAN dibanding −8. Semakin ke kanan → nilai semakin besar. Jadi −3 > −8."
        },
        {
            "no": 2, "tipe": "PG", "kp": "KP 1",
            "soal": "Invers penjumlahan dari −17 adalah ...",
            "konteks": "",
            "pilihan": ["A. 17", "B. −17", "C. 1/17", "D. 0"],
            "jawaban": "A", "pembahasan": "Invers penjumlahan dari −17 adalah +17, karena (−17) + (+17) = 0."
        },
        {
            "no": 3, "tipe": "PG", "kp": "KP 2",
            "soal": "Hasil dari (−8) × (−5) + (−4) × 3 adalah ...",
            "konteks": "",
            "pilihan": ["A. −52", "B. 28", "C. 52", "D. −28"],
            "jawaban": "B", "pembahasan": "(−8)×(−5) = +40 (tanda sama → positif); (−4)×3 = −12 (tanda berbeda → negatif); 40 + (−12) = 28."
        },
        {
            "no": 4, "tipe": "PG", "kp": "KP 2",
            "soal": "Suhu awal gudang beku adalah −15°C. Suhu turun lagi 8°C, lalu naik 5°C. Suhu akhir gudang adalah ...",
            "konteks": "💡 Ini soal literasi finansial tentang perubahan suhu.",
            "pilihan": ["A. −18°C", "B. −28°C", "C. 18°C", "D. 28°C"],
            "jawaban": "A", "pembahasan": "−15 + (−8) + 5 = −15 − 8 + 5 = −23 + 5 = −18°C."
        },
        {
            "no": 5, "tipe": "PG", "kp": "KP 3",
            "soal": "Faktorisasi prima dari 72 adalah ...",
            "konteks": "",
            "pilihan": ["A. 2² × 3²", "B. 2³ × 3²", "C. 2² × 3³", "D. 2⁴ × 3"],
            "jawaban": "B", "pembahasan": "72 = 2×36 = 2×2×18 = 2×2×2×9 = 2×2×2×3×3 = 2³ × 3²."
        },
        {
            "no": 6, "tipe": "PG", "kp": "KP 3",
            "soal": "FPB dari 48 dan 60 adalah ...",
            "konteks": "",
            "pilihan": ["A. 6", "B. 12", "C. 24", "D. 240"],
            "jawaban": "B", "pembahasan": "48 = 2⁴ × 3; 60 = 2² × 3 × 5. FPB = faktor prima sama, pangkat terkecil = 2² × 3 = 4 × 3 = 12."
        },
        {
            "no": 7, "tipe": "Isian", "kp": "KP 2",
            "soal": "Urutkan bilangan berikut dari yang TERKECIL ke TERBESAR:",
            "konteks": "Bilangan: −10, 5, −3, 0, 8, −7, 4",
            "pilihan": None,
            "jawaban": "−10, −7, −3, 0, 4, 5, 8",
            "pembahasan": "Pada garis bilangan dari kiri ke kanan: −10 < −7 < −3 < 0 < 4 < 5 < 8."
        },
        {
            "no": 8, "tipe": "Isian", "kp": "KP 3",
            "soal": "KPK dari 8, 12, dan 15 adalah ...",
            "konteks": "💡 Gunakan Tab Pohon Faktor untuk membantu!",
            "pilihan": None,
            "jawaban": "120",
            "pembahasan": "8 = 2³; 12 = 2² × 3; 15 = 3 × 5. KPK = 2³ × 3 × 5 = 8 × 3 × 5 = 120."
        },
    ]

    skor_total = 0
    sudah_submit = st.session_state.get('submitted', False)

    for soal in soal_list:
        kp_color = {"KP 1": "#2E75B6", "KP 2": "#70AD47", "KP 3": "#ED7D31"}[soal["kp"]]
        st.markdown(f"""
        <div style="border:1px solid #E0E0E0;border-radius:12px;padding:1rem 1.2rem;margin:0.8rem 0;
                    border-left:5px solid {kp_color};">
        <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;">
            <span style="background:{kp_color};color:white;padding:2px 10px;border-radius:20px;
                         font-size:0.78rem;font-weight:700;">{soal['kp']}</span>
            <span style="background:#F0F0F0;padding:2px 10px;border-radius:20px;
                         font-size:0.78rem;font-weight:700;">{soal['tipe']}</span>
            <b>Soal {soal['no']}</b>
        </div>
        <div style="font-size:0.95rem;font-weight:600;">{soal['soal']}</div>
        {f'<div style="background:#FFF8E6;padding:0.5rem 0.8rem;border-radius:8px;margin-top:0.4rem;font-size:0.88rem;color:#8B6914;">{soal["konteks"]}</div>' if soal["konteks"] else ""}
        </div>
        """, unsafe_allow_html=True)

        key = f"soal_{soal['no']}"
        if soal["tipe"] == "PG":
            jawab = st.radio("Pilih jawaban:", soal["pilihan"],
                            key=key, label_visibility="collapsed",
                            index=None if key not in st.session_state.jawab else
                            soal["pilihan"].index(st.session_state.jawab.get(key, soal["pilihan"][0])))
            if jawab:
                st.session_state.jawab[key] = jawab
        else:
            jawab = st.text_input("Jawaban kamu:", key=key,
                                 placeholder="Tulis jawabanmu di sini...")
            if jawab:
                st.session_state.jawab[key] = jawab

        if sudah_submit and key in st.session_state.jawab:
            j = st.session_state.jawab[key]
            benar = (soal["tipe"] == "PG" and j and j.startswith(soal["jawaban"])) or \
                    (soal["tipe"] == "Isian" and soal["jawaban"].lower() in j.lower())
            if benar:
                skor_total += 1
                st.markdown(f'<div class="success-card" style="font-size:0.85rem;">✅ <b>BENAR!</b> {soal["pembahasan"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="danger-card" style="font-size:0.85rem;">❌ <b>Belum tepat.</b> Jawaban: <b>{soal["jawaban"]}</b>. {soal["pembahasan"]}</div>', unsafe_allow_html=True)

        st.markdown("")

    col_btn1, col_btn2 = st.columns([1, 3])
    with col_btn1:
        if st.button("✅ Submit & Lihat Nilai", type="primary", use_container_width=True):
            st.session_state.submitted = True
            st.rerun()
    with col_btn2:
        if st.button("🔄 Reset Jawaban", use_container_width=True):
            st.session_state.submitted = False
            st.session_state.jawab = {}
            st.rerun()

    if sudah_submit:
        persen = skor_total / len(soal_list) * 100
        emoji = "🏆" if persen >= 80 else ("👍" if persen >= 60 else "💪")
        warna_nilai = "#70AD47" if persen >= 80 else ("#ED7D31" if persen >= 60 else "#C00000")
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#1A3C6E,#2E75B6);color:white;
                    border-radius:16px;padding:1.5rem 2rem;text-align:center;margin-top:1rem;">
            <div style="font-size:1.1rem;opacity:0.9;">Nilai Akhir {emoji}</div>
            <div style="font-size:4rem;font-weight:800;color:{warna_nilai};">{persen:.0f}</div>
            <div style="font-size:1rem;opacity:0.8;">{skor_total} dari {len(soal_list)} soal benar</div>
            <div style="margin-top:0.8rem;font-size:0.9rem;">
            {'🏆 Excellent! Kamu sudah sangat memahami bilangan bulat!' if persen>=80 else ('👍 Bagus! Pelajari lagi bagian yang masih salah.' if persen>=60 else '💪 Semangat! Eksplorasi lebih dalam dengan kalkulator digital!')}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # REFLEKSI
        st.markdown("---")
        st.markdown("### 🔍 Refleksi Penggunaan Kalkulator Digital Streamlit")
        r1 = st.text_area("1. Fitur apa yang paling membantumu memahami bilangan bulat? Mengapa?",
                          placeholder="Tuliskan refleksimu di sini...", height=80)
        r2 = st.text_area("2. Apa yang kamu temukan saat bereksplorasi dengan kalkulator digital yang tidak kamu temukan dari buku?",
                          placeholder="Tuliskan refleksimu di sini...", height=80)
        r3 = st.text_area("3. Bagaimana perasaanmu belajar matematika dengan kalkulator digital ini?",
                          placeholder="Tuliskan refleksimu di sini...", height=80)
        if r1 or r2 or r3:
            st.markdown('<div class="success-card">✅ Terima kasih atas refleksimu! Salin ke LKS-mu.</div>', unsafe_allow_html=True)
