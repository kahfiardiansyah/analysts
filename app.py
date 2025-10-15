# app.py - FIXED VERSION
from flask import Flask, jsonify, request
import os
from datetime import datetime
import pandas as pd
import numpy as np

# Try to import CORS, if not available, continue without it
try:
    from flask_cors import CORS
    CORS_AVAILABLE = True
except ImportError:
    CORS_AVAILABLE = False
    print("⚠️ flask_cors not available, running without CORS")

# ============================================================================
# SIMPLIFIED IMPORT - NO EXTERNAL DEPENDENCIES
# ============================================================================

# Set semua ke False karena file routes/services tidak ada
ANALYSIS_ROUTES_AVAILABLE = False
UPLOAD_ROUTES_AVAILABLE = False
VISUALIZATION_ROUTES_AVAILABLE = False
COMPLEX_ANALYSIS_AVAILABLE = False
DATA_ANALYZER_AVAILABLE = False
FILE_PROCESSOR_AVAILABLE = False

print("🔧 Running in standalone mode - using built-in features only")

# ============================================================================
# MANUAL 50 QUESTIONS LIST - FALLBACK
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
# FLASK APP INITIALIZATION
# ============================================================================
app = Flask(__name__)

if CORS_AVAILABLE:
    CORS(app)
else:
    print("🚨 Running without CORS - frontend may have connection issues")

# Config
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DATA_FOLDER'] = 'data'

# ============================================================================
# HEALTH CHECK & BASIC ENDPOINTS
# ============================================================================
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy 🎉',
        'message': 'InsightFlow API is running!',
        'timestamp': datetime.now().isoformat(),
        'features': {
            'analysis_routes': ANALYSIS_ROUTES_AVAILABLE,
            'upload_routes': UPLOAD_ROUTES_AVAILABLE,
            'visualization_routes': VISUALIZATION_ROUTES_AVAILABLE,
            'complex_analysis': COMPLEX_ANALYSIS_AVAILABLE,
            'data_analyzer': DATA_ANALYZER_AVAILABLE,
            'file_processor': FILE_PROCESSOR_AVAILABLE,
            '50_questions': True  # Selalu true karena manual fallback
        }
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to InsightFlow Analytics! 🚀',
        'version': '2.0 - Enhanced with 50 Questions',
        'endpoints': {
            'health': '/health (GET)',
            'upload': '/upload (POST)',
            'analyze': '/analyze (POST)',
            'visualize': '/visualize (POST)',
            'files': '/api/files (GET)',
            'questions': '/api/questions (GET)'
        }
    })

# ============================================================================
# QUESTIONS ENDPOINT - FIXED WITH MANUAL FALLBACK
# ============================================================================
@app.route('/api/questions', methods=['GET'])
def get_questions():
    """Get all available 50 questions - dengan manual fallback"""
    return jsonify({
        'success': True,
        'total_questions': len(MANUAL_QUESTIONS),
        'questions': MANUAL_QUESTIONS,
        'categories': {
            'Analisis Deskriptif': 'Pertanyaan 1-10 tentang data dasar',
            'Analisis Eksploratif': 'Pertanyaan 11-20 tentang pattern & insight', 
            'Analisis Prediktif': 'Pertanyaan 21-30 tentang prediksi & modeling',
            'Data Preparation': 'Pertanyaan 31-40 tentang cleaning data',
            'Visualisasi Data': 'Pertanyaan 41-50 tentang chart & grafik'
        },
        'source': 'manual_fallback',
        'message': '✅ 50 pertanyaan data analyst berhasil di-load!'
    }), 200

