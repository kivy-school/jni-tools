from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Surface"]

class Surface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/Surface"
    __javaconstructor__ = [("(Landroid/graphics/SurfaceTexture;)V", False), ("(Landroid/view/SurfaceControl;)V", False)]
    CHANGE_FRAME_RATE_ALWAYS = JavaStaticField("I")
    CHANGE_FRAME_RATE_ONLY_IF_SEAMLESS = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FRAME_RATE_COMPATIBILITY_AT_LEAST = JavaStaticField("I")
    FRAME_RATE_COMPATIBILITY_DEFAULT = JavaStaticField("I")
    FRAME_RATE_COMPATIBILITY_FIXED_SOURCE = JavaStaticField("I")
    ROTATION_0 = JavaStaticField("I")
    ROTATION_180 = JavaStaticField("I")
    ROTATION_270 = JavaStaticField("I")
    ROTATION_90 = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    release = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    clearFrameRate = JavaMethod("()V")
    lockCanvas = JavaMethod("(Landroid/graphics/Rect;)Landroid/graphics/Canvas;")
    lockHardwareCanvas = JavaMethod("()Landroid/graphics/Canvas;")
    setFrameRate = JavaMultipleMethod([("(FII)V", False, False), ("(FI)V", False, False)])
    unlockCanvas = JavaMethod("(Landroid/graphics/Canvas;)V")
    unlockCanvasAndPost = JavaMethod("(Landroid/graphics/Canvas;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")
    describeContents = JavaMethod("()I")

    class OutOfResourcesException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Surface$OutOfResourcesException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]