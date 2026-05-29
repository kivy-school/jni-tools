from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PictureInPictureParams"]

class PictureInPictureParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/PictureInPictureParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getActions = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    isAutoEnterEnabled = JavaMethod("()Z")
    getSourceRectHint = JavaMethod("()Landroid/graphics/Rect;")
    getCloseAction = JavaMethod("()Landroid/app/RemoteAction;")
    getAspectRatio = JavaMethod("()Landroid/util/Rational;")
    getExpandedAspectRatio = JavaMethod("()Landroid/util/Rational;")
    isSeamlessResizeEnabled = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/PictureInPictureParams$Builder"
        __javaconstructor__ = [("(Landroid/app/PictureInPictureParams;)V", False), ("()V", False)]
        setActions = JavaMethod("(Ljava/util/List;)Landroid/app/PictureInPictureParams$Builder;")
        setAspectRatio = JavaMethod("(Landroid/util/Rational;)Landroid/app/PictureInPictureParams$Builder;")
        setAutoEnterEnabled = JavaMethod("(Z)Landroid/app/PictureInPictureParams$Builder;")
        setCloseAction = JavaMethod("(Landroid/app/RemoteAction;)Landroid/app/PictureInPictureParams$Builder;")
        setExpandedAspectRatio = JavaMethod("(Landroid/util/Rational;)Landroid/app/PictureInPictureParams$Builder;")
        setSourceRectHint = JavaMethod("(Landroid/graphics/Rect;)Landroid/app/PictureInPictureParams$Builder;")
        setSeamlessResizeEnabled = JavaMethod("(Z)Landroid/app/PictureInPictureParams$Builder;")
        setSubtitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/PictureInPictureParams$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/PictureInPictureParams$Builder;")
        build = JavaMethod("()Landroid/app/PictureInPictureParams;")