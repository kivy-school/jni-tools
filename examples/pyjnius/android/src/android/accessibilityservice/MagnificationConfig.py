from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MagnificationConfig"]

class MagnificationConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/MagnificationConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MAGNIFICATION_MODE_DEFAULT = JavaStaticField("I")
    MAGNIFICATION_MODE_FULLSCREEN = JavaStaticField("I")
    MAGNIFICATION_MODE_WINDOW = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCenterY = JavaMethod("()F")
    getCenterX = JavaMethod("()F")
    toString = JavaMethod("()Ljava/lang/String;")
    getMode = JavaMethod("()I")
    isActivated = JavaMethod("()Z")
    getScale = JavaMethod("()F")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/MagnificationConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setCenterX = JavaMethod("(F)Landroid/accessibilityservice/MagnificationConfig$Builder;")
        setCenterY = JavaMethod("(F)Landroid/accessibilityservice/MagnificationConfig$Builder;")
        setMode = JavaMethod("(I)Landroid/accessibilityservice/MagnificationConfig$Builder;")
        setActivated = JavaMethod("(Z)Landroid/accessibilityservice/MagnificationConfig$Builder;")
        setScale = JavaMethod("(F)Landroid/accessibilityservice/MagnificationConfig$Builder;")
        build = JavaMethod("()Landroid/accessibilityservice/MagnificationConfig;")