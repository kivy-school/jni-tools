from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlinePresentationSpec"]

class InlinePresentationSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/inline/InlinePresentationSpec"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getStyle = JavaMethod("()Landroid/os/Bundle;")
    getMaxSize = JavaMethod("()Landroid/util/Size;")
    getMinSize = JavaMethod("()Landroid/util/Size;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/inline/InlinePresentationSpec$Builder"
        __javaconstructor__ = [("(Landroid/util/Size;Landroid/util/Size;)V", False)]
        build = JavaMethod("()Landroid/widget/inline/InlinePresentationSpec;")
        setStyle = JavaMethod("(Landroid/os/Bundle;)Landroid/widget/inline/InlinePresentationSpec$Builder;")