# ============================================================================
# CORE ANALYSIS ENDPOINT (WITH 50 QUESTIONS SUPPORT)
# ============================================================================
@app.route('/analyze', methods=['POST'])
def analyze_data():
    """Main analysis endpoint dengan 50 questions support"""
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({
                'success': False,
                'error': 'Please provide a question in JSON format',
                'example': {
                    'question': 'Bagaimana trend penjualan?',
                    'filename': 'optional_filename.csv'
                }
            }), 400
        
        question = data.get('question', '').strip()
        filename = data.get('filename', '')
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Question cannot be empty'
            }), 400
        
        # Load dataset jika filename provided
        df = None
        if filename:
            df = load_uploaded_file(filename)
            if df is None:
                return jsonify({
                    'success': False,
                    'error': f'File {filename} not found or unable to load'
                }), 404
        else:
            # Use sample data jika tidak ada file
            df = generate_sample_data()
        
        # Fallback simple analysis dengan question matching
        result = handle_simple_analysis(df, question)
        result['analysis_engine'] = 'simple_fallback'
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Analysis failed: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

def handle_simple_analysis(df, question):
    """Simple analysis fallback dengan basic question matching"""
    question_lower = question.lower()
    
    # Basic pattern matching
    if any(word in question_lower for word in ['total', 'jumlah', 'sum']):
        return handle_total_analysis(df, question)
    elif any(word in question_lower for word in ['rata', 'average', 'mean']):
        return handle_average_analysis(df, question)
    elif any(word in question_lower for word in ['terlaris', 'terbanyak', 'top']):
        return handle_top_analysis(df, question)
    elif any(word in question_lower for word in ['tren', 'trend', 'perkembangan']):
        return handle_trend_analysis(df, question)
    else:
        return handle_general_analysis(df, question)

def handle_total_analysis(df, question):
    """Handle total-related questions"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        total = df[col].sum()
        
        return {
            'success': True,
            'question': question,
            'answer': f'Total {col}: {total:,.2f}',
            'insights': [
                f'📊 Total nilai pada kolom {col}: {total:,.2f}',
                f'🔢 Berdasarkan {len(df)} baris data'
            ],
            'data': {
                'total': total,
                'column': col,
                'rows_analyzed': len(df)
            }
        }
    else:
        return {
            'success': True,
            'question': question,
            'answer': 'Tidak ditemukan kolom numerik untuk menghitung total',
            'insights': ['Dataset tidak memiliki kolom numerik']
        }

def handle_average_analysis(df, question):
    """Handle average-related questions"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        avg = df[col].mean()
        
        return {
            'success': True,
            'question': question,
            'answer': f'Rata-rata {col}: {avg:,.2f}',
            'insights': [
                f'📈 Rata-rata {col}: {avg:,.2f}',
                f'📊 Nilai tertinggi: {df[col].max():,.2f}',
                f'📉 Nilai terendah: {df[col].min():,.2f}'
            ]
        }
    else:
        return handle_general_analysis(df, question)

def handle_top_analysis(df, question):
    """Handle top-related questions"""
    # Cari kolom categorical untuk top items
    cat_cols = df.select_dtypes(include=['object']).columns
    
    if len(cat_cols) > 0:
        col = cat_cols[0]
        top_items = df[col].value_counts().head(5)
        
        return {
            'success': True,
            'question': question,
            'answer': f'Top 5 {col}: {top_items.index[0]} ({top_items.iloc[0]} occurrences)',
            'insights': [
                f'🏆 {col} teratas: {top_items.index[0]}',
                f'📊 Distribusi: {len(top_items)} unique values'
            ],
            'top_items': top_items.to_dict()
        }
    else:
        return handle_general_analysis(df, question)

def handle_trend_analysis(df, question):
    """Handle trend-related questions"""
    date_cols = df.select_dtypes(include=['datetime64']).columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(date_cols) > 0 and len(numeric_cols) > 0:
        date_col = date_cols[0]
        num_col = numeric_cols[0]
        
        # Simple trend analysis
        if hasattr(df[date_col], 'dt'):
            monthly_trend = df.groupby(df[date_col].dt.to_period('M'))[num_col].mean()
            
            return {
                'success': True,
                'question': question,
                'answer': f'Tren {num_col} berdasarkan waktu dianalisis',
                'insights': [
                    f'📈 Tren {num_col} per bulan berhasil dihitung',
                    f'📅 Periode: {len(monthly_trend)} bulan'
                ],
                'trend_data': monthly_trend.to_dict()
            }
    
    return handle_general_analysis(df, question)

