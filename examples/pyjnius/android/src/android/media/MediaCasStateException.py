from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCasStateException"]

class MediaCasStateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCasStateException"
    getDiagnosticInfo = JavaMethod("()Ljava/lang/String;")