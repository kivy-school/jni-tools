from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlinePresentationSpec"]

class InlinePresentationSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/inline/InlinePresentationSpec"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMinSize = JavaMethod("()Landroid/util/Size;")
    getMaxSize = JavaMethod("()Landroid/util/Size;")
    getStyle = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/inline/InlinePresentationSpec/Builder"
        __javaconstructor__ = [("(Landroid/util/Size;Landroid/util/Size;)V", False)]
        setStyle = JavaMethod("(Landroid/os/Bundle;)Landroid/widget/inline/InlinePresentationSpec$Builder;")
        build = JavaMethod("()Landroid/widget/inline/InlinePresentationSpec;")