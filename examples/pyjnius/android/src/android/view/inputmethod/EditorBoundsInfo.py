from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EditorBoundsInfo"]

class EditorBoundsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/EditorBoundsInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getEditorBounds = JavaMethod("()Landroid/graphics/RectF;")
    getHandwritingBounds = JavaMethod("()Landroid/graphics/RectF;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/EditorBoundsInfo$Builder"
        __javaconstructor__ = [("()V", False)]
        setEditorBounds = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/EditorBoundsInfo$Builder;")
        setHandwritingBounds = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/EditorBoundsInfo$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/EditorBoundsInfo;")