# 📖 E-Ink Display for Windows

**[🇬🇧 English](#-english) | [🇻🇳 Tiếng Việt](#-tiếng-việt)**

---

## 🇬🇧 English

A lightweight desktop utility that transforms your laptop or PC monitor into an eye-friendly **E-Ink display** (Kindle / Onyx Boox simulation) using GPU hardware acceleration via the **Windows Magnification API** (`MagSetFullscreenColorEffect`) — delivering **zero lag** and **zero FPS drop**.

### ✨ Key Features
* **4 Built-in E-Ink Presets:**
  * 📰 **Soft Gray E-Ink (Newsprint):** Eliminates harsh white glare (`#FFFFFF`) into soothing matte newsprint gray.
  * 📖 **Classic Warm Paper:** Adds a paper-like sepia warmth while cutting blue light.
  * 🌙 **Night Reading E-Ink:** Ultra-dim low-glare paper mode to prevent eye strain in dark environments.
  * 🌑 **Dark E-Ink (Inverted Mode):** Charcoal matte background with soft warm-white ink.
* **Real-time Fine-tuning Sliders:** Directly adjust **Paper Brightness**, **Warmth (Blue-light Cut)**, and **Ink Softness (Matte Black)** in real time.
* **Personal Preset & Auto-save:** Save your favorite custom configuration (`settings.json`) and automatically restore your preferred language and display settings on startup.
* **Multi-language Support:** Built-in support for **Vietnamese (🇻🇳), English (🇺🇸), Chinese Simplified (🇨🇳), and Japanese (🇯🇵)**.
* **System Tray Integration:** Minimize neatly to the Windows System Tray for quick one-click switching without cluttering your taskbar.

### 🚀 Installation & Usage

#### Option 1: Download Pre-built `.exe` (Recommended)
1. Go to the **[Releases](../../releases)** section on the right side of this repository.
2. Download the latest **`E-Ink_Display.exe`** file.
3. Double-click to run directly — **no Python installation required!**

#### Option 2: Run from Source Code (`eink_mode.py`)
```bash
git clone [https://github.com/Nhanmykhe/E-ink-Display.git](https://github.com/Nhanmykhe/E-ink-Display.git)
cd E-ink-Display
python eink_mode.py
```

---

## 🇻🇳 Tiếng Việt

Phần mềm tiện ích siêu nhẹ giúp biến màn hình máy tính/laptop Windows của bạn thành **màn hình giấy điện tử E-Ink** (mô phỏng chuẩn máy đọc sách Kindle / Boox) thông qua tăng tốc phần cứng GPU của **Windows Magnification API** — **không giật lag, không tụt FPS** và áp dụng trên toàn bộ hệ điều hành.

### ✨ Tính năng nổi bật
* **4 Chế độ E-Ink cài sẵn:**
  * 📰 **E-Ink Trắng Xám Dịu (Giấy báo):** Khử hoàn toàn độ chói của màu trắng tinh (`#FFFFFF`), chuyển về tông xám giấy báo dịu mắt.
  * 📖 **E-Ink Giấy Cổ Điển:** Tông màu giấy ngả vàng ấm áp, lọc ánh sáng xanh có hại cho mắt.
  * 🌙 **E-Ink Đọc Đêm:** Hạ sâu độ sáng nền giấy, chống mỏi mắt khi làm việc hoặc đọc tài liệu ban đêm.
  * 🌑 **Dark E-Ink (Nền Đen Mực Trắng):** Đảo ngược thông minh với nền than chì dịu và chữ trắng ngà ấm.
* **3 Thanh trượt tinh chỉnh thời gian thực:** Tự do điều chỉnh **Độ sáng nền giấy**, **Độ ấm (Khử ánh sáng xanh)** và **Độ dịu mực đen (Matte Ink)**.
* **Lưu cấu hình cá nhân & Tự động ghi nhớ:** Cho phép lưu thông số yêu thích của riêng bạn và tự động khôi phục trạng thái mỗi khi mở lại ứng dụng.
* **Hỗ trợ Đa ngôn ngữ:** Tích hợp sẵn 4 ngôn ngữ **Tiếng Việt (🇻🇳), Tiếng Anh (🇺🇸), Tiếng Trung (🇨🇳) và Tiếng Nhật (🇯🇵)**.
* **Chạy ngầm ở Khay hệ thống (System Tray):** Thu gọn gọn gàng xuống góc phải thanh Taskbar để bật/tắt nhanh bất kỳ lúc nào.

### 🚀 Hướng dẫn Tải và Sử dụng

#### Cách 1: Tải file `.exe` chạy ngay (Khuyên dùng)
1. Truy cập mục **[Releases](../../releases)** ở cột bên phải của trang GitHub này.
2. Tải file **`E-Ink_Display.exe`** mới nhất về máy.
3. Mở lên và sử dụng ngay lập tức (**không cần cài đặt Python**).

#### Cách 2: Chạy từ mã nguồn (`eink_mode.py`)
```bash
git clone [https://github.com/Nhanmykhe/E-ink-Display.git](https://github.com/Nhanmykhe/E-ink-Display.git)
cd E-ink-Display
python eink_mode.py
```

---

## 📁 Cấu trúc thư mục / Project Structure
```text
E-ink-Display/
├── eink_mode.py      # Mã nguồn chính (Main Python source code)
├── README.md         # Tài liệu hướng dẫn (Documentation)
└── .gitignore        # Cấu hình bỏ qua các file tạm khi build
```
