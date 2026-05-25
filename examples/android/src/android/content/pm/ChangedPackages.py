from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangedPackages"]

class ChangedPackages(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ChangedPackages"
    __javaconstructor__ = [("(ILjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSequenceNumber = JavaMethod("()I")
    getPackageNames = JavaMethod("()Ljava/util/List;")