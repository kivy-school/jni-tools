from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutofillId"]

class AutofillId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/autofill/AutofillId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    create = JavaStaticMethod("(Landroid/view/View;I)Landroid/view/autofill/AutofillId;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")