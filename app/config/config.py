import os

TITLE="Health Engine"
DESCRIPTION="System that combines artificial intelligence (AI) techniques, specifically leveraging the capabilities of Pandas AI"

API_KEY_CHAT_GPT= os.getenv("API_KEY_CHAT_GPT")

#Mongo
CONNECTION_MONGO = "mongodb://localhost:27017/"


EXAMPLE_DB = {
  "pengguna_id":"1",
  "nama_lengkap":"Budi Setiawan",
  "attributes": {
    "usia": "30 tahun",
    "jenis_kelamin": "laki-laki",
    "berat_badan": "75 kg",
    "tinggi_badan": "180 cm",
    "tekanan_darah": "120/80 mmHg",
    "denyut_jantung": "70 bpm",
    "tingkat_kolesterol": "180 mg/dL",
    "tingkat_gula_darah": "95 mg/dL",
    "tingkat_aktivitas": "sedang",
    "riwayat_keluarga": "tidak ada",
    "kondisi_terkini": ["hipertensi", "diabetes"],
    "alergi": ["serbuk sari", "kacang tanah"],
    "obat-obatan": ["lisinopril", "metformin"],
    "faktor_gaya_hidup": ["perokok"],
    "preferensi_diet": ["vegetarian"],
    "preferensi_olahraga": ["lari", "yoga"],
    "kualitas_tidur": "7 jam",
    "tingkat_stres": "sedang",
    "tingkat_vitamin_d": "30 ng/mL",
    "fungsi_tiroid": "normal",
    "fungsi_ginjal": "sehat",
    "fungsi_hati": "normal",
    "kapasitas_paru-paru": "3.5 L",
    "kepadatan_tulang": "normal",
    "ketajaman_penglihatan": "20/20",
    "ketajaman_pendengaran": "normal",
    "status_sistem_kekebalan": "kuat",
    "kesejahteraan_mental": "baik",
    "konsumsi_alkohol": "sesekali",
    "konsumsi_kafein": "sedang",
    "tingkat_hidrasi": "cukup",
    "paparan_matahari": "sedang",
    "dukungan_emosional": "kuat",
    "interaksi_sosial": "aktif",
    "paparan_lingkungan": "minim"
  }
}
