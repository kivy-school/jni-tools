from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateEntry"]

class CreateEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CreateEntry"
    __javaconstructor__ = [("(Landroid/app/slice/Slice;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")