from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Camera"]

class Camera(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Camera"
    __javaconstructor__ = [("()V", False)]
    save = JavaMethod("()V")
    restore = JavaMethod("()V")
    translate = JavaMethod("(FFF)V")
    rotateX = JavaMethod("(F)V")
    rotateY = JavaMethod("(F)V")
    rotateZ = JavaMethod("(F)V")
    rotate = JavaMethod("(FFF)V")
    getLocationX = JavaMethod("()F")
    getLocationY = JavaMethod("()F")
    getLocationZ = JavaMethod("()F")
    setLocation = JavaMethod("(FFF)V")
    getMatrix = JavaMethod("(Landroid/graphics/Matrix;)V")
    applyToCanvas = JavaMethod("(Landroid/graphics/Canvas;)V")
    dotWithNormal = JavaMethod("(FFF)F")
    finalize = JavaMethod("()V")