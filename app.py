import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os

# ============================================================================
# MANUAL 50 QUESTIONS LIST - FORMAT PERINTAH
# ============================================================================
MANUAL_QUESTIONS = [
    # A. ANALISIS DESKRIPTIF & EXPLORASI (1-15)
    "Hitung total penjualan secara keseluruhan",
    "Tampilkan rata-rata penjualan per bulan", 
    "Cari produk terlaris berdasarkan jumlah transaksi",
    "Identifikasi pelanggan dengan pembelian terbanyak",
    "Hitung persentase pertumbuhan penjualan bulanan",
    "Temukan nilai maksimum dan minimum dari setiap kolom numerik",
    "Analisis distribusi penjualan berdasarkan kategori produk",
    "Hitung rasio antara pelanggan baru dan pelanggan lama",
    "Buat summary statistik lengkap dari dataset",
    "Hitung total transaksi per kota atau region",
    "Cari korelasi antara variabel numerik dalam dataset", 
    "Deteksi outlier dalam data penjualan",
    "Analisis tren penjualan berdasarkan timeline",
    "Identifikasi variabel yang paling berpengaruh terhadap target",
    "Bandingkan rata-rata penjualan antar kategori produk",
    
    # B. DATA PREPARATION & CLEANING (16-25)
    "Baca dan tampilkan struktur dataset yang diupload",
    "Hapus data duplikat dari dataset",
    "Ganti nama kolom yang tidak deskriptif", 
    "Ubah tipe data kolom yang tidak sesuai",
    "Filter data berdasarkan kondisi tertentu",
    "Gabungkan dataset dengan file external jika ada",
    "Buat kolom baru hasil perhitungan atau transformasi",
    "Lakukan encoding pada variabel kategorikal",
    "Normalisasi data numerik untuk analisis lebih lanjut", 
    "Ekspor dataset hasil cleaning ke file baru",
    
    # C. VISUALISASI DATA (26-40)
    "Buat grafik batang untuk penjualan per produk",
    "Buat grafik garis trend penjualan overtime", 
    "Buat pie chart distribusi kategori produk",
    "Buat heatmap korelasi antar variabel numerik",
    "Buat scatter plot hubungan dua variabel numerik",
    "Buat histogram distribusi nilai numerik",
    "Buat box plot untuk analisis outlier",
    "Buat bar chart horizontal perbandingan kategori", 
    "Buat stacked bar chart komposisi penjualan",
    "Buat area chart perkembangan kumulatif",
    "Buat multiple subplot dalam satu layout",
    "Buat dashboard interaktif sederhana",
    "Ekspor visualisasi sebagai file gambar", 
    "Buat laporan visual otomatis dari dataset",
    "Buat comparative analysis chart antar segment",
    
    # D. ANALISIS LANJUTAN & INSIGHT (41-50)
    "Buat segmentasi pelanggan berdasarkan RFM",
    "Analisis pola pembelian pelanggan tertentu", 
    "Identifikasi seasonality dalam data penjualan",
    "Buat forecasting sederhana untuk periode berikutnya",
    "Analisis customer lifetime value",
    "Identifikasi produk yang sering dibeli bersama",
    "Buat cohort analysis retention pelanggan", 
    "Analisis sales funnel dan conversion rate",
    "Buat performance benchmark antar periode",
    "Generate actionable insights dari data"
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
    st.sidebar.markdown("### 50 Perintah Data Analyst")
    st.sidebar.markdown("---")
    
    # Main content
    st.title("📊 InsightFlow Analytics Dashboard")
    st.markdown("Selamat datang! Upload file data Anda dan pilih perintah analisis dari 50 perintah yang tersedia.")
    
    # Tab layout
    tab1, tab2, tab3 = st.tabs(["📋 Daftar Perintah", "📁 Upload Data", "🔍 Analisis Data"])
    
    with tab1:
        show_questions_tab()
    
    with tab2:
        show_upload_tab()
    
    with tab3:
        show_analysis_tab()

def show_questions_tab():
    """Display the 50 commands"""
    st.header("📋 Daftar 50 Perintah Analisis Data")
    st.markdown("""
    **Kategori Perintah:**
    - **1-15:** Analisis Deskriptif & Eksplorasi
    - **16-25:** Data Preparation & Cleaning  
    - **26-40:** Visualisasi Data
    - **41-50:** Analisis Lanjutan & Insight
    """)
    
    # Display commands in expandable sections
    categories = {
        "Analisis Deskriptif & Eksplorasi (1-15)": MANUAL_QUESTIONS[0:15],
        "Data Preparation & Cleaning (16-25)": MANUAL_QUESTIONS[15:25],
        "Visualisasi Data (26-40)": MANUAL_QUESTIONS[25:40],
        "Analisis Lanjutan & Insight (41-50)": MANUAL_QUESTIONS[40:50]
    }
    
    for category, commands in categories.items():
        with st.expander(f"📂 {category}"):
            for i, command in enumerate(commands, start=1):
                st.write(f"**{i}.** {command}")

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
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                st.metric("🔢 Numerik", len(numeric_cols))
            with col4:
                categorical_cols = df.select_dtypes(include=['object']).columns
                st.metric("📝 Kategorikal", len(categorical_cols))
            
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
            
            # Store column types for analysis
            st.session_state.numeric_columns = numeric_cols.tolist()
            st.session_state.categorical_columns = categorical_cols.tolist()
            st.session_state.date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()
            
        except Exception as e:
            st.error(f"❌ Error membaca file: {str(e)}")
    else:
        st.info("📁 Silakan upload file CSV atau Excel untuk memulai analisis")
        if 'file_uploaded' in st.session_state:
            st.session_state.file_uploaded = False

def show_analysis_tab():
    """Handle data analysis"""
    st.header("🔍 Analisis Data")
    
    if not st.session_state.get('file_uploaded', False):
        st.warning("⚠️ Silakan upload file data terlebih dahulu di tab 'Upload Data'")
        return
    
    df = st.session_state.df
    
    # Command selection
    st.subheader("🎯 Pilih Perintah Analisis")
    selected_command = st.selectbox(
        "Pilih perintah:",
        options=MANUAL_QUESTIONS,
        index=0,
        help="Pilih salah satu dari 50 perintah analisis data"
    )
    
    # Additional parameters based on command type
    st.subheader("⚙️ Parameter Analisis")
    
    command_lower = selected_command.lower()
    
    # Dynamic parameter selection based on command type
    if any(word in command_lower for word in ['hitung', 'tampilkan', 'rata', 'average', 'max', 'min', 'tren', 'total']):
        # Commands about numeric data
        if st.session_state.numeric_columns:
            numeric_column = st.selectbox(
                "Pilih kolom numerik untuk dianalisis:",
                options=st.session_state.numeric_columns
            )
        else:
            numeric_column = None
            st.warning("❌ Tidak ada kolom numerik dalam dataset")
    
    if any(word in command_lower for word in ['cari', 'identifikasi', 'terlaris', 'terbanyak', 'top', 'distribusi', 'kelompok', 'kategori']):
        # Commands about categorical data
        if st.session_state.categorical_columns:
            categorical_column = st.selectbox(
                "Pilih kolom kategorikal untuk dianalisis:",
                options=st.session_state.categorical_columns
            )
        else:
            categorical_column = None
            st.warning("❌ Tidak ada kolom kategorikal dalam dataset")
    
    if any(word in command_lower for word in ['korelasi']):
        # Correlation analysis needs multiple numeric columns
        if len(st.session_state.numeric_columns) >= 2:
            st.info("🔗 Analisis korelasi akan membandingkan semua kolom numerik")
        else:
            st.warning("❌ Diperlukan minimal 2 kolom numerik untuk analisis korelasi")
    
    # Analysis button
    if st.button("🚀 Jalankan Perintah", type="primary", use_container_width=True):
        with st.spinner("🔄 Menjalankan analisis..."):
            try:
                # Perform analysis based on command type
                result = perform_analysis(df, selected_command, 
                                        numeric_column if 'numeric_column' in locals() else None,
                                        categorical_column if 'categorical_column' in locals() else None)
                
                # Display results
                st.subheader("📊 Hasil Analisis")
                st.success(f"**Perintah:** {selected_command}")
                
                if 'answer' in result:
                    st.info(f"**Hasil:** {result['answer']}")
                
                if 'insights' in result:
                    st.subheader("💡 Insights")
                    for insight in result['insights']:
                        st.write(f"• {insight}")
                
                if 'data' in result and result['data']:
                    st.subheader("📈 Data Hasil")
                    st.json(result['data'])
                
                if 'recommendations' in result:
                    st.subheader("🎯 Rekomendasi")
                    for rec in result['recommendations']:
                        st.write(f"• {rec}")
                    
            except Exception as e:
                st.error(f"❌ Error dalam analisis: {str(e)}")

def perform_analysis(df, command, numeric_col=None, categorical_col=None):
    """Perform analysis based on command type"""
    command_lower = command.lower()
    
    # Basic pattern matching for different command types
    if any(word in command_lower for word in ['hitung total', 'total']):
        return handle_total_analysis(df, command, numeric_col)
    elif any(word in command_lower for word in ['rata-rata', 'rata', 'average']):
        return handle_average_analysis(df, command, numeric_col)
    elif any(word in command_lower for word in ['maksimum', 'minimum', 'max', 'min']):
        return handle_minmax_analysis(df, command, numeric_col)
    elif any(word in command_lower for word in ['terlaris', 'terbanyak', 'top']):
        return handle_top_analysis(df, command, categorical_col)
    elif any(word in command_lower for word in ['tren', 'trend']):
        return handle_trend_analysis(df, command, numeric_col)
    elif any(word in command_lower for word in ['korelasi']):
        return handle_correlation_analysis(df, command)
    elif any(word in command_lower for word in ['distribusi']):
        return handle_distribution_analysis(df, command, categorical_col, numeric_col)
    elif any(word in command_lower for word in ['summary', 'statistik']):
        return handle_summary_analysis(df, command)
    elif any(word in command_lower for word in ['nilai hilang', 'missing']):
        return handle_missing_analysis(df, command)
    elif any(word in command_lower for word in ['duplikat', 'duplikasi']):
        return handle_duplicate_analysis(df, command)
    elif any(word in command_lower for word in ['outlier']):
        return handle_outlier_analysis(df, command, numeric_col)
    elif any(word in command_lower for word in ['visualisasi', 'grafik', 'chart']):
        return handle_visualization_commands(df, command, numeric_col, categorical_col)
    elif any(word in command_lower for word in ['segmentasi', 'rfm']):
        return handle_segmentation_analysis(df, command)
    else:
        return handle_general_analysis(df, command)

def handle_total_analysis(df, command, numeric_col):
    """Handle total-related commands"""
    if numeric_col:
        total = df[numeric_col].sum()
        return {
            'answer': f'✅ Total {numeric_col}: {total:,.2f}',
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
            'answer': '❌ Tidak ada kolom numerik yang dipilih untuk analisis total',
            'insights': ['Silakan pilih kolom numerik di parameter analisis'],
            'recommendations': ['Pilih kolom numerik seperti "sales", "price", "quantity" dll.']
        }

def handle_average_analysis(df, command, numeric_col):
    """Handle average-related commands"""
    if numeric_col:
        avg = df[numeric_col].mean()
        median = df[numeric_col].median()
        return {
            'answer': f'✅ Rata-rata {numeric_col}: {avg:,.2f}',
            'insights': [
                f'📈 Rata-rata {numeric_col}: {avg:,.2f}',
                f'📊 Median: {median:,.2f}',
                f'🎯 Nilai tertinggi: {df[numeric_col].max():,.2f}',
                f'📉 Nilai terendah: {df[numeric_col].min():,.2f}',
                f'📋 Standar deviasi: {df[numeric_col].std():,.2f}',
                f'🔢 Jumlah data: {len(df)} baris'
            ],
            'data': {
                'average': float(avg),
                'median': float(median),
                'max': float(df[numeric_col].max()),
                'min': float(df[numeric_col].min()),
                'std': float(df[numeric_col].std()),
                'count': len(df)
            }
        }
    else:
        return {
            'answer': '❌ Tidak ada kolom numerik yang dipilih untuk analisis rata-rata',
            'insights': ['Silakan pilih kolom numerik di parameter analisis'],
            'recommendations': ['Pilih kolom numerik seperti "sales", "price", "quantity" dll.']
        }

def handle_minmax_analysis(df, command, numeric_col):
    """Handle maximum/minimum analysis"""
    if numeric_col:
        max_val = df[numeric_col].max()
        min_val = df[numeric_col].min()
        max_idx = df[numeric_col].idxmax()
        min_idx = df[numeric_col].idxmin()
        
        return {
            'answer': f'✅ Nilai maksimum {numeric_col}: {max_val:,.2f}, minimum: {min_val:,.2f}',
            'insights': [
                f'📈 Nilai maksimum {numeric_col}: {max_val:,.2f}',
                f'📉 Nilai minimum {numeric_col}: {min_val:,.2f}',
                f'📊 Rentang nilai: {max_val - min_val:,.2f}',
                f'📋 Rata-rata: {df[numeric_col].mean():,.2f}',
                f'🔍 Maksimum pada baris: {max_idx + 1}',
                f'🔍 Minimum pada baris: {min_idx + 1}'
            ],
            'data': {
                'max_value': float(max_val),
                'min_value': float(min_val),
                'range': float(max_val - min_val),
                'average': float(df[numeric_col].mean()),
                'max_index': int(max_idx),
                'min_index': int(min_idx)
            }
        }
    else:
        return {
            'answer': '❌ Tidak ada kolom numerik yang dipilih untuk analisis maksimum/minimum',
            'insights': ['Silakan pilih kolom numerik di parameter analisis']
        }

def handle_top_analysis(df, command, categorical_col):
    """Handle top-related commands"""
    if categorical_col:
        top_items = df[categorical_col].value_counts().head(10)
        total_categories = df[categorical_col].nunique()
        
        insights = [
            f'🏆 Top 10 {categorical_col}:',
            f'🥇 1. {top_items.index[0]} ({top_items.iloc[0]}x)',
            f'🥈 2. {top_items.index[1]} ({top_items.iloc[1]}x)',
            f'🥉 3. {top_items.index[2]} ({top_items.iloc[2]}x)',
            f'📊 Total kategori: {total_categories}',
            f'🔢 Total data points: {len(df)}'
        ]
        
        # Add more items if available
        if len(top_items) > 3:
            for i in range(3, min(6, len(top_items))):
                insights.append(f'{i+1}. {top_items.index[i]} ({top_items.iloc[i]}x)')
        
        return {
            'answer': f'✅ Top {categorical_col}: {top_items.index[0]} dengan {top_items.iloc[0]} occurrences',
            'insights': insights,
            'data': top_items.to_dict()
        }
    else:
        return {
            'answer': '❌ Tidak ada kolom kategorikal yang dipilih untuk analisis top items',
            'insights': ['Silakan pilih kolom kategorikal di parameter analisis'],
            'recommendations': ['Pilih kolom seperti "product", "category", "region" dll.']
        }

def handle_trend_analysis(df, command, numeric_col):
    """Handle trend-related commands"""
    date_cols = df.select_dtypes(include=['datetime64']).columns
    
    if len(date_cols) > 0 and numeric_col:
        date_col = date_cols[0]
        # Simple trend analysis
        if hasattr(df[date_col], 'dt'):
            # Monthly trend
            monthly_trend = df.groupby(df[date_col].dt.to_period('M'))[numeric_col].mean()
            
            insights = [
                f'📈 Tren {numeric_col} per bulan:',
                f'📅 Periode analisis: {len(monthly_trend)} bulan',
                f'📊 Rata-rata overall: {df[numeric_col].mean():,.2f}',
                f'🔍 Kolom tanggal: {date_col}',
                f'📈 Nilai tertinggi: {monthly_trend.max():,.2f}',
                f'📉 Nilai terendah: {monthly_trend.min():,.2f}'
            ]
            
            return {
                'answer': f'✅ Tren {numeric_col} berdasarkan waktu berhasil dianalisis',
                'insights': insights,
                'data': monthly_trend.to_dict()
            }
        else:
            return {
                'answer': f'❌ Kolom {date_col} bukan tipe datetime yang valid',
                'insights': ['Pastikan kolom tanggal dalam format yang benar']
            }
    
    return {
        'answer': '❌ Tidak cukup data untuk analisis tren',
        'insights': [
            'Diperlukan kolom tanggal dan kolom numerik',
            f'Kolom tanggal tersedia: {len(date_cols)}',
            f'Kolom numerik: {numeric_col if numeric_col else "Tidak dipilih"}'
        ]
    }

def handle_correlation_analysis(df, command):
    """Handle correlation analysis"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) >= 2:
        correlation_matrix = df[numeric_cols].corr()
        
        # Get top correlation pairs
        correlations = []
        for i in range(len(numeric_cols)):
            for j in range(i+1, len(numeric_cols)):
                corr = correlation_matrix.iloc[i, j]
                if not np.isnan(corr):
                    correlations.append({
                        'variables': f"{numeric_cols[i]} vs {numeric_cols[j]}",
                        'correlation': float(corr),
                        'strength': 'Kuat' if abs(corr) > 0.7 else 'Sedang' if abs(corr) > 0.3 else 'Lemah'
                    })
        
        # Sort by absolute correlation
        correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)
        
        top_corr = correlations[0] if correlations else None
        
        insights = [
            f'📈 Ditemukan {len(correlations)} pasangan korelasi',
            f'🔗 Korelasi terkuat: {top_corr["variables"]} ({top_corr["correlation"]:.3f}) - {top_corr["strength"]}' if top_corr else 'Tidak ada korelasi yang signifikan',
            f'📊 Total variabel numerik: {len(numeric_cols)}',
            f'🔢 Skala korelasi: -1 (negatif sempurna) hingga +1 (positif sempurna)'
        ]
        
        return {
            'answer': f'✅ Analisis korelasi antara {len(numeric_cols)} variabel numerik',
            'insights': insights,
            'data': {
                'top_correlations': correlations[:10],
                'total_variables': len(numeric_cols),
                'correlation_matrix_available': True
            }
        }
    else:
        return {
            'answer': '❌ Tidak cukup kolom numerik untuk analisis korelasi',
            'insights': ['Dibutuhkan minimal 2 kolom numerik untuk analisis korelasi'],
            'recommendations': ['Pastikan dataset memiliki minimal 2 kolom numerik']
        }

def handle_distribution_analysis(df, command, categorical_col, numeric_col):
    """Handle distribution analysis"""
    if categorical_col and numeric_col:
        distribution = df.groupby(categorical_col)[numeric_col].agg(['count', 'sum', 'mean', 'std']).round(2)
        
        insights = [
            f'📊 Distribusi {numeric_col} berdasarkan {categorical_col}',
            f'📈 Total kategori: {len(distribution)}',
            f'🔢 Rata-rata overall: {df[numeric_col].mean():,.2f}',
            f'📋 Kategori dengan nilai tertinggi: {distribution["mean"].idxmax()} ({distribution["mean"].max():,.2f})'
        ]
        
        return {
            'answer': f'✅ Distribusi {numeric_col} berdasarkan {categorical_col} berhasil dianalisis',
            'insights': insights,
            'data': distribution.to_dict()
        }
    else:
        return {
            'answer': '❌ Diperlukan kolom kategorikal dan numerik untuk analisis distribusi',
            'insights': ['Silakan pilih kolom kategorikal dan numerik di parameter analisis']
        }

def handle_summary_analysis(df, command):
    """Handle summary statistics"""
    numeric_summary = df.describe()
    categorical_summary = df.select_dtypes(include=['object']).describe()
    
    insights = [
        f'📊 Dataset summary: {df.shape[0]} baris, {df.shape[1]} kolom',
        f'🔢 Kolom numerik: {len(df.select_dtypes(include=[np.number]).columns)}',
        f'📝 Kolom kategorikal: {len(df.select_dtypes(include=["object"]).columns)}',
        f'📅 Kolom tanggal: {len(df.select_dtypes(include=["datetime64"]).columns)}',
        f'📉 Nilai hilang: {df.isnull().sum().sum()} ({df.isnull().sum().sum()/(len(df)*len(df.columns))*100:.2f}%)'
    ]
    
    return {
        'answer': '✅ Summary statistik dataset berhasil dihasilkan',
        'insights': insights,
        'data': {
            'shape': list(df.shape),
            'numeric_columns': df.select_dtypes(include=[np.number]).columns.tolist(),
            'categorical_columns': df.select_dtypes(include=['object']).columns.tolist(),
            'missing_values': df.isnull().sum().to_dict(),
            'data_types': df.dtypes.astype(str).to_dict()
        }
    }

def handle_missing_analysis(df, command):
    """Handle missing values analysis"""
    missing_data = df.isnull().sum()
    missing_percentage = (missing_data / len(df)) * 100
    total_missing = missing_data.sum()
    
    insights = [
        f'📊 Total nilai hilang: {total_missing}',
        f'📉 Persentase nilai hilang: {total_missing/(len(df)*len(df.columns))*100:.2f}%',
        f'🔍 Kolom dengan nilai hilang terbanyak: {missing_data.idxmax()} ({missing_data.max()} nilai)'
    ]
    
    # Add details for columns with missing values
    for col in missing_data[missing_data > 0].index:
        insights.append(f'• {col}: {missing_data[col]} nilai hilang ({missing_percentage[col]:.2f}%)')
    
    return {
        'answer': f'✅ Analisis nilai hilang: {total_missing} nilai hilang ditemukan',
        'insights': insights,
        'data': {
            'total_missing': int(total_missing),
            'missing_by_column': missing_data[missing_data > 0].to_dict(),
            'missing_percentage': missing_percentage[missing_percentage > 0].to_dict()
        }
    }

def handle_duplicate_analysis(df, command):
    """Handle duplicate analysis"""
    duplicate_rows = df.duplicated().sum()
    duplicate_percentage = (duplicate_rows / len(df)) * 100
    
    insights = [
        f'🔄 Baris duplikat: {duplicate_rows}',
        f'📊 Persentase duplikat: {duplicate_percentage:.2f}%',
        f'🔢 Total baris: {len(df)}'
    ]
    
    if duplicate_rows > 0:
        insights.append('💡 Disarankan untuk menghapus baris duplikat untuk analisis yang lebih akurat')
    
    return {
        'answer': f'✅ Ditemukan {duplicate_rows} baris duplikat',
        'insights': insights,
        'data': {
            'duplicate_rows': int(duplicate_rows),
            'duplicate_percentage': float(duplicate_percentage),
            'total_rows': len(df)
        }
    }

def handle_outlier_analysis(df, command, numeric_col):
    """Handle outlier analysis"""
    if numeric_col:
        Q1 = df[numeric_col].quantile(0.25)
        Q3 = df[numeric_col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[numeric_col] < lower_bound) | (df[numeric_col] > upper_bound)]
        outlier_count = len(outliers)
        outlier_percentage = (outlier_count / len(df)) * 100
        
        insights = [
            f'🎯 Outlier pada {numeric_col}: {outlier_count}',
            f'📊 Persentase outlier: {outlier_percentage:.2f}%',
            f'📈 Batas bawah: {lower_bound:.2f}',
            f'📉 Batas atas: {upper_bound:.2f}',
            f'📋 Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}'
        ]
        
        return {
            'answer': f'✅ Ditemukan {outlier_count} outlier pada {numeric_col}',
            'insights': insights,
            'data': {
                'outlier_count': outlier_count,
                'outlier_percentage': float(outlier_percentage),
                'bounds': {'lower': float(lower_bound), 'upper': float(upper_bound)},
                'quartiles': {'Q1': float(Q1), 'Q3': float(Q3), 'IQR': float(IQR)}
            }
        }
    else:
        return {
            'answer': '❌ Tidak ada kolom numerik yang dipilih untuk analisis outlier',
            'insights': ['Silakan pilih kolom numerik di parameter analisis']
        }

def handle_visualization_commands(df, command, numeric_col, categorical_col):
    """Handle visualization-related commands"""
    command_lower = command.lower()
    
    if any(word in command_lower for word in ['grafik batang', 'bar chart']):
        if categorical_col and numeric_col:
            return {
                'answer': f'✅ Data untuk grafik batang {categorical_col} vs {numeric_col} siap',
                'insights': [
                    f'📊 Grafik batang: {categorical_col} vs {numeric_col}',
                    f'📈 Total kategori: {df[categorical_col].nunique()}',
                    f'🔢 Rata-rata {numeric_col}: {df[numeric_col].mean():,.2f}',
                    '💡 Gunakan data di bawah untuk membuat visualisasi di Excel/Tableau'
                ],
                'data': df.groupby(categorical_col)[numeric_col].mean().to_dict()
            }
    
    elif any(word in command_lower for word in ['grafik garis', 'line chart', 'tren']):
        date_cols = df.select_dtypes(include=['datetime64']).columns
        if len(date_cols) > 0 and numeric_col:
            date_col = date_cols[0]
            monthly_trend = df.groupby(df[date_col].dt.to_period('M'))[numeric_col].mean()
            return {
                'answer': f'✅ Data untuk grafik garis tren {numeric_col} siap',
                'insights': [
                    f'📈 Grafik garis: Tren {numeric_col} over time',
                    f'📅 Periode: {len(monthly_trend)} bulan',
                    f'🔍 Kolom tanggal: {date_col}',
                    '💡 Data trend bulanan tersedia untuk visualisasi'
                ],
                'data': monthly_trend.to_dict()
            }
    
    return {
        'answer': '✅ Perintah visualisasi diterima',
        'insights': [
            '📊 Data untuk visualisasi telah dipersiapkan',
            '💡 Gunakan data di bawah untuk membuat visualisasi di tools favorit Anda',
            '🎨 Recommended tools: Excel, Tableau, Python matplotlib/seaborn'
        ],
        'data': {
            'numeric_columns': st.session_state.numeric_columns,
            'categorical_columns': st.session_state.categorical_columns,
            'date_columns': st.session_state.date_columns
        }
    }

def handle_segmentation_analysis(df, command):
    """Handle segmentation analysis"""
    # Simple RFM-like segmentation if we have customer data
    customer_cols = [col for col in df.columns if any(word in col.lower() for word in ['customer', 'pelanggan', 'user', 'id'])]
    amount_cols = [col for col in df.columns if any(word in col.lower() for word in ['amount', 'total', 'price', 'sales'])]
    
    if customer_cols and amount_cols:
        customer_col = customer_cols[0]
        amount_col = amount_cols[0]
        
        # Simple customer segmentation
        customer_stats = df.groupby(customer_col).agg({
            amount_col: ['count', 'sum', 'mean']
        }).round(2)
        
        insights = [
            f'👥 Total pelanggan unik: {len(customer_stats)}',
            f'💰 Total transaksi: {len(df)}',
            f'📊 Rata-rata transaksi per pelanggan: {customer_stats[(amount_col, 'count')].mean():.1f}',
            f'🎯 Pelanggan terbaik: {customer_stats[(amount_col, 'sum')].idxmax()}'
        ]
        
        return {
            'answer': '✅ Segmentasi pelanggan berhasil dianalisis',
            'insights': insights,
            'data': customer_stats.head(10).to_dict()
        }
    
    return {
        'answer': '❌ Data tidak cukup untuk analisis segmentasi pelanggan',
        'insights': [
            'Diperlukan kolom pelanggan/customer dan kolom amount/penjualan',
            f'Kolom customer ditemukan: {len(customer_cols)}',
            f'Kolom amount ditemukan: {len(amount_cols)}'
        ]
    }

def handle_general_analysis(df, command):
    """General analysis fallback with more specific responses"""
    command_lower = command.lower()
    
    # More specific responses for common command types
    if any(word in command_lower for word in ['prediksi', 'model', 'machine learning', 'forecasting']):
        return {
            'answer': '✅ Permintaan analisis prediktif diterima',
            'insights': [
                '🤖 Analisis prediktif membutuhkan modeling machine learning',
                '📊 Untuk analisis dasar, gunakan perintah deskriptif',
                '💡 Rekomendasi: Coba per
