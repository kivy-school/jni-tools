from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoomButtonsController"]

class ZoomButtonsController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ZoomButtonsController"
    __javaconstructor__ = [("(Landroid/view/View;)V", False)]
    setZoomInEnabled = JavaMethod("(Z)V")
    setZoomOutEnabled = JavaMethod("(Z)V")
    setZoomSpeed = JavaMethod("(J)V")
    setOnZoomListener = JavaMethod("(Landroid/widget/ZoomButtonsController$OnZoomListener;)V")
    setFocusable = JavaMethod("(Z)V")
    isAutoDismissed = JavaMethod("()Z")
    setAutoDismissed = JavaMethod("(Z)V")
    isVisible = JavaMethod("()Z")
    setVisible = JavaMethod("(Z)V")
    getContainer = JavaMethod("()Landroid/view/ViewGroup;")
    getZoomControls = JavaMethod("()Landroid/view/View;")
    onTouch = JavaMethod("(Landroid/view/View;Landroid/view/MotionEvent;)Z")

    class OnZoomListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ZoomButtonsController/OnZoomListener"
        onVisibilityChanged = JavaMethod("(Z)V")
        onZoom = JavaMethod("(Z)V")