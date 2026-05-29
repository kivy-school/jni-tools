from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationResponseValue"]

class TranslationResponseValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationResponseValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_DEFINITIONS = JavaStaticField("Ljava/lang/String;")
    STATUS_ERROR = JavaStaticField("I")
    STATUS_SUCCESS = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    forError = JavaStaticMethod("()Landroid/view/translation/TranslationResponseValue;")
    getTransliteration = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getStatusCode = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/CharSequence;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationResponseValue$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setTransliteration = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationResponseValue$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/translation/TranslationResponseValue$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationResponseValue;")
        setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationResponseValue$Builder;")