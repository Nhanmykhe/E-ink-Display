import atexit
import ctypes
import json
import os
import sys
import tkinter as tk
from tkinter import ttk

# Tải thư viện Magnification.dll của Windows
mag_dll = ctypes.windll.LoadLibrary("Magnification.dll")
kernel32 = ctypes.windll.kernel32


class MAGCOLOREFFECT(ctypes.Structure):
    _fields_ = [("transform", (ctypes.c_float * 5) * 5)]


def create_matrix(values):
    effect = MAGCOLOREFFECT()
    for r in range(5):
        for c in range(5):
            effect.transform[r][c] = values[r][c]
    return effect


# Ma trận gốc 100% của Windows
IDENTITY_MATRIX = create_matrix([
    [1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0],
])


def reset_screen_safely():
    """Hàm bảo hiểm: Luôn trả màn hình về gốc và gỡ Magnification an toàn"""
    try:
        mag_dll.MagSetFullscreenColorEffect(ctypes.byref(IDENTITY_MATRIX))
        mag_dll.MagUninitialize()
    except Exception:
        pass


atexit.register(reset_screen_safely)


def get_config_path():
    appdata = os.getenv("APPDATA") or os.path.expanduser("~")
    config_dir = os.path.join(appdata, "EInkDisplayPro")
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "eink_config.json")


CONFIG_FILE = get_config_path()

