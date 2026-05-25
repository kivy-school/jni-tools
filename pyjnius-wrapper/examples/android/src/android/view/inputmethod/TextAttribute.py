from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextAttribute"]

class TextAttribute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/TextAttribute"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTextConversionSuggestions = JavaMethod("()Ljava/util/List;")
    getExtras = JavaMethod("()Landroid/os/PersistableBundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/TextAttribute/Builder"
        __javaconstructor__ = [("()V", False)]
        setTextConversionSuggestions = JavaMethod("(Ljava/util/List;)Landroid/view/inputmethod/TextAttribute$Builder;")
        setExtras = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/view/inputmethod/TextAttribute$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/TextAttribute;")