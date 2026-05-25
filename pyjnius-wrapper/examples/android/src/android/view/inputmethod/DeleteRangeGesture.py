from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeleteRangeGesture"]

class DeleteRangeGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/DeleteRangeGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getGranularity = JavaMethod("()I")
    getDeletionStartArea = JavaMethod("()Landroid/graphics/RectF;")
    getDeletionEndArea = JavaMethod("()Landroid/graphics/RectF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/DeleteRangeGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        setDeletionStartArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        setDeletionEndArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/DeleteRangeGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/DeleteRangeGesture;")