from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectRangeGesture"]

class SelectRangeGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/SelectRangeGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    getGranularity = JavaMethod("()I")
    getSelectionEndArea = JavaMethod("()Landroid/graphics/RectF;")
    getSelectionStartArea = JavaMethod("()Landroid/graphics/RectF;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/SelectRangeGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        setSelectionEndArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        setSelectionStartArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/SelectRangeGesture;")