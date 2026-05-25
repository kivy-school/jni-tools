from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FieldClassification"]

class FieldClassification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/assist/classification/FieldClassification"
    __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;Ljava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    getHints = JavaMethod("()Ljava/util/Set;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")