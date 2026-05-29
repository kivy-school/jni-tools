from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisibilitySetterAction"]

class VisibilitySetterAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/VisibilitySetterAction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/VisibilitySetterAction$Builder"
        __javaconstructor__ = [("(II)V", False)]
        setVisibility = JavaMethod("(II)Landroid/service/autofill/VisibilitySetterAction$Builder;")
        build = JavaMethod("()Landroid/service/autofill/VisibilitySetterAction;")