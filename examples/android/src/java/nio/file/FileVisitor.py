from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileVisitor"]

class FileVisitor(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileVisitor"
    preVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    visitFile = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    visitFileFailed = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")
    postVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")