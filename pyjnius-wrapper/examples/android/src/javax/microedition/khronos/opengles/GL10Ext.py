from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GL10Ext"]

class GL10Ext(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/opengles/GL10Ext"
    glQueryMatrixxOES = JavaMultipleMethod([("([II[II)I", False, False), ("(Ljava/nio/IntBuffer;Ljava/nio/IntBuffer;)I", False, False)])