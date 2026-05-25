from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Face"]

class Face(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/Face"
    ID_UNSUPPORTED = JavaStaticField("I")
    SCORE_MAX = JavaStaticField("I")
    SCORE_MIN = JavaStaticField("I")
    getBounds = JavaMethod("()Landroid/graphics/Rect;")
    getScore = JavaMethod("()I")
    getId = JavaMethod("()I")
    getLeftEyePosition = JavaMethod("()Landroid/graphics/Point;")
    getRightEyePosition = JavaMethod("()Landroid/graphics/Point;")
    getMouthPosition = JavaMethod("()Landroid/graphics/Point;")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/params/Face/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/hardware/camera2/params/Face;)V", False)]
        setBounds = JavaMethod("(Landroid/graphics/Rect;)Landroid/hardware/camera2/params/Face$Builder;")
        setScore = JavaMethod("(I)Landroid/hardware/camera2/params/Face$Builder;")
        setId = JavaMethod("(I)Landroid/hardware/camera2/params/Face$Builder;")
        setLeftEyePosition = JavaMethod("(Landroid/graphics/Point;)Landroid/hardware/camera2/params/Face$Builder;")
        setRightEyePosition = JavaMethod("(Landroid/graphics/Point;)Landroid/hardware/camera2/params/Face$Builder;")
        setMouthPosition = JavaMethod("(Landroid/graphics/Point;)Landroid/hardware/camera2/params/Face$Builder;")
        build = JavaMethod("()Landroid/hardware/camera2/params/Face;")