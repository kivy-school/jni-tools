from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaProjectionConfig"]

class MediaProjectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjectionConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    createConfigForDefaultDisplay = JavaStaticMethod("()Landroid/media/projection/MediaProjectionConfig;")
    createConfigForUserChoice = JavaStaticMethod("()Landroid/media/projection/MediaProjectionConfig;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")