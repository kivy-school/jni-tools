from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GLES10Ext"]

class GLES10Ext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/GLES10Ext"
    __javaconstructor__ = [("()V", False)]
    glQueryMatrixxOES = JavaMultipleMethod([("([II[II)I", True, False), ("(Ljava/nio/IntBuffer;Ljava/nio/IntBuffer;)I", True, False)])