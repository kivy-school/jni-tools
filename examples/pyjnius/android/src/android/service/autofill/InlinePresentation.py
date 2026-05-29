from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlinePresentation"]

class InlinePresentation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/InlinePresentation"
    __javaconstructor__ = [("(Landroid/app/slice/Slice;Landroid/widget/inline/InlinePresentationSpec;Z)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")
    createTooltipPresentation = JavaStaticMethod("(Landroid/app/slice/Slice;Landroid/widget/inline/InlinePresentationSpec;)Landroid/service/autofill/InlinePresentation;")
    getInlinePresentationSpec = JavaMethod("()Landroid/widget/inline/InlinePresentationSpec;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isPinned = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")