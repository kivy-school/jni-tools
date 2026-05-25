from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeleteGesture"]

class DeleteGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/DeleteGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getGranularity = JavaMethod("()I")
    getDeletionArea = JavaMethod("()Landroid/graphics/RectF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/DeleteGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/DeleteGesture$Builder;")
        setDeletionArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/DeleteGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/DeleteGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/DeleteGesture;")