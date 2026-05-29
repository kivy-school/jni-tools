from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextAttribute"]

class TextAttribute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/TextAttribute"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTextConversionSuggestions = JavaMethod("()Ljava/util/List;")
    getExtras = JavaMethod("()Landroid/os/PersistableBundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/TextAttribute$Builder"
        __javaconstructor__ = [("()V", False)]
        setExtras = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/view/inputmethod/TextAttribute$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/TextAttribute;")
        setTextConversionSuggestions = JavaMethod("(Ljava/util/List;)Landroid/view/inputmethod/TextAttribute$Builder;")