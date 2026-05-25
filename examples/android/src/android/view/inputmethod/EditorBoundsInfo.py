from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EditorBoundsInfo"]

class EditorBoundsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/EditorBoundsInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getEditorBounds = JavaMethod("()Landroid/graphics/RectF;")
    getHandwritingBounds = JavaMethod("()Landroid/graphics/RectF;")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/EditorBoundsInfo/Builder"
        __javaconstructor__ = [("()V", False)]
        setEditorBounds = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/EditorBoundsInfo$Builder;")
        setHandwritingBounds = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/EditorBoundsInfo$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/EditorBoundsInfo;")