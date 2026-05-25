from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteEntry"]

class RemoteEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/RemoteEntry"
    __javaconstructor__ = [("(Landroid/app/slice/Slice;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")