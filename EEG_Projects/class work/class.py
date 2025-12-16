
import mne
import matplotlib.pyplot as plt # برای پلات کردن
from pathlib import Path # P بزرگ درست است

# این خط دیتاست 'sample' را دانلود می‌کند و مسیر آن را به صورت یک رشته برمی‌گرداند.
# حتماً به خاطر حجم زیاد (حدود 1.5GB) و اینترنت شما، برای اولین بار زمانبر خواهد بود.
print("Attempting to download 'sample' dataset...")
raw_data_path_string = mne.datasets.sample.data_path()
print(f"Sample dataset downloaded/found at: {raw_data_path_string}")

# حالا مسیر رشته‌ای را به یک شیء Path تبدیل می‌کنیم تا بتوانیم از عملگر / استفاده کنیم.
sample_data_path = Path(raw_data_path_string)

# ساخت مسیر کامل فایل داده خام با استفاده از شیء Path
raw_file = sample_data_path / 'MEG' / 'sample' / 'sample_audvis_raw.fif'
print(f"Full path to raw data file: {raw_file}")

# خواندن فایل داده خام و بارگذاری کامل داده‌ها در حافظه (preload=True)
# این مرحله نیز به دلیل حجم زیاد داده‌ها زمانبر و نیازمند RAM کافی است.
print("\nReading raw data and preloading (this might take a while)...")
try:
    raw = mne.io.read_raw_fif(raw_file, preload=True, verbose=False)
    print("Raw data loaded successfully.")

    # پلات کردن داده‌ها
    # verbose=False برای جلوگیری از پیام‌های اضافی در پلات کردن
    print("\nPlotting raw EEG data...")
    fig = raw.plot(title='Raw EEG Data', show=False, verbose=False)
    fig.show()
    print("Plotting complete.")

except Exception as e:
    print(f"ERROR: An error occurred during loading or plotting: {e}")
    print("This might be due to incomplete download, corrupted file, or insufficient RAM.")