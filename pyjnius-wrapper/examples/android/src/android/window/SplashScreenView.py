from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SplashScreenView"]

class SplashScreenView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/SplashScreenView"
    setAlpha = JavaMethod("(F)V")
    getIconAnimationDuration = JavaMethod("()Ljava/time/Duration;")
    getIconAnimationStart = JavaMethod("()Ljava/time/Instant;")
    remove = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    onLayout = JavaMethod("(ZIIII)V")
    getIconView = JavaMethod("()Landroid/view/View;")