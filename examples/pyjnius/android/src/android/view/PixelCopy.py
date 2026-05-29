from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PixelCopy"]

class PixelCopy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/PixelCopy"
    ERROR_DESTINATION_INVALID = JavaStaticField("I")
    ERROR_SOURCE_INVALID = JavaStaticField("I")
    ERROR_SOURCE_NO_DATA = JavaStaticField("I")
    ERROR_TIMEOUT = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    SUCCESS = JavaStaticField("I")
    request = JavaMultipleMethod([("(Landroid/view/SurfaceView;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/SurfaceView;Landroid/graphics/Rect;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Surface;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Surface;Landroid/graphics/Rect;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Window;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Window;Landroid/graphics/Rect;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/PixelCopy$Request;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V", True, False)])

    class OnPixelCopyFinishedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/PixelCopy/OnPixelCopyFinishedListener"
        onPixelCopyFinished = JavaMethod("(I)V")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/PixelCopy/Request"
        getDestinationBitmap = JavaMethod("()Landroid/graphics/Bitmap;")
        getSourceRect = JavaMethod("()Landroid/graphics/Rect;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/PixelCopy/Request/Builder"
            ofWindow = JavaMultipleMethod([("(Landroid/view/Window;)Landroid/view/PixelCopy$Request$Builder;", True, False), ("(Landroid/view/View;)Landroid/view/PixelCopy$Request$Builder;", True, False)])
            ofSurface = JavaMultipleMethod([("(Landroid/view/Surface;)Landroid/view/PixelCopy$Request$Builder;", True, False), ("(Landroid/view/SurfaceView;)Landroid/view/PixelCopy$Request$Builder;", True, False)])
            setSourceRect = JavaMethod("(Landroid/graphics/Rect;)Landroid/view/PixelCopy$Request$Builder;")
            setDestinationBitmap = JavaMethod("(Landroid/graphics/Bitmap;)Landroid/view/PixelCopy$Request$Builder;")
            build = JavaMethod("()Landroid/view/PixelCopy$Request;")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/PixelCopy/Result"
        getStatus = JavaMethod("()I")
        getBitmap = JavaMethod("()Landroid/graphics/Bitmap;")