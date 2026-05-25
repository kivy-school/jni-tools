from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationSpec"]

class TranslationSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationSpec"
    __javaconstructor__ = [("(Landroid/icu/util/ULocale;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DATA_FORMAT_TEXT = JavaStaticField("I")
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")
    getDataFormat = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")