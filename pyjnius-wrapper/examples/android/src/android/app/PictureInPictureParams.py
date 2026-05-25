from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PictureInPictureParams"]

class PictureInPictureParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/PictureInPictureParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAspectRatio = JavaMethod("()Landroid/util/Rational;")
    getExpandedAspectRatio = JavaMethod("()Landroid/util/Rational;")
    getActions = JavaMethod("()Ljava/util/List;")
    getCloseAction = JavaMethod("()Landroid/app/RemoteAction;")
    getSourceRectHint = JavaMethod("()Landroid/graphics/Rect;")
    isAutoEnterEnabled = JavaMethod("()Z")
    isSeamlessResizeEnabled = JavaMethod("()Z")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/PictureInPictureParams/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/app/PictureInPictureParams;)V", False)]
        setAspectRatio = JavaMethod("(Landroid/util/Rational;)Landroid/app/PictureInPictureParams$Builder;")
        setExpandedAspectRatio = JavaMethod("(Landroid/util/Rational;)Landroid/app/PictureInPictureParams$Builder;")
        setActions = JavaMethod("(Ljava/util/List;)Landroid/app/PictureInPictureParams$Builder;")
        setCloseAction = JavaMethod("(Landroid/app/RemoteAction;)Landroid/app/PictureInPictureParams$Builder;")
        setSourceRectHint = JavaMethod("(Landroid/graphics/Rect;)Landroid/app/PictureInPictureParams$Builder;")
        setAutoEnterEnabled = JavaMethod("(Z)Landroid/app/PictureInPictureParams$Builder;")
        setSeamlessResizeEnabled = JavaMethod("(Z)Landroid/app/PictureInPictureParams$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/PictureInPictureParams$Builder;")
        setSubtitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/PictureInPictureParams$Builder;")
        build = JavaMethod("()Landroid/app/PictureInPictureParams;")