def handle_general_analysis(df, question):
    """General analysis fallback"""
    return {
        'success': True,
        'question': question,
        'answer': f'Saya menganalisis: "{question}"',
        'insights': [
            f'📊 Dataset: {df.shape[0]} baris, {df.shape[1]} kolom',
            f'🔢 Kolom numerik: {len(df.select_dtypes(include=[np.number]).columns)}',
            f'📝 Kolom teks: {len(df.select_dtypes(include=["object"]).columns)}',
            '💡 Gunakan pertanyaan spesifik untuk analisis lebih detail'
        ],
        'recommendations': [
            'Upload file CSV/Excel untuk analisis real data',
            'Gunakan pertanyaan dari 50 questions list',
            'Contoh: "Bagaimana total penjualan?" atau "Apa produk terlaris?"'
        ],
        'dataset_info': {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'data_types': df.dtypes.astype(str).to_dict()
        }
    }

# ============================================================================
# FILE UPLOAD ENDPOINT
# ============================================================================
@app.route('/upload', methods=['POST'])
def upload_file():
    """Enhanced upload endpoint dengan real data processing"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        # Validasi file extension
        allowed_extensions = ['.csv', '.xlsx', '.xls']
        file_extension = os.path.splitext(file.filename)[1].lower()
        if file_extension not in allowed_extensions:
            return jsonify({
                'success': False, 
                'error': f'File type not supported. Allowed: {", ".join(allowed_extensions)}'
            }), 400
        
        # Save file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{file.filename}"
        filepath = os.path.join('uploads', filename)
        
        # Ensure upload directory exists
        os.makedirs('uploads', exist_ok=True)
        file.save(filepath)
        
        # Process file untuk mendapatkan real data
        file_size = os.path.getsize(filepath)
        
        try:
            # Load data dengan pandas
            if file_extension == '.csv':
                df = pd.read_csv(filepath)
            else:
                df = pd.read_excel(filepath)
            
            # Generate real preview data
            preview_data = df.head(10).replace({np.nan: None}).to_dict('records')
            
            # Basic info
            basic_info = {
                'rows': len(df),
                'columns': len(df.columns),
                'column_names': df.columns.tolist(),
                'data_types': df.dtypes.astype(str).to_dict()
            }
            
            # Data quality analysis
            missing_values = df.isnull().sum().to_dict()
            duplicated_rows = df.duplicated().sum()
            missing_percentage = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
            
            result = {
                'success': True,
                'message': 'File uploaded and analyzed successfully',
                'filename': filename,
                'original_filename': file.filename,
                'filepath': filepath,
                'file_size': file_size,
                'file_size_mb': round(file_size / (1024 * 1024), 2),
                'preview': preview_data,
                'basic_info': basic_info,
                'data_quality': {
                    'missing_values': missing_values,
                    'missing_percentage': round(missing_percentage, 2),
                    'duplicated_rows': duplicated_rows,
                    'total_cells': len(df) * len(df.columns)
                },
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as processing_error:
            # Fallback jika processing gagal
            result = {
                'success': True,
                'message': 'File uploaded (processing limited)',
                'filename': filename,
                'original_filename': file.filename,
                'filepath': filepath,
                'file_size': file_size,
                'file_size_mb': round(file_size / (1024 * 1024), 2),
                'preview': [],
                'basic_info': {'rows': 0, 'columns': 0},
                'data_quality': {'missing_percentage': 0, 'duplicated_rows': 0},
                'warning': f'Data processing limited: {str(processing_error)}'
            }
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Upload failed: {str(e)}'
        }), 500

# ============================================================================
# VISUALIZATION ENDPOINT
# ============================================================================
@app.route('/visualize', methods=['POST'])
def generate_visualizations():
    """Enhanced visualization dengan real data"""
    try:
        data = request.get_json()
        
        if not data or 'filename' not in data:
            return jsonify({'success': False, 'error': 'Filename required'}), 400
        
        filename = data['filename']
        filepath = os.path.join('uploads', filename)
        
        if not os.path.exists(filepath):
            return jsonify({'success': False, 'error': 'File not found'}), 404
        
        # Load dataset
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension == '.csv':
            df = pd.read_csv(filepath)
        else:
            df = pd.read_excel(filepath)
        
        # Generate real visualizations
        charts = generate_real_charts(df)
        
        return jsonify({
            'success': True,
            'message': 'Visualizations generated successfully',
            'filename': filename,
            'charts': charts,
            'chart_count': sum(len(charts[key]) for key in charts)
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Visualization failed: {str(e)}'
        }), 500

# ============================================================================
# FILE MANAGEMENT ENDPOINTS
# ============================================================================
@app.route('/api/files', methods=['GET'])
def list_uploaded_files():
    """List semua uploaded files"""
    try:
        files = []
        if os.path.exists('uploads'):
            for filename in os.listdir('uploads'):
                filepath = os.path.join('uploads', filename)
                if os.path.isfile(filepath):
                    files.append({
                        'name': filename,
                        'size': os.path.getsize(filepath),
                        'size_mb': round(os.path.getsize(filepath) / (1024 * 1024), 2),
                        'modified': datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
                    })
        
        return jsonify({
            'success': True,
            'total_files': len(files),
            'files': files
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Failed to list files: {str(e)}'
        }), 500

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
def load_uploaded_file(filename):
    """Load uploaded file dari uploads directory"""
    if not filename:
        return None
    
    filepath = os.path.join('uploads', filename)
    if not os.path.exists(filepath):
        return None
    
    try:
        if filename.endswith('.csv'):
            return pd.read_csv(filepath)
        elif filename.endswith(('.xlsx', '.xls')):
            return pd.read_excel(filepath)
        else:
            return None
    except Exception as e:
        print(f"Error loading file {filename}: {e}")
        return None

def generate_sample_data():
    """Generate sample data untuk testing"""
    return pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=100, freq='D'),
        'product': ['Product A', 'Product B', 'Product C'] * 33 + ['Product A'],
        'sales': np.random.randint(50, 500, 100),
        'price': np.random.uniform(10, 100, 100),
        'customer_id': range(1, 101),
        'region': ['Jakarta', 'Surabaya', 'Bandung'] * 33 + ['Jakarta'],
        'category': ['Electronics', 'Fashion', 'Home'] * 33 + ['Electronics']
    })

def generate_real_charts(df):
    """Generate real charts dari dataset"""
    charts = {
        'histograms': {},
        'barcharts': {},
        'linecharts': {}
    }
    
    # Analyze numeric columns untuk histograms
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for col in numeric_columns[:3]:  # Max 3 histograms
        if len(df[col].unique()) > 1:
            hist, bins = np.histogram(df[col].dropna(), bins=10)
            charts['histograms'][col] = {
                'labels': [f"{bins[i]:.1f}-{bins[i+1]:.1f}" for i in range(len(bins)-1)],
                'data': hist.tolist()
            }
    
    # Analyze categorical columns untuk barcharts
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns[:2]:  # Max 2 barcharts
        value_counts = df[col].value_counts().head(10)
        if len(value_counts) > 0:
            charts['barcharts'][col] = {
                'labels': value_counts.index.tolist(),
                'data': value_counts.values.tolist()
            }
    
    return charts

# ============================================================================
# APPLICATION STARTUP
# ============================================================================
if __name__ == '__main__':
    print("=" * 60)
    print("🚀 INSIGHTFLOW API STARTING...")
    print("=" * 60)
    print(f"📍 Health Check: http://localhost:8000/health")
    print(f"📍 Homepage: http://localhost:8000/")
    print(f"📍 Questions: http://localhost:8000/api/questions")
    print("=" * 60)
    print("🔧 Loaded Features:")
    print(f"   • 50 Questions: ✅ ALWAYS AVAILABLE")
    print(f"   • File Upload: ✅ AVAILABLE") 
    print(f"   • Basic Analysis: ✅ AVAILABLE")
    print(f"   • Visualization: ✅ AVAILABLE")
    print("=" * 60)
    
    # Ensure directories exist
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    app.run(host='0.0.0.0', port=8000, debug=True)