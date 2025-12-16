import mne
import os

print("--- Step 1: Loading Raw Data for Processing ---")

try:
    # این تابع خودش اگر دیتاست قبلاً دانلود نشده باشه، دانلودش می‌کنه.
    data_root = mne.datasets.sample.data_path()
    sample_data_folder = os.path.join(data_root, 'MEG', 'sample')
    fif_file_path = os.path.join(sample_data_folder, 'sample_audvis_raw.fif')

    print(f"\nAttempting to load Raw data from: {fif_file_path}")

    # لود کردن فایل FIF به یک شیء Raw
    # preload=True باعث میشه تمام داده‌ها در حافظه بارگذاری بشن.
    raw = mne.io.read_raw_fif(fif_file_path, preload=True, verbose=False)
    print("Raw data loaded successfully!")

    # نمایش اطلاعات اولیه سیگنال
    print("\n--- Raw Info (Initial) ---")
    print(raw)
    print(f"Sampling frequency: {raw.info['sfreq']} Hz")
    print(f"Number of channels: {len(raw.ch_names)}")
    print(f"Duration: {raw.n_times / raw.info['sfreq']:.2f} seconds")

    # ذخیره شیء 'raw' در یک متغیر سراسری یا فایل موقت برای استفاده در مراحل بعدی
    # (در عمل، شیء raw در حافظه باقی می ماند تا اسکریپت تمام شود،
    # اما برای آموزش مرحله به مرحله، فرض می کنیم در هر مرحله آن را داریم)

    print("\nRaw data is now loaded and ready for the next processing steps!")

    # -------------------------------------------------------------
    # مرحله ۲: (متدهای پردازشی) - در ادامه اضافه خواهیم کرد
    # -------------------------------------------------------------


except FileNotFoundError:
    print(f"\nError: The file {fif_file_path} was not found.")
    print("Please make sure the 'sample' dataset is downloaded correctly by MNE.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    print("Please ensure MNE is correctly installed.")

print("\n--- Data Loading Process Complete ---")