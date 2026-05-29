from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Camera"]

class Camera(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Camera"
    __javaconstructor__ = [("()V", False)]
    getLocationX = JavaMethod("()F")
    getLocationY = JavaMethod("()F")
    getLocationZ = JavaMethod("()F")
    rotateY = JavaMethod("(F)V")
    rotateZ = JavaMethod("(F)V")
    rotateX = JavaMethod("(F)V")
    applyToCanvas = JavaMethod("(Landroid/graphics/Canvas;)V")
    dotWithNormal = JavaMethod("(FFF)F")
    save = JavaMethod("()V")
    restore = JavaMethod("()V")
    translate = JavaMethod("(FFF)V")
    getMatrix = JavaMethod("(Landroid/graphics/Matrix;)V")
    setLocation = JavaMethod("(FFF)V")
    rotate = JavaMethod("(FFF)V")