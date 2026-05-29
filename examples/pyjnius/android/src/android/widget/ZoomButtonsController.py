from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoomButtonsController"]

class ZoomButtonsController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ZoomButtonsController"
    __javaconstructor__ = [("(Landroid/view/View;)V", False)]
    isVisible = JavaMethod("()Z")
    setFocusable = JavaMethod("(Z)V")
    onTouch = JavaMethod("(Landroid/view/View;Landroid/view/MotionEvent;)Z")
    setZoomSpeed = JavaMethod("(J)V")
    setVisible = JavaMethod("(Z)V")
    setAutoDismissed = JavaMethod("(Z)V")
    setOnZoomListener = JavaMethod("(Landroid/widget/ZoomButtonsController$OnZoomListener;)V")
    isAutoDismissed = JavaMethod("()Z")
    getContainer = JavaMethod("()Landroid/view/ViewGroup;")
    getZoomControls = JavaMethod("()Landroid/view/View;")
    setZoomInEnabled = JavaMethod("(Z)V")
    setZoomOutEnabled = JavaMethod("(Z)V")

    class OnZoomListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ZoomButtonsController$OnZoomListener"
        onVisibilityChanged = JavaMethod("(Z)V")
        onZoom = JavaMethod("(Z)V")