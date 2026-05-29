from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GLU"]

class GLU(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/GLU"
    __javaconstructor__ = [("()V", False)]
    gluOrtho2D = JavaStaticMethod("(Ljavax/microedition/khronos/opengles/GL10;FFFF)V")
    gluPerspective = JavaStaticMethod("(Ljavax/microedition/khronos/opengles/GL10;FFFF)V")
    gluErrorString = JavaStaticMethod("(I)Ljava/lang/String;")
    gluLookAt = JavaStaticMethod("(Ljavax/microedition/khronos/opengles/GL10;FFFFFFFFF)V")
    gluProject = JavaStaticMethod("(FFF[FI[FI[II[FI)I")
    gluUnProject = JavaStaticMethod("(FFF[FI[FI[II[FI)I")