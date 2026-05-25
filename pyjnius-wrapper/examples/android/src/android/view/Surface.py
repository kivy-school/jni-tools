from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Surface"]

class Surface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/Surface"
    __javaconstructor__ = [("(Landroid/view/SurfaceControl;)V", False), ("(Landroid/graphics/SurfaceTexture;)V", False)]
    CHANGE_FRAME_RATE_ALWAYS = JavaStaticField("I")
    CHANGE_FRAME_RATE_ONLY_IF_SEAMLESS = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FRAME_RATE_COMPATIBILITY_DEFAULT = JavaStaticField("I")
    FRAME_RATE_COMPATIBILITY_FIXED_SOURCE = JavaStaticField("I")
    ROTATION_0 = JavaStaticField("I")
    ROTATION_180 = JavaStaticField("I")
    ROTATION_270 = JavaStaticField("I")
    ROTATION_90 = JavaStaticField("I")
    finalize = JavaMethod("()V")
    release = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    lockCanvas = JavaMethod("(Landroid/graphics/Rect;)Landroid/graphics/Canvas;")
    unlockCanvasAndPost = JavaMethod("(Landroid/graphics/Canvas;)V")
    lockHardwareCanvas = JavaMethod("()Landroid/graphics/Canvas;")
    unlockCanvas = JavaMethod("(Landroid/graphics/Canvas;)V")
    describeContents = JavaMethod("()I")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    setFrameRate = JavaMultipleMethod([("(FII)V", False, False), ("(FI)V", False, False)])
    clearFrameRate = JavaMethod("()V")

    class OutOfResourcesException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Surface/OutOfResourcesException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]