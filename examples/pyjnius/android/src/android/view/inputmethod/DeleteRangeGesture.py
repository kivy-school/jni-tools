from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeleteRangeGesture"]

class DeleteRangeGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/DeleteRangeGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    getDeletionEndArea = JavaMethod("()Landroid/graphics/RectF;")
    getDeletionStartArea = JavaMethod("()Landroid/graphics/RectF;")
    getGranularity = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/DeleteRangeGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setDeletionEndArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        setDeletionStartArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/DeleteRangeGesture;")