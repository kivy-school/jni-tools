from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationContext"]

class TranslationContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationContext"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_DEFINITIONS = JavaStaticField("I")
    FLAG_LOW_LATENCY = JavaStaticField("I")
    FLAG_TRANSLITERATION = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSourceSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    getTargetSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    getTranslationFlags = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationContext$Builder"
        __javaconstructor__ = [("(Landroid/view/translation/TranslationSpec;Landroid/view/translation/TranslationSpec;)V", False)]
        setTranslationFlags = JavaMethod("(I)Landroid/view/translation/TranslationContext$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationContext;")