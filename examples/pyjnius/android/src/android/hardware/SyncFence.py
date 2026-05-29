from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncFence"]

class SyncFence(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SyncFence"
    __javaconstructor__ = [("(Landroid/hardware/SyncFence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SIGNAL_TIME_INVALID = JavaStaticField("J")
    SIGNAL_TIME_PENDING = JavaStaticField("J")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    close = JavaMethod("()V")
    await = JavaMethod("(Ljava/time/Duration;)Z")
    isValid = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSignalTime = JavaMethod("()J")
    awaitForever = JavaMethod("()Z")