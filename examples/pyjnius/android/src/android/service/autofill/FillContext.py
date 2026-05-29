from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillContext"]

class FillContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillContext"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getFocusedId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    getRequestId = JavaMethod("()I")
    getStructure = JavaMethod("()Landroid/app/assist/AssistStructure;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")