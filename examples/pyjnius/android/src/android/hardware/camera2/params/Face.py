from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Face"]

class Face(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/Face"
    ID_UNSUPPORTED = JavaStaticField("I")
    SCORE_MAX = JavaStaticField("I")
    SCORE_MIN = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getBounds = JavaMethod("()Landroid/graphics/Rect;")
    getId = JavaMethod("()I")
    getScore = JavaMethod("()I")
    getMouthPosition = JavaMethod("()Landroid/graphics/Point;")
    getRightEyePosition = JavaMethod("()Landroid/graphics/Point;")
    getLeftEyePosition = JavaMethod("()Landroid/graphics/Point;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/params/Face$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/hardware/camera2/params/Face;)V", False)]
        setMouthPosition = JavaMethod("(Landroid/graphics/Point;)Landroid/hardware/camera2/params/Face$Builder;")
        setLeftEyePosition = JavaMethod("(Landroid/graphics/Point;)Landroid/hardware/camera2/params/Face$Builder;")
        setRightEyePosition = JavaMethod("(Landroid/graphics/Point;)Landroid/hardware/camera2/params/Face$Builder;")
        setScore = JavaMethod("(I)Landroid/hardware/camera2/params/Face$Builder;")
        setId = JavaMethod("(I)Landroid/hardware/camera2/params/Face$Builder;")
        build = JavaMethod("()Landroid/hardware/camera2/params/Face;")
        setBounds = JavaMethod("(Landroid/graphics/Rect;)Landroid/hardware/camera2/params/Face$Builder;")