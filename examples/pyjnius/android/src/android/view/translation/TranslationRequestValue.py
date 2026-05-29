from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationRequestValue"]

class TranslationRequestValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationRequestValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    forText = JavaStaticMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationRequestValue;")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")