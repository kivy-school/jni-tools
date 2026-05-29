from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathMatcher"]

class PathMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/PathMatcher"
    matches = JavaMethod("(Ljava/nio/file/Path;)Z")