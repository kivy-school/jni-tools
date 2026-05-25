from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SharedElementCallback"]

class SharedElementCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/SharedElementCallback"
    __javaconstructor__ = [("()V", False)]
    onSharedElementStart = JavaMethod("(Ljava/util/List;Ljava/util/List;Ljava/util/List;)V")
    onSharedElementEnd = JavaMethod("(Ljava/util/List;Ljava/util/List;Ljava/util/List;)V")
    onRejectSharedElements = JavaMethod("(Ljava/util/List;)V")
    onMapSharedElements = JavaMethod("(Ljava/util/List;Ljava/util/Map;)V")
    onCaptureSharedElementSnapshot = JavaMethod("(Landroid/view/View;Landroid/graphics/Matrix;Landroid/graphics/RectF;)Landroid/os/Parcelable;")
    onCreateSnapshotView = JavaMethod("(Landroid/content/Context;Landroid/os/Parcelable;)Landroid/view/View;")
    onSharedElementsArrived = JavaMethod("(Ljava/util/List;Ljava/util/List;Landroid/app/SharedElementCallback$OnSharedElementsReadyListener;)V")

    class OnSharedElementsReadyListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/SharedElementCallback/OnSharedElementsReadyListener"
        onSharedElementsReady = JavaMethod("()V")