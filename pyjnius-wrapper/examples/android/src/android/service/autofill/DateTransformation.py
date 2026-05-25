from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateTransformation"]

class DateTransformation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/DateTransformation"
    __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;Landroid/icu/text/DateFormat;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")