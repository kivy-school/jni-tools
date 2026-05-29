from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationSpec"]

class TranslationSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationSpec"
    __javaconstructor__ = [("(Landroid/icu/util/ULocale;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DATA_FORMAT_TEXT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDataFormat = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")