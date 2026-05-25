from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisibilitySetterAction"]

class VisibilitySetterAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/VisibilitySetterAction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/VisibilitySetterAction/Builder"
        __javaconstructor__ = [("(II)V", False)]
        setVisibility = JavaMethod("(II)Landroid/service/autofill/VisibilitySetterAction$Builder;")
        build = JavaMethod("()Landroid/service/autofill/VisibilitySetterAction;")