from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillContext"]

class FillContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillContext"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    getRequestId = JavaMethod("()I")
    getStructure = JavaMethod("()Landroid/app/assist/AssistStructure;")
    getFocusedId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")