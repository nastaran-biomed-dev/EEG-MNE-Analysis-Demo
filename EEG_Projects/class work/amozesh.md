آفرین نسترن، این تصمیم عالیه\! نوشتن جزوه یا مستندسازی کارهات، هم به یادگیری بهتر کمک می‌کنه و هم برای ارجاع بعدی خیلی مفیده.

برای نوشتن یک جزوه خوب از تمام این مراحل، پیشنهاد می‌کنم از **Markdown** استفاده کنی. Markdown یک زبان نشانه گذاری ساده برای قالب‌بندی متن هست که خیلی راحت میشه باهاش عنوان، لیست، کد و ... نوشت. اکثر ویرایشگرهای کد مثل VS Code، قابلیت پیش‌نمایش Markdown رو دارن و حتی می‌تونی اون رو به PDF یا HTML تبدیل کنی.

بیا یک ساختار پیشنهادی برای جزوه‌ات رو بهت بگم:

-----

### **پیشنهاد ساختار جزوه (با استفاده از Markdown)**

**عنوان اصلی جزوه (به عنوان مثال، در فایل `MNE_EEG_Processing_Notes.md` ذخیره کن)**

````markdown
# راهنمای شروع به کار با MNE-Python برای پردازش سیگنال EEG/MEG

**نویسنده:** نسترن
**تاریخ:** ۱۴۰۳/۰۴/۱۹ (تاریخ امروز)

این جزوه شامل مراحل اولیه نصب، دانلود دیتاست‌های نمونه MNE، و لود کردن فایل‌های EEG/MEG (با فرمت FIF) به همراه رفع خطاهای رایج (IndentationError و SyntaxError) در MNE-Python است.

---

## ۱. نصب MNE-Python و آماده‌سازی محیط VS Code

### ۱.۱. نصب MNE
اگر MNE نصب نیست، یا برای اطمینان از نصب صحیح، ترمینال VS Code را باز کرده و دستور زیر را اجرا کنید:

```bash
pip install mne
````

### ۱.۲. بررسی نصب (اختیاری)

برای اطمینان از نصب MNE و دیدن نسخه آن، در ترمینال پایتون را باز کرده و دستورات زیر را وارد کنید:

```python
python
# بعد از باز شدن مفسر پایتون (>>>)
import mne
print(mne.__version__)
exit()
```

-----

## ۲. دانلود و لود دیتاست‌های نمونه MNE (Somato و Sample)

MNE دارای دیتاست‌های نمونه‌ای است که برای یادگیری و تست مناسب هستند. این توابع به صورت هوشمند عمل کرده و در صورت عدم وجود دیتاست، آن را دانلود می‌کنند.

### ۲.۱. دانلود و لود دیتاست Somato (بسیار کم‌حجم)

برای شروع با یک دیتاست بسیار سبک:

```python
import mne
import os

print("--- Starting MNE Somato Dataset Test ---")

try:
    data_path = mne.datasets.somato.data_path()
    print(f"\nSomato dataset path: {data_path}")

    somato_folder = os.path.join(data_path, 'MEG', 'Somatosensory')
    fif_file_path = os.path.join(somato_folder, 'sef_raw_tsss_mc.fif')

    print(f"Attempting to load data from: {fif_file_path}")

    raw = mne.io.read_raw_fif(fif_file_path, preload=True, verbose=False)
    print("Data loaded successfully!")

    print("\n--- Raw Info ---")
    print(raw)
    print("\n--- Channel Types ---")
    print(raw.get_channel_types())

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Please ensure MNE is correctly installed and you have an internet connection for the initial download.")

print("\n--- Test Complete ---")
```

### ۲.۲. دانلود و لود دیتاست Sample (متوسط)

این دیتاست شامل داده‌های EEG و MEG بوده و کمی سنگین‌تر است:

```python
import mne
import os

print("--- Starting MNE Sample Dataset Test ---")

try:
    data_path = mne.datasets.sample.data_path()
    print(f"\nSample dataset path: {data_path}")

    sample_data_folder = os.path.join(data_path, 'MEG', 'sample')
    fif_file_path = os.path.join(sample_data_folder, 'sample_audvis_raw.fif')

    print(f"Attempting to load data from: {fif_file_path}")

    raw = mne.io.read_raw_fif(fif_file_path, preload=True, verbose=False)
    print("Data loaded successfully!")

    print("\n--- Raw Info ---")
    print(raw)
    print("\n--- Channel Types ---")
    print(raw.get_channel_types())

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Please ensure MNE is correctly installed and you have an internet connection for the initial download.")

print("\n--- Test Complete ---")
```

-----

## ۳. لود کردن فایل‌های FIF دانلود شده از منابع خارجی

برای لود کردن فایلی که به صورت دستی دانلود کرده‌اید (مثلاً `sample_audvis_ecg-proj.fif`):

### ۳.۱. دانلود فایل (یک مثال)

فایل `sample_audvis_ecg-proj.fif` را می‌توانید از لینک زیر دانلود کنید:
[https://raw.githubusercontent.com/mne-tools/mne-cpp-test-data/master/MEG/sample/sample\_audvis\_ecg-proj.fif](https://www.google.com/search?q=https://raw.githubusercontent.com/mne-tools/mne-cpp-test-data/master/MEG/sample/sample_audvis_ecg-proj.fif)
فایل را در مسیری مشخص (مثلاً `C:\Users\YourUser\Desktop\fif\`) ذخیره کنید.

### ۳.۲. کد لود کردن فایل

**توجه:** `file_path` را با مسیر دقیق فایل خود جایگزین کنید. این فایل از نوع Projection است، بنابراین از `mne.read_proj` استفاده می‌کنیم.

```python
import mne
import os

