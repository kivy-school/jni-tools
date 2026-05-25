from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlinePresentation"]

class InlinePresentation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/InlinePresentation"
    __javaconstructor__ = [("(Landroid/app/slice/Slice;Landroid/widget/inline/InlinePresentationSpec;Z)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    createTooltipPresentation = JavaStaticMethod("(Landroid/app/slice/Slice;Landroid/widget/inline/InlinePresentationSpec;)Landroid/service/autofill/InlinePresentation;")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")
    getInlinePresentationSpec = JavaMethod("()Landroid/widget/inline/InlinePresentationSpec;")
    isPinned = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")