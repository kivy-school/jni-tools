from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewTranslationRequest"]

class ViewTranslationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/ViewTranslationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ID_TEXT = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getValue = JavaMethod("(Ljava/lang/String;)Landroid/view/translation/TranslationRequestValue;")
    getAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    getKeys = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/ViewTranslationRequest$Builder"
        __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;)V", False), ("(Landroid/view/autofill/AutofillId;J)V", False)]
        setValue = JavaMethod("(Ljava/lang/String;Landroid/view/translation/TranslationRequestValue;)Landroid/view/translation/ViewTranslationRequest$Builder;")
        build = JavaMethod("()Landroid/view/translation/ViewTranslationRequest;")