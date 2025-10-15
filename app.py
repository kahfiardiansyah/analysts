import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os

# ============================================================================
# MANUAL 50 QUESTIONS LIST
# ============================================================================
MANUAL_QUESTIONS = [
    # A. Analisis Deskriptif (1-10)
    "Bagaimana cara melihat total penjualan secara keseluruhan?",
    "Bagaimana menghitung rata-rata penjualan per bulan?",
    "Bagaimana mencari produk terlaris?",
    "Bagaimana mengetahui pelanggan dengan pembelian terbanyak?",
    "Bagaimana menghitung persentase pertumbuhan penjualan dari bulan ke bulan?",
    "Bagaimana mencari nilai maksimum dan minimum dari kolom tertentu?",
    "Bagaimana menghitung distribusi penjualan berdasarkan kategori produk?",
    "Bagaimana menghitung rasio pelanggan baru dan pelanggan lama?",
    "Bagaimana membuat summary statistik dari dataset?",
    "Bagaimana menghitung total transaksi per kota atau cabang?",
    
    # B. Analisis Eksploratif (11-20)
    "Bagaimana mencari korelasi antara dua variabel?",
    "Bagaimana mendeteksi outlier dalam data penjualan?",
    "Bagaimana melihat tren penjualan berdasarkan waktu?",
    "Bagaimana mengetahui variabel yang paling berpengaruh terhadap target?",
    "Bagaimana menghitung perbedaan rata-rata antar dua kelompok?",
    "Bagaimana mengetahui pola pembelian pelanggan tertentu?",
    "Bagaimana mengelompokkan pelanggan berdasarkan perilaku belanja?",
    "Bagaimana melihat distribusi data dalam bentuk visual?",
    "Bagaimana mendeteksi nilai hilang dalam dataset?",
    "Bagaimana melakukan imputasi untuk nilai yang hilang?",
    
    # C. Analisis Prediktif (21-30)
    "Bagaimana membuat prediksi penjualan untuk bulan depan?",
    "Bagaimana membuat model regresi sederhana?",
    "Bagaimana memprediksi pelanggan yang akan churn?",
    "Bagaimana memilih model machine learning terbaik?",
    "Bagaimana membagi dataset menjadi data train dan test?",
    "Bagaimana melakukan validasi silang?",
    "Bagaimana menghitung metrik evaluasi?",
    "Bagaimana menampilkan importance dari tiap fitur?",
    "Bagaimana menyimpan dan memuat ulang model?",
    "Bagaimana membuat prediksi otomatis dari input user?",
    
    # D. Data Preparation (31-40)
    "Bagaimana membaca file CSV atau Excel dengan pandas?",
    "Bagaimana menghapus duplikasi data?",
    "Bagaimana mengganti nama kolom dalam dataframe?",
    "Bagaimana mengubah tipe data kolom?",
    "Bagaimana memfilter data berdasarkan kondisi tertentu?",
    "Bagaimana menggabungkan dua dataset?",
    "Bagaimana menambahkan kolom baru hasil perhitungan?",
    "Bagaimana melakukan encoding pada variabel kategorikal?",
    "Bagaimana melakukan normalisasi atau standarisasi data numerik?",
    "Bagaimana menyimpan dataset hasil olahan menjadi file baru?",
    
    # E. Visualisasi Data (41-50)
    "Bagaimana membuat grafik batang penjualan per produk?",
    "Bagaimana membuat grafik garis untuk tren waktu?",
    "Bagaimana membuat pie chart untuk proporsi kategori produk?",
    "Bagaimana membuat heatmap untuk korelasi antar variabel?",
    "Bagaimana membuat scatter plot antara dua variabel numerik?",
    "Bagaimana menambahkan label dan judul pada grafik?",
    "Bagaimana menampilkan beberapa grafik dalam satu layout?",
    "Bagaimana menyimpan grafik sebagai file gambar?",
    "Bagaimana membuat dashboard interaktif sederhana?",
    "Bagaimana membuat visualisasi otomatis dari dataset?"
]

