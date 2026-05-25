from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClassificationContext"]

class TextClassificationContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextClassificationContext"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getWidgetType = JavaMethod("()Ljava/lang/String;")
    getWidgetVersion = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextClassificationContext/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setWidgetVersion = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextClassificationContext$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextClassificationContext;")