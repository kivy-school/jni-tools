from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttachedSurfaceControl"]

class AttachedSurfaceControl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/AttachedSurfaceControl"
    setTouchableRegion = JavaMethod("(Landroid/graphics/Region;)V")
    addOnBufferTransformHintChangedListener = JavaMethod("(Landroid/view/AttachedSurfaceControl$OnBufferTransformHintChangedListener;)V")
    applyTransactionOnDraw = JavaMethod("(Landroid/view/SurfaceControl$Transaction;)Z")
    buildReparentTransaction = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
    getBufferTransformHint = JavaMethod("()I")
    registerOnJankDataListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/SurfaceControl$OnJankDataListener;)Landroid/view/SurfaceControl$OnJankDataListenerRegistration;")
    removeOnBufferTransformHintChangedListener = JavaMethod("(Landroid/view/AttachedSurfaceControl$OnBufferTransformHintChangedListener;)V")
    setChildBoundingInsets = JavaMethod("(Landroid/graphics/Rect;)V")
    getInputTransferToken = JavaMethod("()Landroid/window/InputTransferToken;")

    class OnBufferTransformHintChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/AttachedSurfaceControl$OnBufferTransformHintChangedListener"
        onBufferTransformHintChanged = JavaMethod("(I)V")