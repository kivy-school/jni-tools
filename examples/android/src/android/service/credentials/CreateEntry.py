from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateEntry"]

class CreateEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CreateEntry"
    __javaconstructor__ = [("(Landroid/app/slice/Slice;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")