# ============================================================================
# STREAMLIT APP
# ============================================================================
def main():
    st.set_page_config(
        page_title="InsightFlow Analytics", 
        page_icon="📊", 
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Sidebar
    st.sidebar.title("🎯 InsightFlow Analytics")
    st.sidebar.markdown("### 50 Pertanyaan Data Analyst")
    st.sidebar.markdown("---")
    
    # Main content
    st.title("📊 InsightFlow Analytics Dashboard")
    st.markdown("Selamat datang! Upload file data Anda dan pilih pertanyaan analitis dari 50 pertanyaan yang tersedia.")
    
    # Tab layout
    tab1, tab2, tab3 = st.tabs(["📋 Pertanyaan", "📁 Upload Data", "🔍 Analisis"])
    
    with tab1:
        show_questions_tab()
    
    with tab2:
        show_upload_tab()
    
    with tab3:
        show_analysis_tab()

def show_questions_tab():
    """Display the 50 questions"""
    st.header("📋 Daftar 50 Pertanyaan Analitis")
    st.markdown("""
    **Kategori Pertanyaan:**
    - **1-10:** Analisis Deskriptif
    - **11-20:** Analisis Eksploratif  
    - **21-30:** Analisis Prediktif
    - **31-40:** Data Preparation
    - **41-50:** Visualisasi Data
    """)
    
    # Display questions in expandable sections
    categories = {
        "Analisis Deskriptif (1-10)": MANUAL_QUESTIONS[0:10],
        "Analisis Eksploratif (11-20)": MANUAL_QUESTIONS[10:20],
        "Analisis Prediktif (21-30)": MANUAL_QUESTIONS[20:30],
        "Data Preparation (31-40)": MANUAL_QUESTIONS[30:40],
        "Visualisasi Data (41-50)": MANUAL_QUESTIONS[40:50]
    }
    
    for category, questions in categories.items():
        with st.expander(f"📂 {category}"):
            for i, question in enumerate(questions, start=1):
                st.write(f"**{i}.** {question}")

def show_upload_tab():
    """Handle file upload and display"""
    st.header("📁 Upload File Data")
    
    uploaded_file = st.file_uploader(
        "Pilih file CSV atau Excel", 
        type=['csv', 'xlsx'],
        help="Upload file data Anda untuk dianalisis"
    )
    
    if uploaded_file is not None:
        try:
            # Read file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success(f"✅ File berhasil diupload!")
            
            # Display file info
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📊 Baris", df.shape[0])
            with col2:
                st.metric("📈 Kolom", df.shape[1])
            with col3:
                st.metric("🔢 Numerik", len(df.select_dtypes(include=[np.number]).columns))
            with col4:
                st.metric("📝 Kategorikal", len(df.select_dtypes(include=['object']).columns))
            
            # Data preview
            st.subheader("👀 Preview Data")
            st.dataframe(df.head(10), use_container_width=True)
            
            # Column info
            st.subheader("📋 Informasi Kolom")
            col_info = pd.DataFrame({
                'Kolom': df.columns,
                'Tipe Data': df.dtypes,
                'Nilai Unik': [df[col].nunique() for col in df.columns],
                'Nilai Hilang': [df[col].isnull().sum() for col in df.columns]
            })
            st.dataframe(col_info, use_container_width=True)
            
            # Data quality
            st.subheader("📊 Kualitas Data")
            missing_percentage = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
            duplicated_rows = df.duplicated().sum()
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("📉 Nilai Hilang", f"{missing_percentage:.2f}%")
            with col2:
                st.metric("🔄 Baris Duplikat", duplicated_rows)
            
            # Store dataframe in session state
            st.session_state.df = df
            st.session_state.file_uploaded = True
            st.session_state.filename = uploaded_file.name
            
        except Exception as e:
            st.error(f"❌ Error membaca file: {str(e)}")
    else:
        st.info("📁 Silakan upload file CSV atau Excel untuk memulai analisis")
        st.session_state.file_uploaded = False

def show_analysis_tab():
    """Handle data analysis"""
    st.header("🔍 Analisis Data")
    
    if not st.session_state.get('file_uploaded', False):
        st.warning("⚠️ Silakan upload file data terlebih dahulu di tab 'Upload Data'")
        return
    
    df = st.session_state.df
    
    # Question selection
    st.subheader("🎯 Pilih Pertanyaan Analitis")
    selected_question = st.selectbox(
        "Pilih pertanyaan:",
        options=MANUAL_QUESTIONS,
        index=0,
        help="Pilih salah satu dari 50 pertanyaan analitis"
    )
    
    # Additional parameters
    st.subheader("⚙️ Parameter Analisis")
    col1, col2 = st.columns(2)
    
    with col1:
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            numeric_column = st.selectbox(
                "Pilih kolom numerik:",
                options=numeric_columns
            )
        else:
            numeric_column = None
            st.warning("Tidak ada kolom numerik dalam dataset")
    
    with col2:
        categorical_columns = df.select_dtypes(include=['object']).columns
        if len(categorical_columns) > 0:
            categorical_column = st.selectbox(
                "Pilih kolom kategorikal:",
                options=categorical_columns
            )
        else:
            categorical_column = None
            st.warning("Tidak ada kolom kategorikal dalam dataset")
    
    # Analysis button
    if st.button("🚀 Jalankan Analisis", type="primary"):
        with st.spinner("Menjalankan analisis..."):
            try:
                # Perform analysis based on question type
                result = perform_analysis(df, selected_question, numeric_column, categorical_column)
                
                # Display results
                st.subheader("📊 Hasil Analisis")
                st.success(f"**Pertanyaan:** {selected_question}")
                
                if 'answer' in result:
                    st.info(f"**Jawaban:** {result['answer']}")
                
                if 'insights' in result:
                    st.subheader("💡 Insights")
                    for insight in result['insights']:
                        st.write(f"• {insight}")
                
                if 'data' in result and result['data']:
                    st.subheader("📈 Data Hasil")
                    st.json(result['data'])
                    
            except Exception as e:
                st.error(f"❌ Error dalam analisis: {str(e)}")

def perform_analysis(df, question, numeric_col=None, categorical_col=None):
    """Perform analysis based on question type"""
    question_lower = question.lower()
    
    # Basic pattern matching for different question types
    if any(word in question_lower for word in ['total', 'jumlah', 'sum']):
        return handle_total_analysis(df, question, numeric_col)
    elif any(word in question_lower for word in ['rata', 'average', 'mean']):
        return handle_average_analysis(df, question, numeric_col)
    elif any(word in question_lower for word in ['terlaris', 'terbanyak', 'top']):
        return handle_top_analysis(df, question, categorical_col)
    elif any(word in question_lower for word in ['tren', 'trend', 'perkembangan']):
        return handle_trend_analysis(df, question, numeric_col)
    elif any(word in question_lower for word in ['korelasi', 'correlation']):
        return handle_correlation_analysis(df, question)
    else:
        return handle_general_analysis(df, question)

def handle_total_analysis(df, question, numeric_col):
    """Handle total-related questions"""
    if numeric_col:
        total = df[numeric_col].sum()
        return {
            'answer': f'Total {numeric_col}: {total:,.2f}',
            'insights': [
                f'📊 Total nilai pada kolom {numeric_col}: {total:,.2f}',
                f'🔢 Berdasarkan {len(df)} baris data',
                f'📈 Nilai rata-rata: {df[numeric_col].mean():,.2f}',
                f'🎯 Nilai tertinggi: {df[numeric_col].max():,.2f}',
                f'📉 Nilai terendah: {df[numeric_col].min():,.2f}'
            ],
            'data': {
                'total': float(total),
                'column': numeric_col,
                'rows_analyzed': len(df),
                'average': float(df[numeric_col].mean()),
                'max': float(df[numeric_col].max()),
                'min': float(df[numeric_col].min())
            }
        }
    else:
        return {
            'answer': 'Tidak ada kolom numerik yang dipilih',
            'insights': ['Silakan pilih kolom numerik untuk analisis total']
        }

def handle_average_analysis(df, question, numeric_col):
    """Handle average-related questions"""
    if numeric_col:
        avg = df[numeric_col].mean()
        return {
            'answer': f'Rata-rata {numeric_col}: {avg:,.2f}',
            'insights': [
                f'📈 Rata-rata {numeric_col}: {avg:,.2f}',
                f'📊 Nilai tertinggi: {df[numeric_col].max():,.2f}',
                f'📉 Nilai terendah: {df[numeric_col].min():,.2f}',
                f'📋 Standar deviasi: {df[numeric_col].std():,.2f}',
                f'🔢 Jumlah data: {len(df)} baris'
            ],
            'data': {
                'average': float(avg),
                'max': float(df[numeric_col].max()),
                'min': float(df[numeric_col].min()),
                'std': float(df[numeric_col].std()),
                'count': len(df)
            }
        }
    else:
        return handle_general_analysis(df, question)

def handle_top_analysis(df, question, categorical_col):
    """Handle top-related questions"""
    if categorical_col:
        top_items = df[categorical_col].value_counts().head(5)
        return {
            'answer': f'Top 5 {categorical_col}: {top_items.index[0]} ({top_items.iloc[0]} occurrences)',
            'insights': [
                f'🏆 {categorical_col} teratas: {top_items.index[0]}',
                f'📊 Distribusi: {len(top_items)} unique values',
                f'📈 Total categories: {df[categorical_col].nunique()}',
                f'🔢 Total data points: {len(df)}'
            ],
            'data': top_items.to_dict()
        }
    else:
        return handle_general_analysis(df, question)

def handle_trend_analysis(df, question, numeric_col):
    """Handle trend-related questions"""
    date_cols = df.select_dtypes(include=['datetime64']).columns
    
    if len(date_cols) > 0 and numeric_col:
        date_col = date_cols[0]
        # Simple trend analysis
        if hasattr(df[date_col], 'dt'):
            monthly_trend = df.groupby(df[date_col].dt.to_period('M'))[numeric_col].mean()
            return {
                'answer': f'Tren {numeric_col} berdasarkan waktu dianalisis',
                'insights': [
                    f'📈 Tren {numeric_col} per bulan berhasil dihitung',
                    f'📅 Periode: {len(monthly_trend)} bulan',
                    f'📊 Rata-rata overall: {df[numeric_col].mean():,.2f}',
                    f'🔍 Kolom tanggal: {date_col}'
                ],
                'data': monthly_trend.to_dict()
            }
    
    return handle_general_analysis(df, question)

def handle_correlation_analysis(df, question):
    """Handle correlation analysis"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) >= 2:
        correlation_matrix = df[numeric_cols].corr()
        # Get top correlation pairs
        correlations = []
        for i in range(len(numeric_cols)):
            for j in range(i+1, len(numeric_cols)):
                corr = correlation_matrix.iloc[i, j]
                correlations.append({
                    'variables': f"{numeric_cols[i]} vs {numeric_cols[j]}",
                    'correlation': float(corr)
                })
        
        # Sort by absolute correlation
        correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)
        
        return {
            'answer': f'Analisis korelasi antara {len(numeric_cols)} variabel numerik',
            'insights': [
                f'📈 Ditemukan {len(correlations)} pasangan korelasi',
                f'🔗 Korelasi terkuat: {correlations[0]["variables"]} ({correlations[0]["correlation"]:.3f})',
                f'📊 Total variabel numerik: {len(numeric_cols)}'
            ],
            'data': {
                'top_correlations': correlations[:5],
                'total_variables': len(numeric_cols)
            }
        }
    else:
        return {
            'answer': 'Tidak cukup kolom numerik untuk analisis korelasi',
            'insights': ['Dibutuhkan minimal 2 kolom numerik untuk analisis korelasi']
        }

def handle_general_analysis(df, question):
    """General analysis fallback"""
    return {
        'answer': f'Saya menganalisis: "{question}"',
        'insights': [
            f'📊 Dataset: {df.shape[0]} baris, {df.shape[1]} kolom',
            f'🔢 Kolom numerik: {len(df.select_dtypes(include=[np.number]).columns)}',
            f'📝 Kolom teks: {len(df.select_dtypes(include=["object"]).columns)}',
            f'📅 Kolom tanggal: {len(df.select_dtypes(include=["datetime64"]).columns)}',
            '💡 Gunakan pertanyaan spesifik untuk analisis lebih detail'
        ],
        'recommendations': [
            'Coba pertanyaan tentang total atau rata-rata',
            'Analisis distribusi data kategorikal',
            'Lihat tren data berdasarkan waktu',
            'Analisis korelasi antar variabel numerik'
        ],
        'dataset_info': {
            'shape': list(df.shape),
            'columns': df.columns.tolist(),
            'numeric_columns': df.select_dtypes(include=[np.number]).columns.tolist(),
            'categorical_columns': df.select_dtypes(include=['object']).columns.tolist()
        }
    }

# Initialize session state
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

# Run the app
if __name__ == "__main__":
    main()

# Footer
st.markdown("---")
st.markdown("### 🚀 InsightFlow Analytics - 50 Pertanyaan Data Analyst")
st.markdown("Dibuat dengan Streamlit | © 2024")
