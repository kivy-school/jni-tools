from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileVisitor"]

class FileVisitor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileVisitor"
    visitFile = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    visitFileFailed = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")
    preVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    postVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")