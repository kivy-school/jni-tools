from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangedPackages"]

class ChangedPackages(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ChangedPackages"
    __javaconstructor__ = [("(ILjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPackageNames = JavaMethod("()Ljava/util/List;")
    getSequenceNumber = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")