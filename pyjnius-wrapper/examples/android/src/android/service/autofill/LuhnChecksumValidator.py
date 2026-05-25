from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LuhnChecksumValidator"]

class LuhnChecksumValidator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/LuhnChecksumValidator"
    __javaconstructor__ = [("([Landroid/view/autofill/AutofillId;)V", True)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")