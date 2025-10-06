# Prediksi Uber Drive Booking Cancel

## Repository Outline

Berikut adalah isi utama repository:
```
1. P1M2_jyotis_sugata.ipynb         - Notebook utama proses EDA, feature engineering, modeling, evaluasi, dan kesimpulan
2. P1M2_jyotis_sugata_inf.ipynb     - Notebook untuk inferensi model (prediksi booking cancel pada data baru)
3. P1M2_jyotis_sugata_conceptual.txt - Jawaban dari 3 pertanyaan pada
4. description.md                   - Penjelasan singkat project ini
5. url.txt                          - Link dataset, model, dan deployment
6. Dockerfile                       - Docker untuk deployment HuggingFace Spaces
7. requirements.txt                 - Semua module yang dibutuhkan untuk deployment
8. streamlit_app.py                 - Halaman utama dari Deployment HuggingFace Spaces
9. eda.py                           - Halaman hasil visualisasi eda
10. predict.py                      - Halaman inferencing untuk user bisa melakukan demo prediksi dengan model yang telah dibuat
```

## Problem Background
Tingkat pembatalan perjalanan (booking cancellation) menjadi masalah utama pada layanan ride-hailing seperti Uber. Pembatalan menyebabkan hilangnya potensi pendapatan, menurunkan kepuasan pelanggan, serta menambah beban operasional. Dengan memanfaatkan data historis booking, perusahaan dapat membangun model prediksi untuk mengidentifikasi kemungkinan pembatalan sehingga dapat dilakukan intervensi lebih awal.


## Project Output
- Model machine learning (XGBoost) untuk memprediksi kemungkinan booking cancel.
- Notebook analisis data, EDA, dan modeling.
- File model siap deploy (.pkl).
- Notebook inferensi untuk prediksi data baru.
- Link deployment model (HuggingFace Spaces).

## Data
- Sumber: [Kaggle Uber Ride Analytics Dashboard](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard/data)
- Jumlah data: ±150.000 baris, 21 kolom
- Karakteristik: Terdapat kolom kategorikal (lokasi, vehicle type, status), numerik (waktu tunggu, jarak, nilai booking), dan beberapa kolom dengan missing value.
- Penanganan: Missing value diisi dengan rata-rata/median berdasarkan kombinasi lokasi, outlier dianalisis dan diputuskan untuk dipertahankan.

## Method
- Exploratory Data Analysis (EDA) untuk memahami pola pembatalan.
- Feature engineering & selection.
- Penanganan missing value dan outlier.
- Modeling dengan beberapa algoritma: Decision Tree, KNN, SVM, Random Forest, XGBoost.
- Evaluasi model menggunakan recall, precision, dan ROC-AUC.
- Hyperparameter tuning (GridSearchCV) pada XGBoost.
- Model terbaik dipilih berdasarkan kebutuhan bisnis (prioritas recall).

## Stacks
- **Python** (Jupyter Notebook)
- **Pandas**, **NumPy** (manipulasi data)
- **Matplotlib**, **Seaborn** (visualisasi)
- **Scikit-learn** (preprocessing, modeling, evaluasi)
- **XGBoost** (model utama)
- **Pickle** (model saving)
- **HuggingFace Spaces** (deployment)

## Reference
- [Dataset Kaggle](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard/data)
- [Model file (Google Drive)](https://drive.google.com/file/d/1Svc6hWnXX_REhnTghj4xabXgI4LYcDKf/view?usp=sharing)
- [Deployment (HuggingFace Spaces)](https://huggingface.co/spaces/jyotis00/deployment)

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)