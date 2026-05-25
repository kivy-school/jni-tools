from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextValueSanitizer"]

class TextValueSanitizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/TextValueSanitizer"
    __javaconstructor__ = [("(Ljava/util/regex/Pattern;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")