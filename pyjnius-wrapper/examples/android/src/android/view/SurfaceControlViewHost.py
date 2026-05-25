from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceControlViewHost"]

class SurfaceControlViewHost(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceControlViewHost"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/Display;Landroid/os/IBinder;)V", False), ("(Landroid/content/Context;Landroid/view/Display;Landroid/window/InputTransferToken;)V", False)]
    finalize = JavaMethod("()V")
    getSurfacePackage = JavaMethod("()Landroid/view/SurfaceControlViewHost$SurfacePackage;")
    setView = JavaMethod("(Landroid/view/View;II)V")
    getView = JavaMethod("()Landroid/view/View;")
    relayout = JavaMethod("(II)V")
    release = JavaMethod("()V")
    transferTouchGestureToHost = JavaMethod("()Z")

    class SurfacePackage(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControlViewHost/SurfacePackage"
        __javaconstructor__ = [("(Landroid/view/SurfaceControlViewHost$SurfacePackage;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getSurfaceControl = JavaMethod("()Landroid/view/SurfaceControl;")
        notifyConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
        notifyDetachedFromWindow = JavaMethod("()V")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        release = JavaMethod("()V")
        getInputTransferToken = JavaMethod("()Landroid/window/InputTransferToken;")
        toString = JavaMethod("()Ljava/lang/String;")