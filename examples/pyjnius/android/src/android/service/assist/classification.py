from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FieldClassification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/assist/classification/FieldClassification"
    __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;Ljava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHints = JavaMethod("()Ljava/util/Set;")
    toString = JavaMethod("()Ljava/lang/String;")
    getAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")