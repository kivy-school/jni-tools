from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class MediaProjectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjectionConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    createConfigForUserChoice = JavaStaticMethod("()Landroid/media/projection/MediaProjectionConfig;")
    createConfigForDefaultDisplay = JavaStaticMethod("()Landroid/media/projection/MediaProjectionConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class MediaProjection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjection"
    registerCallback = JavaMethod("(Landroid/media/projection/MediaProjection$Callback;Landroid/os/Handler;)V")
    unregisterCallback = JavaMethod("(Landroid/media/projection/MediaProjection$Callback;)V")
    createVirtualDisplay = JavaMethod("(Ljava/lang/String;IIIILandroid/view/Surface;Landroid/hardware/display/VirtualDisplay$Callback;Landroid/os/Handler;)Landroid/hardware/display/VirtualDisplay;")
    stop = JavaMethod("()V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/projection/MediaProjection$Callback"
        __javaconstructor__ = [("()V", False)]
        onCapturedContentResize = JavaMethod("(II)V")
        onCapturedContentVisibilityChanged = JavaMethod("(Z)V")
        onStop = JavaMethod("()V")

class MediaProjectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjectionManager"
    getMediaProjection = JavaMethod("(ILandroid/content/Intent;)Landroid/media/projection/MediaProjection;")
    createScreenCaptureIntent = JavaMultipleMethod([("(Landroid/media/projection/MediaProjectionConfig;)Landroid/content/Intent;", False, False), ("()Landroid/content/Intent;", False, False)])