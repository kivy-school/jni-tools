from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActiveProcessingPicture"]

class ActiveProcessingPicture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/quality/ActiveProcessingPicture"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getProfileId = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")