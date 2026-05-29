from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaProjectionConfig"]

class MediaProjectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjectionConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    createConfigForDefaultDisplay = JavaStaticMethod("()Landroid/media/projection/MediaProjectionConfig;")
    createConfigForUserChoice = JavaStaticMethod("()Landroid/media/projection/MediaProjectionConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")