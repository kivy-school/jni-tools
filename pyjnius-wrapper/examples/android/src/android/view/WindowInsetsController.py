from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowInsetsController"]

class WindowInsetsController(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowInsetsController"
    APPEARANCE_LIGHT_CAPTION_BARS = JavaStaticField("I")
    APPEARANCE_LIGHT_NAVIGATION_BARS = JavaStaticField("I")
    APPEARANCE_LIGHT_STATUS_BARS = JavaStaticField("I")
    APPEARANCE_TRANSPARENT_CAPTION_BAR_BACKGROUND = JavaStaticField("I")
    BEHAVIOR_DEFAULT = JavaStaticField("I")
    BEHAVIOR_SHOW_BARS_BY_SWIPE = JavaStaticField("I")
    BEHAVIOR_SHOW_BARS_BY_TOUCH = JavaStaticField("I")
    BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE = JavaStaticField("I")
    show = JavaMethod("(I)V")
    hide = JavaMethod("(I)V")
    controlWindowInsetsAnimation = JavaMethod("(IJLandroid/view/animation/Interpolator;Landroid/os/CancellationSignal;Landroid/view/WindowInsetsAnimationControlListener;)V")
    setSystemBarsAppearance = JavaMethod("(II)V")
    getSystemBarsAppearance = JavaMethod("()I")
    setSystemBarsBehavior = JavaMethod("(I)V")
    getSystemBarsBehavior = JavaMethod("()I")
    addOnControllableInsetsChangedListener = JavaMethod("(Landroid/view/WindowInsetsController$OnControllableInsetsChangedListener;)V")
    removeOnControllableInsetsChangedListener = JavaMethod("(Landroid/view/WindowInsetsController$OnControllableInsetsChangedListener;)V")

    class OnControllableInsetsChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/WindowInsetsController/OnControllableInsetsChangedListener"
        onControllableInsetsChanged = JavaMethod("(Landroid/view/WindowInsetsController;I)V")