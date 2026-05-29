from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Tag"]

class Tag(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/Tag"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTechList = JavaMethod("()[Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()[B")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")