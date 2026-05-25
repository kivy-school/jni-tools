from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdSelectionSignals"]

class AdSelectionSignals(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdSelectionSignals"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY = JavaStaticField("Landroid/adservices/common/AdSelectionSignals;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/adservices/common/AdSelectionSignals;")