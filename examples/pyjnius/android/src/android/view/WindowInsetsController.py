from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowInsetsController"]

class WindowInsetsController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowInsetsController"
    APPEARANCE_LIGHT_CAPTION_BARS = JavaStaticField("I")
    APPEARANCE_LIGHT_NAVIGATION_BARS = JavaStaticField("I")
    APPEARANCE_LIGHT_STATUS_BARS = JavaStaticField("I")
    APPEARANCE_TRANSPARENT_CAPTION_BAR_BACKGROUND = JavaStaticField("I")
    BEHAVIOR_DEFAULT = JavaStaticField("I")
    BEHAVIOR_SHOW_BARS_BY_SWIPE = JavaStaticField("I")
    BEHAVIOR_SHOW_BARS_BY_TOUCH = JavaStaticField("I")
    BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE = JavaStaticField("I")
    addOnControllableInsetsChangedListener = JavaMethod("(Landroid/view/WindowInsetsController$OnControllableInsetsChangedListener;)V")
    controlWindowInsetsAnimation = JavaMethod("(IJLandroid/view/animation/Interpolator;Landroid/os/CancellationSignal;Landroid/view/WindowInsetsAnimationControlListener;)V")
    getSystemBarsAppearance = JavaMethod("()I")
    getSystemBarsBehavior = JavaMethod("()I")
    removeOnControllableInsetsChangedListener = JavaMethod("(Landroid/view/WindowInsetsController$OnControllableInsetsChangedListener;)V")
    setSystemBarsAppearance = JavaMethod("(II)V")
    setSystemBarsBehavior = JavaMethod("(I)V")
    hide = JavaMethod("(I)V")
    show = JavaMethod("(I)V")

    class OnControllableInsetsChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/WindowInsetsController$OnControllableInsetsChangedListener"
        onControllableInsetsChanged = JavaMethod("(Landroid/view/WindowInsetsController;I)V")