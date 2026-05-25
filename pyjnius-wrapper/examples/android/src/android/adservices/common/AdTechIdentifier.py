from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdTechIdentifier"]

class AdTechIdentifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdTechIdentifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/adservices/common/AdTechIdentifier;")