# Bộ từ điển Đa ngôn ngữ (Việt, Anh, Trung, Nhật)
TRANSLATIONS = {
    "vi": {
        "lang_name": "🇻🇳 Tiếng Việt",
        "btn_normal": "🖥️ TRẢ VỀ MÀN HÌNH GỐC (Tắt E-Ink) [Esc]",
        "sec_presets": "1. Chọn chế độ E-Ink cài sẵn:",
        "preset_paper": "📰 E-Ink Trắng Xám Dịu (Giấy báo - Hết chói)",
        "preset_classic": "📖 E-Ink Giấy Cổ Điển (Ấm dịu)",
        "preset_night": "🌙 E-Ink Đọc Đêm (Siêu tối - Chống mỏi mắt)",
        "btn_fav_load": "⭐ Bật Cấu hình Cá nhân",
        "btn_fav_save": "💾 Lưu vào Cá nhân",
        "sec_sliders": "2. Tinh chỉnh thông số E-Ink:",
        "btn_reset": "🔄 Khôi phục mặc định",
        "lbl_bright": "Độ sáng nền trắng: {val}%",
        "lbl_warm": "Độ ấm (Khử xanh): {val}%",
        "lbl_ink": "Độ dịu mực đen (Matte): {val}%",
        "chk_auto": "Tự động bật ngay cấu hình E-Ink này khi mở ứng dụng",
        "lbl_lang": "🌐 Ngôn ngữ / Language:",
        "status_prefix": "Trạng thái:",
        "mode_normal": "🖥️ Màn hình Gốc (Mặc định)",
        "mode_saved": "📖 Cấu hình đã lưu",
        "mode_custom": "📖 E-Ink Tùy chỉnh (Đã lưu)",
        "mode_paper": "📖 E-Ink Trắng Xám Dịu",
        "mode_classic": "📖 E-Ink Giấy Cổ Điển",
        "mode_night": "📖 E-Ink Đọc Đêm",
        "mode_fav_saved": "💾 Đã lưu vào Cấu hình Cá nhân!",
        "mode_fav_loaded": "⭐ Cấu hình Cá nhân",
        "mode_default": "📖 E-Ink Chuẩn Mặc Định",
    },
    "en": {
        "lang_name": "🇺🇸 English",
        "btn_normal": "🖥️ RESTORE ORIGINAL DISPLAY (Off) [Esc]",
        "sec_presets": "1. E-Ink Presets:",
        "preset_paper": "📰 Soft Gray E-Ink (Newsprint - Anti-Glare)",
        "preset_classic": "📖 Classic Warm Paper E-Ink",
        "preset_night": "🌙 Night Reading E-Ink (Ultra Dim)",
        "btn_fav_load": "⭐ Load My Preset",
        "btn_fav_save": "💾 Save as My Preset",
        "sec_sliders": "2. Fine-tune E-Ink Parameters:",
        "btn_reset": "🔄 Reset Defaults",
        "lbl_bright": "Paper Brightness: {val}%",
        "lbl_warm": "Warmth (Blue Cut): {val}%",
        "lbl_ink": "Ink Softness (Matte): {val}%",
        "chk_auto": "Auto-apply this E-Ink profile on startup",
        "lbl_lang": "🌐 Language:",
        "status_prefix": "Status:",
        "mode_normal": "🖥️ Original Display (Default)",
        "mode_saved": "📖 Saved Profile",
        "mode_custom": "📖 Custom E-Ink (Saved)",
        "mode_paper": "📖 Soft Gray E-Ink",
        "mode_classic": "📖 Classic Warm E-Ink",
        "mode_night": "📖 Night Reading E-Ink",
        "mode_fav_saved": "💾 Saved to Personal Preset!",
        "mode_fav_loaded": "⭐ Personal Preset",
        "mode_default": "📖 Default E-Ink",
    },
    "zh": {
        "lang_name": "🇨🇳 中文 (简体)",
        "btn_normal": "🖥️ 恢复原始屏幕 (关闭墨水屏) [Esc]",
        "sec_presets": "1. 选择预设墨水屏模式:",
        "preset_paper": "📰 柔和灰白墨水屏 (报纸感 - 防刺眼)",
        "preset_classic": "📖 经典暖色纸张墨水屏 (护眼)",
        "preset_night": "🌙 夜间阅读墨水屏 (超暗抗疲劳)",
        "btn_fav_load": "⭐ 启用个人配置",
        "btn_fav_save": "💾 保存为个人配置",
        "sec_sliders": "2. 微调墨水屏参数:",
        "btn_reset": "🔄 恢复默认",
        "lbl_bright": "纸张白度亮度: {val}%",
        "lbl_warm": "暖色温 (滤蓝光): {val}%",
        "lbl_ink": "墨迹柔和度 (雾面): {val}%",
        "chk_auto": "启动软件时自动应用此墨水屏配置",
        "lbl_lang": "🌐 语言 / Language:",
        "status_prefix": "当前状态:",
        "mode_normal": "🖥️ 原始屏幕 (默认)",
        "mode_saved": "📖 已保存的配置",
        "mode_custom": "📖 自定义墨水屏 (已保存)",
        "mode_paper": "📖 柔和灰白墨水屏",
        "mode_classic": "📖 经典暖色墨水屏",
        "mode_night": "📖 夜间阅读墨水屏",
        "mode_fav_saved": "💾 已保存到个人配置!",
        "mode_fav_loaded": "⭐ 个人配置",
        "mode_default": "📖 默认标准墨水屏",
    },
    "ja": {
        "lang_name": "🇯🇵 日本語",
        "btn_normal": "🖥️ 元の画面に戻す (E-Ink オフ) [Esc]",
        "sec_presets": "1. E-Ink プリセットの選択:",
        "preset_paper": "📰 ソフトグレー E-Ink (新聞紙風・防眩)",
        "preset_classic": "📖 クラシック暖色ペーパー E-Ink",
        "preset_night": "🌙 夜間読書モード E-Ink (超低輝度)",
        "btn_fav_load": "⭐ マイ設定を適用",
        "btn_fav_save": "💾 マイ設定に保存",
        "sec_sliders": "2. E-Ink パラメータ微調整:",
        "btn_reset": "🔄 初期値に戻す",
        "lbl_bright": "紙面の明るさ: {val}%",
        "lbl_warm": "色温度 (ブルーライト軽減): {val}%",
        "lbl_ink": "インクの柔らかさ (マット): {val}%",
        "chk_auto": "起動時にこの E-Ink 設定を自動適用する",
        "lbl_lang": "🌐 言語 / Language:",
        "status_prefix": "ステータス:",
        "mode_normal": "🖥️ 元の画面 (デフォルト)",
        "mode_saved": "📖 保存された設定",
        "mode_custom": "📖 カスタム E-Ink (保存済)",
        "mode_paper": "📖 ソフトグレー E-Ink",
        "mode_classic": "📖 クラシック暖色 E-Ink",
        "mode_night": "📖 夜間読書 E-Ink",
        "mode_fav_saved": "💾 マイ設定に保存しました！",
        "mode_fav_loaded": "⭐ マイ設定",
        "mode_default": "📖 標準 E-Ink",
    },
}


class EInkControllerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("E-Ink Display Pro")
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)

        self.initializing = True
        self.is_closing = False

        if not mag_dll.MagInitialize():
            raise RuntimeError("Cannot initialize Windows Magnification API.")

        self.default_brightness = 0.68
        self.default_warmth = 0.05
        self.default_ink = 0.05

        saved_cfg = self.load_config()

        self.lang_code = saved_cfg.get("language", "vi")
        if self.lang_code not in TRANSLATIONS:
            self.lang_code = "vi"

        self.brightness = tk.DoubleVar(
            value=saved_cfg.get("brightness", self.default_brightness)
        )
        self.warmth = tk.DoubleVar(
            value=saved_cfg.get("warmth", self.default_warmth)
        )
        self.ink_softness = tk.DoubleVar(
            value=saved_cfg.get("ink_softness", self.default_ink)
        )
        self.auto_apply = tk.BooleanVar(
            value=saved_cfg.get("auto_apply", True)
        )

        self.fav_brightness = saved_cfg.get(
            "fav_brightness", self.default_brightness
        )
        self.fav_warmth = saved_cfg.get("fav_warmth", self.default_warmth)
        self.fav_ink = saved_cfg.get("fav_ink", self.default_ink)

        # Lưu khóa trạng thái hiện tại để dịch tự động khi đổi ngôn ngữ
        self.current_status_key = "mode_normal"
        self.is_eink_active = False

        self.build_ui()
        self.apply_language_texts()

        self.root.update_idletasks()
        self.root.minsize(420, self.root.winfo_reqheight())

        self.initializing = False

        if self.auto_apply.get():
            self.update_eink_effect(status_key="mode_saved")

        self.root.bind("<Escape>", lambda e: self.set_normal())
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def save_config(self):
        if self.is_closing:
            return
        data = {
            "language": self.lang_code,
            "brightness": round(self.brightness.get(), 4),
            "warmth": round(self.warmth.get(), 4),
            "ink_softness": round(self.ink_softness.get(), 4),
            "auto_apply": self.auto_apply.get(),
            "fav_brightness": round(self.fav_brightness, 4),
            "fav_warmth": round(self.fav_warmth, 4),
            "fav_ink": round(self.fav_ink, 4),
        }
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception:
            pass

    def build_ui(self):
        frame = ttk.Frame(self.root, padding=16)
        frame.pack(fill="both", expand=True)

        self.lbl_status = ttk.Label(
            frame,
            text="",
            font=("Segoe UI", 10, "bold"),
            foreground="#0066CC",
        )
        self.lbl_status.pack(anchor="w", pady=(0, 8))

        self.btn_normal = tk.Button(
            frame,
            text="",
            font=("Segoe UI", 9, "bold"),
            bg="#E1F0FF",
            fg="#003366",
            activebackground="#CCE4FF",
            relief="groove",
            pady=6,
            command=self.set_normal,
        )
        self.btn_normal.pack(fill="x", pady=(0, 12))

        self.lbl_sec_presets = ttk.Label(
            frame, text="", font=("Segoe UI", 10, "bold")
        )
        self.lbl_sec_presets.pack(anchor="w", pady=(0, 6))

        self.btn_preset_paper = ttk.Button(
            frame,
            text="",
            command=lambda: self.apply_preset(0.68, 0.02, 0.05, "mode_paper"),
        )
        self.btn_preset_paper.pack(fill="x", pady=2)

        self.btn_preset_classic = ttk.Button(
            frame,
            text="",
            command=lambda: self.apply_preset(0.70, 0.14, 0.06, "mode_classic"),
        )
        self.btn_preset_classic.pack(fill="x", pady=2)

        self.btn_preset_night = ttk.Button(
            frame,
            text="",
            command=lambda: self.apply_preset(0.48, 0.18, 0.04, "mode_night"),
        )
        self.btn_preset_night.pack(fill="x", pady=2)

        fav_frame = ttk.Frame(frame)
        fav_frame.pack(fill="x", pady=(4, 2))
        self.btn_fav_load = ttk.Button(
            fav_frame, text="", command=self.load_favorite_preset
        )
        self.btn_fav_load.pack(side="left", fill="x", expand=True, padx=(0, 2))

        self.btn_fav_save = ttk.Button(
            fav_frame, text="", command=self.save_as_favorite
        )
        self.btn_fav_save.pack(side="right", fill="x", expand=True, padx=(2, 0))

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=10)

        header_frame = ttk.Frame(frame)
        header_frame.pack(fill="x", pady=(0, 6))

        self.lbl_sec_sliders = ttk.Label(
            header_frame, text="", font=("Segoe UI", 10, "bold")
        )
        self.lbl_sec_sliders.pack(side="left")

        self.btn_reset = ttk.Button(
            header_frame, text="", command=self.reset_sliders_to_default
        )
        self.btn_reset.pack(side="right")

        self.lbl_bright = ttk.Label(frame, text="")
        self.lbl_bright.pack(anchor="w")
        self.scale_bright = ttk.Scale(
            frame,
            from_=0.30,
            to=0.95,
            variable=self.brightness,
            command=self.on_slider_move,
        )
        self.scale_bright.pack(fill="x", pady=(0, 6))

        self.lbl_warm = ttk.Label(frame, text="")
        self.lbl_warm.pack(anchor="w")
        self.scale_warm = ttk.Scale(
            frame,
            from_=0.00,
            to=0.30,
            variable=self.warmth,
            command=self.on_slider_move,
        )
        self.scale_warm.pack(fill="x", pady=(0, 6))

        self.lbl_ink = ttk.Label(frame, text="")
        self.lbl_ink.pack(anchor="w")
        self.scale_ink = ttk.Scale(
            frame,
            from_=0.00,
            to=0.12,
            variable=self.ink_softness,
            command=self.on_slider_move,
        )
        self.scale_ink.pack(fill="x", pady=(0, 8))

        self.chk_auto = ttk.Checkbutton(
            frame,
            text="",
            variable=self.auto_apply,
            command=self.save_config,
        )
        self.chk_auto.pack(anchor="w", pady=(2, 8))

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=(2, 10))

        # Thay nút Thoát ở đáy bằng khung chọn Ngôn ngữ
        lang_frame = ttk.Frame(frame)
        lang_frame.pack(fill="x", pady=(2, 0))

        self.lbl_lang = ttk.Label(
            lang_frame, text="", font=("Segoe UI", 9, "bold")
        )
        self.lbl_lang.pack(side="left")

        self.lang_keys = list(TRANSLATIONS.keys())
        self.lang_names = [
            TRANSLATIONS[k]["lang_name"] for k in self.lang_keys
        ]

        self.combo_lang = ttk.Combobox(
            lang_frame,
            values=self.lang_names,
            state="readonly",
            width=18,
            font=("Segoe UI", 9),
        )
        self.combo_lang.current(self.lang_keys.index(self.lang_code))
        self.combo_lang.pack(side="right")
        self.combo_lang.bind("<<ComboboxSelected>>", self.on_language_change)

    def on_language_change(self, _=None):
        if self.is_closing:
            return
        idx = self.combo_lang.current()
        if 0 <= idx < len(self.lang_keys):
            self.lang_code = self.lang_keys[idx]
            self.apply_language_texts()
            self.save_config()

    def apply_language_texts(self):
        """Cập nhật toàn bộ chữ trên giao diện theo ngôn ngữ đang chọn"""
        if self.is_closing:
            return
        t = TRANSLATIONS[self.lang_code]

        self.btn_normal.config(text=t["btn_normal"])
        self.lbl_sec_presets.config(text=t["sec_presets"])
        self.btn_preset_paper.config(text=t["preset_paper"])
        self.btn_preset_classic.config(text=t["preset_classic"])
        self.btn_preset_night.config(text=t["preset_night"])
        self.btn_fav_load.config(text=t["btn_fav_load"])
        self.btn_fav_save.config(text=t["btn_fav_save"])
        self.lbl_sec_sliders.config(text=t["sec_sliders"])
        self.btn_reset.config(text=t["btn_reset"])
        self.chk_auto.config(text=t["chk_auto"])
        self.lbl_lang.config(text=t["lbl_lang"])

        self.update_labels_only()
        self.update_status_label()

    def update_status_label(self):
        if self.is_closing:
            return
        t = TRANSLATIONS[self.lang_code]
        mode_text = t.get(self.current_status_key, t["mode_normal"])
        color = "#2E7D32" if self.is_eink_active else "#0066CC"
        if self.current_status_key == "mode_fav_saved":
            color = "#0066CC"
        self.lbl_status.config(
            text=f"{t['status_prefix']} {mode_text}", foreground=color
        )

    def update_labels_only(self):
        if self.is_closing:
            return
        t = TRANSLATIONS[self.lang_code]
        b = int(self.brightness.get() * 100)
        w = int((self.warmth.get() / 0.30) * 100)
        ink = int((self.ink_softness.get() / 0.12) * 100)

        self.lbl_bright.config(text=t["lbl_bright"].format(val=b))
        self.lbl_warm.config(text=t["lbl_warm"].format(val=w))
        self.lbl_ink.config(text=t["lbl_ink"].format(val=ink))

    def on_slider_move(self, _=None):
        if self.initializing or self.is_closing:
            return
        self.update_eink_effect(status_key="mode_custom")
        self.save_config()

    def apply_preset(self, brightness, warmth, ink, status_key):
        if self.is_closing:
            return
        self.initializing = True
        self.brightness.set(brightness)
        self.warmth.set(warmth)
        self.ink_softness.set(ink)
        self.initializing = False
        self.update_eink_effect(status_key=status_key)
        self.save_config()

    def save_as_favorite(self):
        if self.is_closing:
            return
        self.fav_brightness = self.brightness.get()
        self.fav_warmth = self.warmth.get()
        self.fav_ink = self.ink_softness.get()
        self.save_config()
        self.current_status_key = "mode_fav_saved"
        self.update_status_label()

    def load_favorite_preset(self):
        self.apply_preset(
            self.fav_brightness,
            self.fav_warmth,
            self.fav_ink,
            "mode_fav_loaded",
        )

    def reset_sliders_to_default(self):
        self.apply_preset(
            self.default_brightness,
            self.default_warmth,
            self.default_ink,
            "mode_default",
        )

    def update_eink_effect(self, status_key="mode_custom"):
        if self.is_closing:
            return
        b = self.brightness.get()
        w = self.warmth.get()
        ink = self.ink_softness.get()

        self.is_eink_active = True
        self.current_status_key = status_key
        self.update_labels_only()
        self.update_status_label()

        effective_scale = max(0.2, b - ink)
        luma_r, luma_g, luma_b = 0.299, 0.587, 0.114

        r_mult = effective_scale * (1.0 + w * 0.25)
        g_mult = effective_scale * (1.0 - w * 0.15)
        b_mult = effective_scale * (1.0 - w * 0.85)

        matrix = create_matrix([
            [luma_r * r_mult, luma_r * g_mult, luma_r * b_mult, 0.0, 0.0],
            [luma_g * r_mult, luma_g * g_mult, luma_g * b_mult, 0.0, 0.0],
            [luma_b * r_mult, luma_b * g_mult, luma_b * b_mult, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0, 0.0],
            [ink, ink * (1.0 - w * 0.2), ink * (1.0 - w * 0.6), 0.0, 1.0],
        ])

        mag_dll.MagSetFullscreenColorEffect(ctypes.byref(matrix))

    def set_normal(self):
        """Trả màn hình về màu sắc và độ sáng gốc của Windows"""
        mag_dll.MagSetFullscreenColorEffect(ctypes.byref(IDENTITY_MATRIX))
        if not self.is_closing:
            self.is_eink_active = False
            self.current_status_key = "mode_normal"
            self.update_status_label()

    def on_close(self):
        """Đóng ứng dụng an toàn tuyệt đối khi bấm nút X của cửa sổ"""
        if self.is_closing:
            return
        self.save_config()
        self.is_closing = True
        try:
            self.scale_bright.configure(command="")
            self.scale_warm.configure(command="")
            self.scale_ink.configure(command="")
        except Exception:
            pass

        reset_screen_safely()

        try:
            self.root.quit()
            self.root.destroy()
        except Exception:
            pass
        os._exit(0)


if __name__ == "__main__":
    mutex = kernel32.CreateMutexW(None, False, "EInkDisplayPro_SingleInstance")
    if kernel32.GetLastError() == 183:
        sys.exit(0)

    root = tk.Tk()
    app = EInkControllerApp(root)
    root.mainloop()