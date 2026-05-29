from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewTranslationResponse"]

class ViewTranslationResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/ViewTranslationResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getValue = JavaMethod("(Ljava/lang/String;)Landroid/view/translation/TranslationResponseValue;")
    getAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    getKeys = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/ViewTranslationResponse$Builder"
        __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;)V", False)]
        setValue = JavaMethod("(Ljava/lang/String;Landroid/view/translation/TranslationResponseValue;)Landroid/view/translation/ViewTranslationResponse$Builder;")
        build = JavaMethod("()Landroid/view/translation/ViewTranslationResponse;")