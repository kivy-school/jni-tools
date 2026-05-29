from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SharedElementCallback"]

class SharedElementCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/SharedElementCallback"
    __javaconstructor__ = [("()V", False)]
    onCaptureSharedElementSnapshot = JavaMethod("(Landroid/view/View;Landroid/graphics/Matrix;Landroid/graphics/RectF;)Landroid/os/Parcelable;")
    onCreateSnapshotView = JavaMethod("(Landroid/content/Context;Landroid/os/Parcelable;)Landroid/view/View;")
    onMapSharedElements = JavaMethod("(Ljava/util/List;Ljava/util/Map;)V")
    onRejectSharedElements = JavaMethod("(Ljava/util/List;)V")
    onSharedElementEnd = JavaMethod("(Ljava/util/List;Ljava/util/List;Ljava/util/List;)V")
    onSharedElementStart = JavaMethod("(Ljava/util/List;Ljava/util/List;Ljava/util/List;)V")
    onSharedElementsArrived = JavaMethod("(Ljava/util/List;Ljava/util/List;Landroid/app/SharedElementCallback$OnSharedElementsReadyListener;)V")

    class OnSharedElementsReadyListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/SharedElementCallback$OnSharedElementsReadyListener"
        onSharedElementsReady = JavaMethod("()V")