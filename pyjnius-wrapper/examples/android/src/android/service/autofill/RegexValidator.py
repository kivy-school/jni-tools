from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RegexValidator"]

class RegexValidator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/RegexValidator"
    __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;Ljava/util/regex/Pattern;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")