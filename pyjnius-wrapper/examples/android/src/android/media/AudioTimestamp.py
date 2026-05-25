from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioTimestamp"]

class AudioTimestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioTimestamp"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TIMEBASE_BOOTTIME = JavaStaticField("I")
    TIMEBASE_MONOTONIC = JavaStaticField("I")
    framePosition = JavaField("J")
    nanoTime = JavaField("J")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")