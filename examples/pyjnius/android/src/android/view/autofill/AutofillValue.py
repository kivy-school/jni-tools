from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutofillValue"]

class AutofillValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/autofill/AutofillValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTextValue = JavaMethod("()Ljava/lang/CharSequence;")
    isText = JavaMethod("()Z")
    getToggleValue = JavaMethod("()Z")
    isToggle = JavaMethod("()Z")
    getListValue = JavaMethod("()I")
    isList = JavaMethod("()Z")
    getDateValue = JavaMethod("()J")
    isDate = JavaMethod("()Z")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    forText = JavaStaticMethod("(Ljava/lang/CharSequence;)Landroid/view/autofill/AutofillValue;")
    forToggle = JavaStaticMethod("(Z)Landroid/view/autofill/AutofillValue;")
    forList = JavaStaticMethod("(I)Landroid/view/autofill/AutofillValue;")
    forDate = JavaStaticMethod("(J)Landroid/view/autofill/AutofillValue;")