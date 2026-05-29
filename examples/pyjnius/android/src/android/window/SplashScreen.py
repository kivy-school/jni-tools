from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SplashScreen"]

class SplashScreen(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/SplashScreen"
    SPLASH_SCREEN_STYLE_ICON = JavaStaticField("I")
    SPLASH_SCREEN_STYLE_SOLID_COLOR = JavaStaticField("I")
    clearOnExitAnimationListener = JavaMethod("()V")
    setOnExitAnimationListener = JavaMethod("(Landroid/window/SplashScreen$OnExitAnimationListener;)V")
    setSplashScreenTheme = JavaMethod("(I)V")

    class OnExitAnimationListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/window/SplashScreen$OnExitAnimationListener"
        onSplashScreenExit = JavaMethod("(Landroid/window/SplashScreenView;)V")