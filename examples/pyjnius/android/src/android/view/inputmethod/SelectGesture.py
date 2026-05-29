from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectGesture"]

class SelectGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/SelectGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    getSelectionArea = JavaMethod("()Landroid/graphics/RectF;")
    getGranularity = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/SelectGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/SelectGesture$Builder;")
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/SelectGesture$Builder;")
        setSelectionArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/SelectGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/SelectGesture;")