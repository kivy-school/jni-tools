from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlternativeSpan"]

class AlternativeSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/AlternativeSpan"
    __javaconstructor__ = [("(IILjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getStartPosition = JavaMethod("()I")
    getEndPosition = JavaMethod("()I")
    getAlternatives = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")