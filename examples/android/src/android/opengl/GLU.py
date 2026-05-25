from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GLU"]

class GLU(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/GLU"
    __javaconstructor__ = [("()V", False)]
    gluErrorString = JavaStaticMethod("(I)Ljava/lang/String;")
    gluLookAt = JavaStaticMethod("(Ljavax/microedition/khronos/opengles/GL10;FFFFFFFFF)V")
    gluOrtho2D = JavaStaticMethod("(Ljavax/microedition/khronos/opengles/GL10;FFFF)V")
    gluPerspective = JavaStaticMethod("(Ljavax/microedition/khronos/opengles/GL10;FFFF)V")
    gluProject = JavaStaticMethod("(FFF[FI[FI[II[FI)I")
    gluUnProject = JavaStaticMethod("(FFF[FI[FI[II[FI)I")