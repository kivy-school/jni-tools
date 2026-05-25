from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SplashScreen"]

class SplashScreen(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/SplashScreen"
    SPLASH_SCREEN_STYLE_ICON = JavaStaticField("I")
    SPLASH_SCREEN_STYLE_SOLID_COLOR = JavaStaticField("I")
    setOnExitAnimationListener = JavaMethod("(Landroid/window/SplashScreen$OnExitAnimationListener;)V")
    clearOnExitAnimationListener = JavaMethod("()V")
    setSplashScreenTheme = JavaMethod("(I)V")

    class OnExitAnimationListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/window/SplashScreen/OnExitAnimationListener"
        onSplashScreenExit = JavaMethod("(Landroid/window/SplashScreenView;)V")