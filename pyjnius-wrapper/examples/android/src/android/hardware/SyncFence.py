from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncFence"]

class SyncFence(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SyncFence"
    __javaconstructor__ = [("(Landroid/hardware/SyncFence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SIGNAL_TIME_INVALID = JavaStaticField("J")
    SIGNAL_TIME_PENDING = JavaStaticField("J")
    isValid = JavaMethod("()Z")
    await = JavaMethod("(Ljava/time/Duration;)Z")
    awaitForever = JavaMethod("()Z")
    getSignalTime = JavaMethod("()J")
    close = JavaMethod("()V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")