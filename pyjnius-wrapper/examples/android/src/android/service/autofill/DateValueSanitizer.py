from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateValueSanitizer"]

class DateValueSanitizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/DateValueSanitizer"
    __javaconstructor__ = [("(Landroid/icu/text/DateFormat;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")