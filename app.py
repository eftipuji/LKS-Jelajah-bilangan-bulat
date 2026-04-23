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
    Penulis: Efti Puji Lestari
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# HALAMAN BERANDA
# ══════════════════════════════════════════
if tab_choice == "🏠 Beranda":
    st.markdown("## 👋 Selamat Datang, Penjelajah Matematika!")
# ... (kode selanjutnya dibiarkan sama seperti asli)