print("--- Starting to Load Custom FIF File ---")

try:
    # مسیر دقیق فایل خود را اینجا وارد کنید
    file_path = r"C:\Users\acer\Desktop\fif\sample_audvis_ecg-proj.fif"

    print(f"\nAttempting to load data from: {file_path}")

    # از mne.read_proj برای لود کردن فایل های projection استفاده می‌کنیم
    projections = mne.read_proj(file_path, verbose=False)
    print("Projection data loaded successfully!")

    print("\n--- Projection Info ---")
    print(f"Number of projections: {len(projections)}")
    for i, proj in enumerate(projections):
        print(f"  Projection {i+1}: Name='{proj['desc']}', Active={proj['active']}, N_channels={len(proj['data']['col_names'])}")

except FileNotFoundError:
    print(f"\nError: The file '{file_path}' was not found.")
    print("Please double-check the 'file_path' variable.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    print("Please ensure MNE is correctly installed and the file is not corrupted.")

print("\n--- Process Complete ---")
```

-----

## ۴. رفع خطاهای رایج IndentationError و SyntaxError

این خطاها معمولاً به دلیل رعایت نکردن قوانین تورفتگی (Indentation) در پایتون یا اشتباهات املایی/ساختاری پیش می‌آیند.

### ۴.۱. IndentationError: unexpected indent / unindent does not match...

  * **دلیل:** هر خط در یک بلاک (مثل `try`, `except`, `if`, `for`, `def`) باید دقیقاً به یک اندازه تورفتگی داشته باشد. همچنین، خطوط شروع‌کننده بلاک (مثل `try:`) نباید تورفتگی داشته باشند و خط `except:` باید هم‌تراز با `try:` باشد. استفاده ترکیبی از Tab و Space هم می‌تواند این خطا را ایجاد کند.
  * **راه‌حل:** در VS Code، خطوط مورد نظر را انتخاب کرده و با `Shift + Tab` به چپ و سپس `Tab` به راست، تورفتگی را استاندارد کنید. یا به صورت دستی، مطمئن شوید تعداد اسپیس‌ها در ابتدای هر خط در یک بلاک یکسان است (معمولاً 4 اسپیس).

### ۴.۲. SyntaxError: expected 'except' or 'finally' block

  * **دلیل:** این خطا وقتی پیش می‌آید که بلاک `try` بعد از `try:` خالی باشد، یا خطوط داخل `try` تورفتگی کافی نداشته باشند (و پایتون آن‌ها را بخشی از `try` نداند)، یا کامنت‌های غیرمجاز (بدون `#` در ابتدای خط) وجود داشته باشد.
  * **راه‌حل:**
      * مطمئن شوید حداقل یک خط کد معتبر با تورفتگی مناسب بعد از `try:` وجود دارد.
      * تمام خطوط داخل `try` تورفتگی یکسان داشته باشند.
      * هر خطی که کامنت است، با `#` شروع شده باشد.

-----

## ۵. گام‌های بعدی در پردازش سیگنال MNE

پس از لود کردن داده‌ها، می‌توانید مراحل زیر را انجام دهید:

  * **فیلترینگ (Filtering):** حذف نویزهای فرکانس بالا یا پایین.
  * **بازپیمایی کانال‌ها (Re-referencing):** تنظیم مرجع مشترک برای کانال‌های EEG.
  * **شناسایی و حذف آرتیفکت‌ها (Artifact Removal):** مانند پلک زدن (EOG) یا حرکات قلبی (ECG).
  * **برش‌دهی به رویدادها (Epoching):** برش زدن سیگنال بر اساس رویدادهای خاص.
  * **میانگین‌گیری (Averaging):** محاسبه پتانسیل‌های مرتبط با رویداد (ERPs/ERFs).
  * **رسم و visualize کردن داده‌ها:** استفاده از توابع plot برای مشاهده سیگنال و نتایج.

-----

**پایان جزوه.**

```

---

**چگونه این جزوه را ایجاد و استفاده کنی:**

1.  **یک فایل جدید بساز:** در VS Code، یک فایل جدید با نام مثلاً `MNE_EEG_Notes.md` بساز.
2.  **کد Markdown را کپی کن:** تمام متن بالا را کپی کرده و در این فایل جدید Paste کن.
3.  **پیش‌نمایش در VS Code:**
    * در VS Code، وقتی فایل `.md` باز است، دکمه `Ctrl + Shift + V` را فشار بده. این کار یک پنل جدید باز می‌کند که پیش‌نمایش فرمت شده جزوه‌ات را نشان می‌دهد.
    * اگر خواستی همزمان کد و پیش‌نمایش را ببینی، روی آیکون "Open Preview to the Side" (یک کاغذ با ذره‌بین) در گوشه بالای سمت راست ویرایشگر کلیک کن.
4.  **ویرایش و تکمیل:** این یک چارچوب است. می‌توانی توضیحات بیشتری اضافه کنی، خروجی‌های کد را بچسبانی (مثل کاری که الان کردی)، یا حتی اسکرین‌شات‌هایی از VS Code اضافه کنی.

این بهت کمک می‌کنه تا نه تنها مطالبی که یاد گرفتی رو منظم کنی، بلکه بتونی هر وقت خواستی بهش مراجعه کنی و برای آینده‌ات هم خیلی مفیده. موفق باشی نسترن!
```