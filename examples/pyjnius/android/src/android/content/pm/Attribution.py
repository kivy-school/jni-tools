from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attribution"]

class Attribution(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/Attribution"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTag = JavaMethod("()Ljava/lang/String;")
    getLabel = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")