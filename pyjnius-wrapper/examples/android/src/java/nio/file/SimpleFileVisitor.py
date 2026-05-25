from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleFileVisitor"]

class SimpleFileVisitor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/SimpleFileVisitor"
    __javaconstructor__ = [("()V", False)]
    preVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    visitFile = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    visitFileFailed = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")
    postVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")