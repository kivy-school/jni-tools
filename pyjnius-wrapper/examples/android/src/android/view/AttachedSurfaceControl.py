from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttachedSurfaceControl"]

class AttachedSurfaceControl(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/AttachedSurfaceControl"
    buildReparentTransaction = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
    applyTransactionOnDraw = JavaMethod("(Landroid/view/SurfaceControl$Transaction;)Z")
    getBufferTransformHint = JavaMethod("()I")
    addOnBufferTransformHintChangedListener = JavaMethod("(Landroid/view/AttachedSurfaceControl$OnBufferTransformHintChangedListener;)V")
    removeOnBufferTransformHintChangedListener = JavaMethod("(Landroid/view/AttachedSurfaceControl$OnBufferTransformHintChangedListener;)V")
    setTouchableRegion = JavaMethod("(Landroid/graphics/Region;)V")
    setChildBoundingInsets = JavaMethod("(Landroid/graphics/Rect;)V")
    getInputTransferToken = JavaMethod("()Landroid/window/InputTransferToken;")

    class OnBufferTransformHintChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/AttachedSurfaceControl/OnBufferTransformHintChangedListener"
        onBufferTransformHintChanged = JavaMethod("(I)V")