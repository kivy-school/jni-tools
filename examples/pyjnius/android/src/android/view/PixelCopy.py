from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PixelCopy"]

class PixelCopy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/PixelCopy"
    ERROR_DESTINATION_INVALID = JavaStaticField("I")
    ERROR_SOURCE_INVALID = JavaStaticField("I")
    ERROR_SOURCE_NO_DATA = JavaStaticField("I")
    ERROR_TIMEOUT = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    SUCCESS = JavaStaticField("I")
    request = JavaMultipleMethod([("(Landroid/view/SurfaceView;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/SurfaceView;Landroid/graphics/Rect;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Window;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Window;Landroid/graphics/Rect;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Surface;Landroid/graphics/Rect;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/Surface;Landroid/graphics/Bitmap;Landroid/view/PixelCopy$OnPixelCopyFinishedListener;Landroid/os/Handler;)V", True, False), ("(Landroid/view/PixelCopy$Request;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V", True, False)])

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/PixelCopy$Result"
        getStatus = JavaMethod("()I")
        getBitmap = JavaMethod("()Landroid/graphics/Bitmap;")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/PixelCopy$Request"
        getSourceRect = JavaMethod("()Landroid/graphics/Rect;")
        getDestinationBitmap = JavaMethod("()Landroid/graphics/Bitmap;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/PixelCopy$Request$Builder"
            ofSurface = JavaMultipleMethod([("(Landroid/view/Surface;)Landroid/view/PixelCopy$Request$Builder;", True, False), ("(Landroid/view/SurfaceView;)Landroid/view/PixelCopy$Request$Builder;", True, False)])
            ofWindow = JavaMultipleMethod([("(Landroid/view/View;)Landroid/view/PixelCopy$Request$Builder;", True, False), ("(Landroid/view/Window;)Landroid/view/PixelCopy$Request$Builder;", True, False)])
            setSourceRect = JavaMethod("(Landroid/graphics/Rect;)Landroid/view/PixelCopy$Request$Builder;")
            setDestinationBitmap = JavaMethod("(Landroid/graphics/Bitmap;)Landroid/view/PixelCopy$Request$Builder;")
            build = JavaMethod("()Landroid/view/PixelCopy$Request;")

    class OnPixelCopyFinishedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/PixelCopy$OnPixelCopyFinishedListener"
        onPixelCopyFinished = JavaMethod("(I)V")