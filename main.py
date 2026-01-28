from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

# ВСТАВЬТЕ СЮДА СВОИ ID:
ADMOB_APP_ID = "ca-app-pub-2183089216371855~7403235183"
BANNER_AD_UNIT_ID = "ca-app-pub-2183089216371855/4408232727"

# Тестовые ID (Google):
# ADMOB_APP_ID = "ca-app-pub-3940256099942544~3347511713"
# BANNER_AD_UNIT_ID = "ca-app-pub-3940256099942544/6300978111"

if platform == "android":
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

class RootLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Основной контент
        self.add_widget(Label(text="Контент приложения", size_hint_y=1))

        # Нижняя панель инструментов
        bottom_bar = BoxLayout(size_hint_y=None, height="56dp")
        bottom_bar.add_widget(Button(text="Home"))
        bottom_bar.add_widget(Button(text="Search"))
        bottom_bar.add_widget(Button(text="Profile"))
        self.add_widget(bottom_bar)

class MyApp(App):
    def build(self):
        return RootLayout()

    def on_start(self):
        if platform == "android":
            self.show_banner()

    @run_on_ui_thread
    def show_banner(self):
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        activity = PythonActivity.mActivity

        # Инициализация AdMob
        MobileAds = autoclass("com.google.android.gms.ads.MobileAds")
        MobileAds.initialize(activity)

        AdView = autoclass("com.google.android.gms.ads.AdView")
        AdSize = autoclass("com.google.android.gms.ads.AdSize")
        AdRequestBuilder = autoclass("com.google.android.gms.ads.AdRequest$Builder")

        ad_view = AdView(activity)
        ad_view.setAdSize(AdSize.BANNER)
        ad_view.setAdUnitId(BANNER_AD_UNIT_ID)

        ad_request = AdRequestBuilder().build()
        ad_view.loadAd(ad_request)

        # Добавляем баннер сверху
        FrameLayoutParams = autoclass("android.widget.FrameLayout$LayoutParams")
        Gravity = autoclass("android.view.Gravity")
        params = FrameLayoutParams(
            FrameLayoutParams.MATCH_PARENT,
            FrameLayoutParams.WRAP_CONTENT
        )
        params.gravity = Gravity.TOP

        activity.addContentView(ad_view, params)

if __name__ == "__main__":
    MyApp().run()
