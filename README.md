# 📖 E-Ink Display Pro for Windows

[**🇬🇧 English**](#-english) | [**🇻🇳 Tiếng Việt**](#-tiếng-việt)

---

## 🇬🇧 English

A lightweight utility that transforms your laptop or PC screen into an eye-friendly **E-Ink display (Kindle/Boox simulation)** using GPU hardware acceleration via the Windows Magnification API (Zero lag, zero FPS drop).

### ✨ Key Features
- **3 Built-in Presets:** Soft Gray Newsprint (Anti-glare), Classic Warm Paper, and Ultra-Dim Night Reading.
- **Real-time Fine-tuning Sliders:** Directly adjust Paper Brightness, Warmth (Blue-light cut), and Ink Softness (Matte contrast).
- **Personal Preset & Auto-Save:** Automatically saves your custom slider settings to `AppData` (`eink_config.json`) for the next launch.
- **Multi-language UI:** Instant switching between Tiếng Việt 🇻🇳, English 🇺🇸, 中文 🇨🇳, and 日本語 🇯🇵.
- **Zero External Dependencies:** Built purely with Python's standard libraries (`ctypes`, `tkinter`).

### 🚀 How to Use
1. **Option 1 (Standalone `.exe` - Recommended):** Download `E-Ink_Pro.exe` from the [**Releases**](../../releases) section on the right and run it directly (no Python installation required).
2. **Option 2 (Run from Python source):**
   ```bash
   python eink_mode.py
   ```
3. **Build `.exe` yourself (Optional):**
   ```bash
   pip install pyinstaller
   pyinstaller --noconsole --onefile --clean --name "E-Ink_Pro" eink_mode.py
   ```

### ⌨️ Shortcuts & Tips
- Press **`Esc`** while the app window is focused (or click the top blue button) to instantly restore your original display colors.
- Minimize the window to the taskbar while reading to keep the E-Ink effect active. Closing the window (`X`) safely restores the original screen.

---

## 🇻🇳 Tiếng Việt

Ứng dụng siêu nhẹ giúp chuyển đổi màn hình Laptop/PC sang chế độ **Giả lập Màn hình Đọc Sách E-Ink (Kindle/Boox)** bằng phần cứng GPU thông qua Windows Magnification API (Độ trễ bằng 0, không tụt FPS).

### ✨ Tính năng nổi bật
- **3 Chế độ cài sẵn (Presets):** Giấy báo trắng xám dịu (chống chói), Giấy cổ điển ấm dịu, và Đọc đêm siêu tối.
- **Thanh trượt tinh chỉnh trực tiếp:** Điều chỉnh thời gian thực Độ sáng nền giấy, Độ ấm (khử ánh sáng xanh) và Độ dịu mực đen (Matte Ink).
- **Lưu cấu hình cá nhân & Tự động nhớ (Auto-Save):** Tự động lưu thông số vào thư mục `AppData` (`eink_config.json`) cho lần mở sau.
- **Đa ngôn ngữ:** Chuyển đổi tức thì giữa Tiếng Việt 🇻🇳, English 🇺🇸, 中文 🇨🇳, 日本語 🇯🇵.
- **Không cần thư viện ngoài:** Chỉ sử dụng thư viện chuẩn có sẵn của Python (`ctypes`, `tkinter`).

### 🚀 Cách sử dụng
1. **Cách 1 (Dùng ngay file `.exe` - Khuyên dùng):** Tải file `E-Ink_Pro.exe` tại mục [**Releases**](../../releases) ở góc bên phải trang GitHub và chạy trực tiếp (không cần cài Python).
2. **Cách 2 (Chạy từ mã nguồn Python):**
   ```bash
   python eink_mode.py
   ```
3. **Tự đóng gói sang file `.exe` (Tùy chọn):**
   ```bash
   pip install pyinstaller
   pyinstaller --noconsole --onefile --clean --name "E-Ink_Pro" eink_mode.py
   ```

### ⌨️ Phím tắt & Mẹo sử dụng
- Nhấn phím **`Esc`** khi đang mở cửa sổ ứng dụng (hoặc bấm nút màu xanh trên cùng) để trả màn hình về màu gốc ngay lập tức.
- Khi đang đọc sách, hãy thu nhỏ (`Minimize -`) cửa sổ xuống thanh Taskbar để giữ chế độ E-Ink. Khi đọc xong, bấm nút đóng (`X`) để tắt E-Ink và trả lại màn hình bình thường.