from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutofillValue"]

class AutofillValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/autofill/AutofillValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    forDate = JavaStaticMethod("(J)Landroid/view/autofill/AutofillValue;")
    forText = JavaStaticMethod("(Ljava/lang/CharSequence;)Landroid/view/autofill/AutofillValue;")
    forToggle = JavaStaticMethod("(Z)Landroid/view/autofill/AutofillValue;")
    getListValue = JavaMethod("()I")
    getTextValue = JavaMethod("()Ljava/lang/CharSequence;")
    getToggleValue = JavaMethod("()Z")
    isDate = JavaMethod("()Z")
    isList = JavaMethod("()Z")
    isText = JavaMethod("()Z")
    isToggle = JavaMethod("()Z")
    forList = JavaStaticMethod("(I)Landroid/view/autofill/AutofillValue;")
    getDateValue = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")