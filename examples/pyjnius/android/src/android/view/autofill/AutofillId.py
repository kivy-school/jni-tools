from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutofillId"]

class AutofillId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/autofill/AutofillId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isInAutofillSession = JavaMethod("()Z")
    getAutofillVirtualId = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isVirtual = JavaMethod("()Z")
    create = JavaStaticMethod("(Landroid/view/View;I)Landroid/view/autofill/AutofillId;")
    getViewId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSessionId = JavaMethod("()I")