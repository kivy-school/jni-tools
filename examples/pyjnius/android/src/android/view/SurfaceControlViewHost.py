from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceControlViewHost"]

class SurfaceControlViewHost(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceControlViewHost"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/Display;Landroid/os/IBinder;)V", False), ("(Landroid/content/Context;Landroid/view/Display;Landroid/window/InputTransferToken;)V", False)]
    release = JavaMethod("()V")
    transferTouchGestureToHost = JavaMethod("()Z")
    relayout = JavaMethod("(II)V")
    getSurfacePackage = JavaMethod("()Landroid/view/SurfaceControlViewHost$SurfacePackage;")
    getView = JavaMethod("()Landroid/view/View;")
    setView = JavaMethod("(Landroid/view/View;II)V")

    class SurfacePackage(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControlViewHost$SurfacePackage"
        __javaconstructor__ = [("(Landroid/view/SurfaceControlViewHost$SurfacePackage;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        toString = JavaMethod("()Ljava/lang/String;")
        release = JavaMethod("()V")
        notifyConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
        getInputTransferToken = JavaMethod("()Landroid/window/InputTransferToken;")
        notifyDetachedFromWindow = JavaMethod("()V")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getSurfaceControl = JavaMethod("()Landroid/view/SurfaceControl;")