from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlternativeSpans"]

class AlternativeSpans(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/AlternativeSpans"
    __javaconstructor__ = [("(Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSpans = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")